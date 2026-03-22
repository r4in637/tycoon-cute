import pygame
import random
from game.constants import *
from game.asset_manager import make_background
from game.player   import Player
from game.machine  import Machine
from game.dropper  import Dropper
from game.customer import Customer
from game.weather  import WeatherSystem
from game.hud      import HUD


class Game:
    """
    Central game controller.
    Owns all game objects and orchestrates update / draw.
    """

    def __init__(self, screen: pygame.Surface):
        self.screen  = screen
        self.running = True

        # ── background ──────────────────────────
        self._bg = make_background(SCREEN_W, SCREEN_H)

        # ── game objects ────────────────────────
        floor_mid_y = FLOOR_Y + 40

        # Player starts near the counter
        self.player = Player(200, floor_mid_y + 20)

        # Machines (on the counter / back wall)
        self.machines: list[Machine] = [
            Machine(160,  FLOOR_Y,       "bubble"),
            Machine(260,  FLOOR_Y,       "food"),
            Machine(380,  FLOOR_Y,       "bubble"),
            Machine(500,  FLOOR_Y,       "food"),
        ]

        # Droppers (cash registers on floor)
        self.droppers: list[Dropper] = [
            Dropper(700,  FLOOR_Y + 60,  reward=2),
            Dropper(900,  FLOOR_Y + 60,  reward=3),
            Dropper(1100, FLOOR_Y + 60,  reward=2),
        ]

        # Customer waiting spots
        self._wait_spots = [
            (680,  FLOOR_Y + 120),
            (820,  FLOOR_Y + 100),
            (960,  FLOOR_Y + 130),
            (1100, FLOOR_Y + 110),
        ]
        self._spot_occupied = [False] * len(self._wait_spots)
        self.customers: list[Customer] = []

        self._spawn_timer    = 0.0
        self._spawn_interval = CUSTOMER_SPAWN_INTERVAL
        self._customer_index = 0

        # ── systems ──────────────────────────────
        self.weather = WeatherSystem(SCREEN_W, SCREEN_H)
        self.hud     = HUD(SCREEN_W, SCREEN_H)

    # ──────────────────────────────────────────
    def handle_event(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_e, pygame.K_SPACE):
                self._try_interact_machine()
                self._try_interact_dropper()
            elif event.key == pygame.K_f:
                self._try_sell_to_customer()

    # ──────────────────────────────────────────
    def update(self, dt: float):
        self.player.update(dt)

        for m in self.machines:
            m.update(dt)
        for d in self.droppers:
            d.update(dt)

        # spawn customers
        self._spawn_timer += dt
        if self._spawn_timer >= self._spawn_interval:
            self._spawn_timer = 0
            self._spawn_interval = random.uniform(
                CUSTOMER_SPAWN_INTERVAL * 0.7,
                CUSTOMER_SPAWN_INTERVAL * 1.3
            )
            self._try_spawn_customer()

        # update customers
        for c in self.customers:
            c.update(dt)

        # free spots of done customers
        for c in self.customers:
            if c.done:
                self._free_spot(c)
        self.customers = [c for c in self.customers if not c.done]

        self.weather.update(dt)
        self.hud.update(dt)

        # auto-interact with droppers when walking over them
        self._auto_dropper()

    # ──────────────────────────────────────────
    def _try_interact_machine(self):
        """Pick up item from nearest ready machine."""
        for m in self.machines:
            if m.get_interact_rect().colliderect(self.player.rect):
                item = m.collect()
                if item:
                    if self.player.pick_up(item):
                        self.hud.add_notification(f"+{item['label']}!", TEAL)
                    else:
                        # put it back
                        m.ready = True
                        self.hud.add_notification("Bag full!", RED)
                    break

    def _try_interact_dropper(self):
        """Collect money from dropper."""
        for d in self.droppers:
            if d.get_interact_rect().colliderect(self.player.rect):
                amount = d.collect()
                if amount:
                    self.player.earn(amount)
                    self.hud.add_notification(f"+${amount} bonus!", YELLOW)

    def _auto_dropper(self):
        """Silently collect ready dropper if player stands on it."""
        for d in self.droppers:
            if d.ready and d.rect.colliderect(self.player.rect):
                amount = d.collect()
                if amount:
                    self.player.earn(amount)
                    self.hud.add_notification(f"+${amount} bonus!", YELLOW)

    def _try_sell_to_customer(self):
        """Sell first inventory item to nearest waiting customer."""
        if not self.player.inventory:
            self.hud.add_notification("Nothing to sell!", GRAY)
            return

        best_c   = None
        best_dist = 200.0

        for c in self.customers:
            if c.state != "waiting":
                continue
            dist = (pygame.math.Vector2(c.rect.center) -
                    pygame.math.Vector2(self.player.rect.center)).length()
            if dist < best_dist:
                best_dist = dist
                best_c    = c

        if best_c is None:
            self.hud.add_notification("No customer nearby!", GRAY)
            return

        # try selling matching item first
        item_type = self.player.inventory[0]["type"]
        earned    = best_c.serve(item_type)

        if earned > 0:
            self.player.inventory.pop(0)
            self.player.earn(earned)
            self.hud.record_sale(earned)
            self.hud.add_notification(f"Sold! +${earned} 🎉", GREEN)
        else:
            self.hud.add_notification(
                f"Customer wants {'🧋' if best_c.wants == 'bubble' else '🍔'}!", ORANGE
            )

    # ──────────────────────────────────────────
    def _try_spawn_customer(self):
        free_spots = [i for i, occ in enumerate(self._spot_occupied) if not occ]
        if not free_spots:
            return
        spot_idx   = random.choice(free_spots)
        wx, wy     = self._wait_spots[spot_idx]
        spawn_x    = random.choice([-40, SCREEN_W + 40])
        c = Customer(spawn_x, wx, wy, self._customer_index % 5)
        c._spot_idx = spot_idx
        self._spot_occupied[spot_idx] = True
        self.customers.append(c)
        self._customer_index += 1

    def _free_spot(self, customer: Customer):
        idx = getattr(customer, "_spot_idx", None)
        if idx is not None and 0 <= idx < len(self._spot_occupied):
            self._spot_occupied[idx] = False

    # ──────────────────────────────────────────
    def draw(self):
        # 1. Static background
        self.screen.blit(self._bg, (0, 0))

        # 2. Weather: dark sky overlay + clouds
        self.weather.draw_sky_overlay(self.screen)
        self.weather.draw_clouds(self.screen)

        # 3. Machines & droppers
        for m in self.machines:
            m.draw(self.screen)
        for d in self.droppers:
            d.draw(self.screen)

        # 4. Customers (sorted by y for pseudo-depth)
        all_chars = sorted(
            self.customers + [self.player],
            key=lambda obj: obj.rect.bottom
        )
        for obj in all_chars:
            obj.draw(self.screen)

        # 5. Rain overlay (on top of characters)
        self.weather.draw_rain(self.screen)

        # 6. HUD (always on top)
        self.hud.draw(self.screen, self.player, self.weather)
