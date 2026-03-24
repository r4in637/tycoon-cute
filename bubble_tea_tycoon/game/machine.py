'''
Vending machine that periodically produces items.
Player walks into it to pick up produced items.
'''

import pygame
from game.constants import *
from game.asset_manager import make_bubble_machine, make_food_machine, make_bubble_tea, make_food_item
import random


class Machine(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, kind: str = "bubble"):
        super().__init__()
        self.kind = kind

        if kind == "bubble":
            self.image = make_bubble_machine()
        else:
            self.image = make_food_machine()

        self.rect = self.image.get_rect(midbottom=(x, y))

        self._produce_timer = 0.0
        self._produce_time  = MACHINE_PRODUCE_TIME
        self.ready          = False
        self._item_ready_surf = None

        self._progress_color = TEAL if kind == "bubble" else ORANGE

        if kind == "bubble":
            colors = [PINK, (180, 220, 255), (200, 255, 180), PURPLE]
            self._item_surfs = [make_bubble_tea(c) for c in colors]
        else:
            self._item_surfs = [make_food_item(i) for i in range(4)]

    def _make_item(self) -> dict:
        icon = random.choice(self._item_surfs)
        if self.kind == "bubble":
            price = BUBBLE_TEA_PRICE
            label = "Bubble Tea"
        else:
            price = random.randint(FOOD_PRICE_MIN, FOOD_PRICE_MAX)
            label = random.choice(["Burger", "Sandwich", "Cookie", "Donut"])
        return {"type": self.kind, "price": price, "label": label, "icon": icon}

    def update(self, dt: float):
        if not self.ready:
            self._produce_timer += dt
            if self._produce_timer >= self._produce_time:
                self._produce_timer = 0
                self.ready          = True
                self._item_ready_surf = random.choice(self._item_surfs)

    def collect(self) -> dict | None:
        if self.ready:
            self.ready = False
            return self._make_item()
        return None

    def draw(self, surface: pygame.Surface):
        surface.blit(self.image, self.rect)

        if not self.ready:
            bar_w = self.rect.width - 10
            prog  = self._produce_timer / self._produce_time
            bar_x = self.rect.left + 5
            bar_y = self.rect.top - 14
            pygame.draw.rect(surface, DARK_GRAY,          (bar_x, bar_y, bar_w, 8), border_radius=4)
            pygame.draw.rect(surface, self._progress_color,(bar_x, bar_y, int(bar_w * prog), 8), border_radius=4)
        else:
            font = pygame.font.SysFont("arial", 11, bold=True)
            lbl  = font.render("✓ READY!", True, GREEN)
            surface.blit(lbl, (self.rect.centerx - lbl.get_width() // 2, self.rect.top - 18))
            
            if self._item_ready_surf:
                iy = self.rect.top - 20 - abs(int(pygame.time.get_ticks() / 300 % 8) - 4)
                surface.blit(self._item_ready_surf,
                             (self.rect.centerx - self._item_ready_surf.get_width() // 2, iy))

    def get_interact_rect(self) -> pygame.Rect:
        return self.rect.inflate(30, 30)