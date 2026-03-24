import pygame
import random
import math
from game.constants import *
from game.asset_manager import make_customer_sprite, make_speech_bubble


class Customer(pygame.sprite.Sprite):
    """
    NPC customer that walks to a waiting spot, waits for an item, pays, and leaves.
    """

    STATES = ["walking_in", "waiting", "served", "leaving"]

    def __init__(self, spawn_x: int, wait_x: int, wait_y: int, index: int = 0):
        super().__init__()
        self.image      = make_customer_sprite(index)
        self.rect       = self.image.get_rect(midbottom=(spawn_x, SCREEN_H - 20))
        self.pos        = pygame.math.Vector2(spawn_x, SCREEN_H - 20)
        self.speed      = CUSTOMER_SPEED + random.randint(-10, 20)

        self._wait_pos  = pygame.math.Vector2(wait_x, wait_y)
        self._leave_x   = random.choice([-60, SCREEN_W + 60])

        self.state      = "walking_in"
        self._patience  = random.uniform(12.0, 22.0)
        self._wait_timer= 0.0
        self.wants      = random.choice(["bubble", "food"])
        self.satisfied  = False
        self.done       = False          

        self._bubble    = None
        self._bubble_timer = 0.0
        self._bob_phase = random.uniform(0, math.pi * 2)

        self._want_text = "🧋 Bubble Tea?" if self.wants == "bubble" else "🍔 Food please!"
        self._thought_surf = make_speech_bubble(self._want_text, 13)

    def update(self, dt: float):
        self._bob_phase += dt * 2

        if self.state == "walking_in":
            self._move_toward(self._wait_pos, dt)
            if self._close_to(self._wait_pos, 10):
                self.state = "waiting"

        elif self.state == "waiting":
            self._wait_timer += dt
            if self._wait_timer >= self._patience:
                self.state = "leaving"

        elif self.state == "served":
            self._wait_timer += dt
            if self._wait_timer > 1.0:
                self.state = "leaving"

        elif self.state == "leaving":
            target = pygame.math.Vector2(self._leave_x, self.pos.y)
            self._move_toward(target, dt)
            if abs(self.pos.x - self._leave_x) < 20:
                self.done = True

        self.rect.midbottom = (int(self.pos.x), int(self.pos.y))

    def _move_toward(self, target: pygame.math.Vector2, dt: float):
        diff = target - self.pos
        if diff.length() > 2:
            self.pos += diff.normalize() * self.speed * dt

    def _close_to(self, target: pygame.math.Vector2, threshold: float) -> bool:
        return (self.pos - target).length() <= threshold

    def serve(self, item_type: str) -> int:
        """
        Attempt to serve customer. Returns price earned or 0 if wrong item.
        """
        if self.state == "waiting" and item_type == self.wants:
            self.satisfied  = True
            self.state      = "served"
            self._wait_timer= 0
            self._thought_surf = make_speech_bubble("😊 Thank you!", 13)
            return BUBBLE_TEA_PRICE if self.wants == "bubble" else random.randint(FOOD_PRICE_MIN, FOOD_PRICE_MAX)
        return 0

    def draw(self, surface: pygame.Surface):
        bob = int(math.sin(self._bob_phase) * 2) if self.state == "waiting" else 0

        draw_rect = self.rect.move(0, bob)
        surface.blit(self.image, draw_rect)

        if self.state in ("waiting", "served") and not self.done:
            bx = draw_rect.centerx - self._thought_surf.get_width() // 2
            by = draw_rect.top - self._thought_surf.get_height() - 4
            surface.blit(self._thought_surf, (bx, by))

        if self.state == "waiting":
            bar_w = CUSTOMER_W
            prog  = 1.0 - (self._wait_timer / self._patience)
            color = GREEN if prog > 0.5 else (YELLOW if prog > 0.25 else RED)
            bx    = draw_rect.left
            by    = draw_rect.top - 10
            pygame.draw.rect(surface, DARK_GRAY, (bx, by, bar_w, 5), border_radius=2)
            pygame.draw.rect(surface, color,     (bx, by, int(bar_w * prog), 5), border_radius=2)
