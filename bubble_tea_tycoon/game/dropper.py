import pygame
from game.constants import *
from game.asset_manager import make_dropper, make_coin
import math


class Dropper(pygame.sprite.Sprite):
    """
    A floor spot that periodically drops money when the player stands on it.
    """

    def __init__(self, x: int, y: int, reward: int = 2):
        super().__init__()
        self.image  = make_dropper()
        self.rect   = self.image.get_rect(midbottom=(x, y))
        self.reward = reward

        self._timer    = 0.0
        self._interval = DROPPER_REWARD_INTERVAL
        self.ready     = False

        self._coin_surf = make_coin()
        self._coins: list[dict] = []   # animated coin particles

        self._pulse = 0.0

    # ──────────────────────────────────────────
    def update(self, dt: float):
        self._timer += dt
        if self._timer >= self._interval:
            self._timer = 0
            self.ready  = True

        # update coin particles
        for c in self._coins:
            c["y"]     -= 60 * dt
            c["alpha"] -= 255 * dt
        self._coins = [c for c in self._coins if c["alpha"] > 0]

        self._pulse += dt * 3

    # ──────────────────────────────────────────
    def collect(self) -> int:
        """Returns reward amount if ready, else 0."""
        if self.ready:
            self.ready = False
            # spawn coin particle
            self._coins.append({
                "x": float(self.rect.centerx),
                "y": float(self.rect.top),
                "alpha": 255.0,
            })
            return self.reward
        return 0

    # ──────────────────────────────────────────
    def draw(self, surface: pygame.Surface):
        # glow ring when ready
        if self.ready:
            radius = int(38 + 4 * math.sin(self._pulse))
            glow   = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
            pygame.draw.circle(glow, (80, 230, 100, 80), (radius, radius), radius)
            surface.blit(glow, (self.rect.centerx - radius, self.rect.centery - radius))

        surface.blit(self.image, self.rect)

        # progress ring
        if not self.ready:
            prog  = self._timer / self._interval
            angle = int(360 * prog)
            if angle > 0:
                pygame.draw.arc(
                    surface, GREEN,
                    (self.rect.left - 5, self.rect.top - 5,
                     self.rect.width + 10, self.rect.height + 10),
                    math.radians(90), math.radians(90 + angle), 4
                )

        # coin particles
        for c in self._coins:
            alpha_surf = self._coin_surf.copy()
            alpha_surf.set_alpha(int(c["alpha"]))
            surface.blit(alpha_surf, (int(c["x"]) - 10, int(c["y"])))

        # "$" label
        font = pygame.font.SysFont("arial", 12, bold=True)
        if self.ready:
            lbl = font.render(f"+${self.reward} STEP ON!", True, GREEN)
        else:
            remaining = int(self._interval - self._timer) + 1
            lbl = font.render(f"⏱ {remaining}s", True, GRAY)
        surface.blit(lbl, (self.rect.centerx - lbl.get_width() // 2, self.rect.top - 20))

    # ──────────────────────────────────────────
    def get_interact_rect(self) -> pygame.Rect:
        return self.rect.inflate(20, 20)
