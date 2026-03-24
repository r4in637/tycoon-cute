'''
Manages weather transitions: clear ↔ rain.
Handles clouds movement, sky overlays, and rain drop physics.
'''

import pygame
import random
import math
from game.constants import *


class WeatherSystem:
    def __init__(self, screen_w: int, screen_h: int):
        self.screen_w = screen_w
        self.screen_h = screen_h

        self.state          = "clear"
        self._transition    = 0.0
        self._timer         = 0.0
        self._change_at     = random.uniform(30.0, 60.0)

        self._drops: list[dict] = []
        self._init_drops()

        self._overlay       = pygame.Surface((screen_w, screen_h), pygame.SRCALPHA)
        self._cloud_x       = [random.randint(0, screen_w) for _ in range(6)]
        self._cloud_speeds  = [random.uniform(10, 25) for _ in range(6)]

    def _init_drops(self):
        self._drops = [
            {
                "x": random.uniform(0, self.screen_w),
                "y": random.uniform(-self.screen_h, 0),
                "speed": random.uniform(400, 700),
                "length": random.randint(8, 18),
                "alpha": random.randint(80, 180),
            }
            for _ in range(RAIN_DROP_COUNT)
        ]

    def update(self, dt: float):
        self._timer += dt

        if self._timer >= self._change_at:
            self._timer    = 0
            self._change_at = random.uniform(25.0, 55.0)
            self.state     = "raining" if self.state == "clear" else "clear"

        target = 1.0 if self.state == "raining" else 0.0
        self._transition += (target - self._transition) * dt * 0.8
        self._transition  = max(0.0, min(1.0, self._transition))

        for i in range(len(self._cloud_x)):
            self._cloud_x[i] = (self._cloud_x[i] + self._cloud_speeds[i] * dt) % (self.screen_w + 200)

        if self._transition > 0.01:
            for d in self._drops:
                d["y"] += d["speed"] * dt
                if d["y"] > self.screen_h:
                    d["y"] = random.uniform(-60, -10)
                    d["x"] = random.uniform(0, self.screen_w)

    def draw_sky_overlay(self, surface: pygame.Surface):
        if self._transition < 0.01:
            return
        alpha = int(80 * self._transition)
        self._overlay.fill((0, 0, 0, 0))
        pygame.draw.rect(self._overlay, (30, 40, 60, alpha),
                         (0, 0, self.screen_w, FLOOR_Y))
        surface.blit(self._overlay, (0, 0))

    def draw_rain(self, surface: pygame.Surface):
        if self._transition < 0.01:
            return
        for d in self._drops:
            a = int(d["alpha"] * self._transition)
            if a <= 0:
                continue
            start = (int(d["x"]), int(d["y"]))
            end   = (int(d["x"]) - 2, int(d["y"] + d["length"]))
            pygame.draw.line(surface, (120, 160, 255), start, end, 1)

    def draw_clouds(self, surface: pygame.Surface):
        if self._transition < 0.05:
            return
        alpha = int(200 * self._transition)
        cloud_surf = pygame.Surface((self.screen_w, FLOOR_Y), pygame.SRCALPHA)
        for i, cx in enumerate(self._cloud_x):
            cy    = 50 + (i % 3) * 30
            radii = [40, 30, 35, 25, 20]
            offsets = [(-30, 0), (0, -15), (30, 0), (55, 5), (-55, 5)]
            for (ox, oy), r in zip(offsets, radii):
                pygame.draw.circle(cloud_surf, (180, 180, 200, alpha),
                                   (int(cx + ox), cy + oy), r)
        surface.blit(cloud_surf, (0, 0))

    @property
    def is_raining(self) -> bool:
        return self.state == "raining"

    @property
    def transition(self) -> float:
        return self._transition