'''
The player-controlled seller character.
Moves with WASD / arrow keys and carries items picked up from machines.
'''

import pygame
from game.constants import *
from game.asset_manager import make_player_sprite


class Player(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float):
        super().__init__()
        self._sprites = {
            d: make_player_sprite(d)
            for d in ("down", "up", "left", "right")
        }
        self.direction  = "down"
        self.image      = self._sprites[self.direction]
        self.rect       = self.image.get_rect(midbottom=(x, y))

        self.pos        = pygame.math.Vector2(x, y)
        self.speed      = PLAYER_SPEED
        self.inventory  = []
        self.max_items  = 5
        self.money      = 0

        self._anim_timer = 0.0
        self._frame      = 0

    def handle_input(self) -> pygame.math.Vector2:
        keys  = pygame.key.get_pressed()
        vel   = pygame.math.Vector2(0, 0)

        if keys[pygame.K_LEFT]  or keys[pygame.K_a]:
            vel.x = -1
            self.direction = "left"
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            vel.x =  1
            self.direction = "right"
        if keys[pygame.K_UP]    or keys[pygame.K_w]:
            vel.y = -1
            self.direction = "up"
        if keys[pygame.K_DOWN]  or keys[pygame.K_s]:
            vel.y =  1
            self.direction = "down"

        if vel.length() > 0:
            vel = vel.normalize()
        return vel

    def update(self, dt: float):
        vel = self.handle_input()
        self.pos += vel * self.speed * dt

        half_w = PLAYER_W / 2
        self.pos.x = max(half_w, min(SCREEN_W - half_w, self.pos.x))
        self.pos.y = max(FLOOR_Y + 10, min(SCREEN_H - 10, self.pos.y))

        self.rect.midbottom = (int(self.pos.x), int(self.pos.y))

        if vel.length() > 0:
            self._anim_timer += dt
            if self._anim_timer > 0.2:
                self._anim_timer = 0
                self._frame      = 1 - self._frame
        else:
            self._frame = 0

        self.image = self._sprites[self.direction]

    def pick_up(self, item: dict) -> bool:
        if len(self.inventory) < self.max_items:
            self.inventory.append(item)
            return True
        return False

    def sell_item(self) -> int:
        if self.inventory:
            item = self.inventory.pop(0)
            earned = item["price"]
            self.money += earned
            return earned
        return 0

    def earn(self, amount: int):
        self.money += amount

    def draw(self, surface: pygame.Surface):
        surface.blit(self.image, self.rect)

        for i, item in enumerate(self.inventory):
            icon = item.get("icon")
            if icon:
                ix = self.rect.centerx - 10
                iy = self.rect.top - 20 - i * 12
                surface.blit(icon, (ix, iy))