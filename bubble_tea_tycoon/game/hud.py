'''
Heads-up display: money, inventory, weather indicator, controls help.
Manages visual interface and floating notifications.
'''

import pygame
from game.constants import *


class HUD:
    def __init__(self, screen_w: int, screen_h: int):
        self.screen_w  = screen_w
        self.screen_h  = screen_h
        self._font_big = pygame.font.SysFont("arial", 22, bold=True)
        self._font_med = pygame.font.SysFont("arial", 16)
        self._font_sm  = pygame.font.SysFont("arial", 13)

        self._notifications: list[dict] = []
        self._total_earned  = 0
        self._customers_served = 0

    def add_notification(self, text: str, color=GREEN):
        self._notifications.append({
            "text":  text,
            "color": color,
            "y":     float(self.screen_h - 80),
            "alpha": 255.0,
            "timer": 0.0,
        })

    def record_sale(self, amount: int):
        self._total_earned     += amount
        self._customers_served += 1

    def update(self, dt: float):
        for n in self._notifications:
            n["timer"] += dt
            n["y"]     -= 40 * dt
            if n["timer"] > 1.5:
                n["alpha"] -= 400 * dt
        self._notifications = [n for n in self._notifications if n["alpha"] > 0]

    def draw(self, surface: pygame.Surface, player, weather):
        bar = pygame.Surface((self.screen_w, HUD_HEIGHT), pygame.SRCALPHA)
        bar.fill((20, 20, 30, 210))
        surface.blit(bar, (0, 0))

        money_txt = self._font_big.render(f"💰 ${player.money}", True, YELLOW)
        surface.blit(money_txt, (16, 16))

        inv_x = 220
        inv_label = self._font_med.render("Bag:", True, LIGHT_GRAY)
        surface.blit(inv_label, (inv_x, 20))
        inv_x += 50
        for i, item in enumerate(player.inventory):
            icon = item.get("icon")
            if icon:
                small = pygame.transform.scale(icon, (28, 28))
                surface.blit(small, (inv_x + i * 32, 16))

        for i in range(player.max_items):
            color = DARK_GRAY if i >= len(player.inventory) else GREEN
            pygame.draw.rect(surface, color, (inv_x + i * 32, 44, 28, 4))

        stat_txt = self._font_sm.render(
            f"Served: {self._customers_served}   Total earned: ${self._total_earned}",
            True, LIGHT_GRAY
        )
        surface.blit(stat_txt, (self.screen_w // 2 - stat_txt.get_width() // 2, 22))

        if weather.is_raining:
            w_txt = self._font_med.render("🌧 Rainy", True, LIGHT_BLUE)
        else:
            w_txt = self._font_med.render("☀ Clear", True, YELLOW)
        surface.blit(w_txt, (self.screen_w - 130, 18))

        help_bg = pygame.Surface((self.screen_w, 26), pygame.SRCALPHA)
        help_bg.fill((0, 0, 0, 140))
        surface.blit(help_bg, (0, self.screen_h - 26))
        help_txt = self._font_sm.render(
            "WASD/Arrows: Move  |  E / Space: Interact with machine or dropper  |  F: Sell to nearest customer",
            True, LIGHT_GRAY
        )
        surface.blit(help_txt, (self.screen_w // 2 - help_txt.get_width() // 2, self.screen_h - 22))

        for n in self._notifications:
            ns = self._font_big.render(n["text"], True, n["color"])
            ns.set_alpha(int(max(0, n["alpha"])))
            surface.blit(ns, (self.screen_w // 2 - ns.get_width() // 2, int(n["y"])))