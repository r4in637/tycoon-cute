"""
asset_manager.py
Generates all game graphics programmatically with pygame.draw calls.
No external image files are required.
"""
import pygame
import math
from game.constants import *


def _surf(w, h, alpha=True):
    s = pygame.Surface((w, h), pygame.SRCALPHA if alpha else 0)
    return s


# ──────────────────────────────────────────────
#  PLAYER  (seller character)
# ──────────────────────────────────────────────
def make_player_sprite(direction="down"):
    s = _surf(PLAYER_W, PLAYER_H)

    body_color   = (70, 130, 200)
    skin_color   = (255, 220, 180)
    apron_color  = (255, 255, 255)
    hair_color   = (60, 40, 20)

    # legs
    pygame.draw.rect(s, (40, 80, 160), (6, 36, 10, 20), border_radius=3)
    pygame.draw.rect(s, (40, 80, 160), (20, 36, 10, 20), border_radius=3)
    # shoes
    pygame.draw.ellipse(s, (30, 30, 30), (4, 52, 14, 6))
    pygame.draw.ellipse(s, (30, 30, 30), (18, 52, 14, 6))
    # body
    pygame.draw.rect(s, body_color, (4, 18, 28, 22), border_radius=4)
    # apron
    pygame.draw.rect(s, apron_color, (9, 20, 18, 18), border_radius=3)
    # arms
    pygame.draw.rect(s, body_color, (0, 20, 6, 16), border_radius=3)
    pygame.draw.rect(s, body_color, (30, 20, 6, 16), border_radius=3)
    # hands
    pygame.draw.ellipse(s, skin_color, (0, 34, 8, 8))
    pygame.draw.ellipse(s, skin_color, (28, 34, 8, 8))
    # head
    pygame.draw.ellipse(s, skin_color, (6, 2, 24, 20))
    # hair
    pygame.draw.ellipse(s, hair_color, (5, 1, 26, 12))
    # eyes
    if direction != "up":
        pygame.draw.circle(s, (30, 30, 30), (13, 11), 2)
        pygame.draw.circle(s, (30, 30, 30), (23, 11), 2)
        # smile
        pygame.draw.arc(s, (180, 80, 80), (11, 13, 14, 7), math.pi, 2 * math.pi, 2)

    return s


# ──────────────────────────────────────────────
#  CUSTOMER
# ──────────────────────────────────────────────
_CUSTOMER_PALETTES = [
    ((200, 80, 80),  (255, 210, 160), (150, 50, 50)),
    ((80,  160, 80), (255, 220, 180), (50, 120, 50)),
    ((80,  80,  200),(255, 200, 150), (50, 50, 150)),
    ((200, 160, 80), (240, 200, 170), (150, 110, 40)),
    ((160, 80,  200),(255, 215, 185), (100, 50, 160)),
]

def make_customer_sprite(index=0):
    s = _surf(CUSTOMER_W, CUSTOMER_H)
    body, skin, dark = _CUSTOMER_PALETTES[index % len(_CUSTOMER_PALETTES)]

    # legs
    pygame.draw.rect(s, dark, (4, 30, 9, 20), border_radius=3)
    pygame.draw.rect(s, dark, (17, 30, 9, 20), border_radius=3)
    pygame.draw.ellipse(s, (20, 20, 20), (2, 46, 12, 6))
    pygame.draw.ellipse(s, (20, 20, 20), (16, 46, 12, 6))
    # body
    pygame.draw.rect(s, body, (2, 14, 28, 20), border_radius=4)
    # arms
    pygame.draw.rect(s, body, (0, 16, 4, 14), border_radius=2)
    pygame.draw.rect(s, body, (28, 16, 4, 14), border_radius=2)
    pygame.draw.ellipse(s, skin, (0, 28, 6, 6))
    pygame.draw.ellipse(s, skin, (26, 28, 6, 6))
    # head
    pygame.draw.ellipse(s, skin, (5, 1, 22, 18))
    # hair
    pygame.draw.ellipse(s, dark, (4, 0, 24, 10))
    # eyes
    pygame.draw.circle(s, (30, 30, 30), (11, 9), 2)
    pygame.draw.circle(s, (30, 30, 30), (21, 9), 2)

    return s


# ──────────────────────────────────────────────
#  BUBBLE TEA MACHINE
# ──────────────────────────────────────────────
def make_bubble_machine():
    s = _surf(MACHINE_W, MACHINE_H)

    # body
    pygame.draw.rect(s, (60, 60, 80), (5, 20, 70, 70), border_radius=8)
    # top funnel
    pygame.draw.polygon(s, (90, 90, 120), [(20, 0), (60, 0), (65, 20), (15, 20)])
    # screen / display
    pygame.draw.rect(s, (30, 200, 200), (15, 30, 50, 25), border_radius=4)
    pygame.draw.rect(s, (0, 240, 240), (18, 33, 44, 19), border_radius=3)
    # bubbles on screen
    for bx, by in [(26, 40), (36, 43), (46, 39), (56, 42)]:
        pygame.draw.circle(s, (0, 80, 80), (bx, by), 4)
    # button panel
    pygame.draw.rect(s, (50, 50, 70), (10, 60, 60, 20), border_radius=4)
    for bx in [20, 35, 55]:
        pygame.draw.circle(s, PINK, (bx, 70), 5)
    # nozzle
    pygame.draw.rect(s, (40, 40, 60), (32, 80, 16, 10))
    pygame.draw.ellipse(s, TEAL, (30, 87, 20, 8))
    # label
    font = pygame.font.SysFont("arial", 9, bold=True)
    lbl = font.render("BOBA", True, WHITE)
    s.blit(lbl, (22, 50))
    return s


# ──────────────────────────────────────────────
#  FOOD MACHINE
# ──────────────────────────────────────────────
def make_food_machine():
    s = _surf(MACHINE_W, MACHINE_H)

    # body
    pygame.draw.rect(s, (180, 80, 50), (5, 15, 70, 75), border_radius=8)
    # top
    pygame.draw.rect(s, (220, 110, 70), (5, 10, 70, 12), border_radius=4)
    # glass window
    pygame.draw.rect(s, (200, 230, 255, 160), (12, 22, 56, 40), border_radius=4)
    pygame.draw.rect(s, (150, 200, 240, 80), (14, 24, 52, 36), border_radius=3)
    # food items inside window
    pygame.draw.ellipse(s, YELLOW,  (18, 32, 18, 12))   # sandwich
    pygame.draw.ellipse(s, ORANGE,  (42, 28, 16, 14))   # burger
    pygame.draw.rect(s,   BROWN,    (20, 44, 14, 10), border_radius=2)  # cookie
    # dispenser slot
    pygame.draw.rect(s, (100, 40, 20), (20, 80, 40, 8), border_radius=3)
    # buttons
    pygame.draw.rect(s, (80, 30, 10), (12, 64, 56, 14), border_radius=4)
    for bx in [22, 35, 48, 60]:
        pygame.draw.circle(s, YELLOW, (bx, 71), 4)
    # label
    font = pygame.font.SysFont("arial", 9, bold=True)
    lbl = font.render("FOOD", True, WHITE)
    s.blit(lbl, (25, 50))
    return s


# ──────────────────────────────────────────────
#  DROPPER  (cash register / floor money spot)
# ──────────────────────────────────────────────
def make_dropper():
    s = _surf(DROPPER_W, DROPPER_H)

    # base
    pygame.draw.rect(s, (40, 160, 60), (5, 30, 60, 35), border_radius=6)
    # cash register body
    pygame.draw.rect(s, (50, 50, 50), (8, 5, 54, 32), border_radius=5)
    # screen
    pygame.draw.rect(s, (30, 200, 80), (12, 9, 46, 18), border_radius=3)
    # dollar sign on screen
    font = pygame.font.SysFont("arial", 16, bold=True)
    txt = font.render("$", True, (0, 80, 30))
    s.blit(txt, (30, 10))
    # buttons row
    pygame.draw.rect(s, (30, 30, 30), (10, 29, 50, 6), border_radius=2)
    for bx in [18, 28, 38, 50]:
        pygame.draw.circle(s, (200, 200, 200), (bx, 32), 2)
    # coin slot
    pygame.draw.rect(s, (20, 20, 20), (22, 46, 26, 6), border_radius=2)
    # glow ring (indicates active)
    pygame.draw.ellipse(s, (60, 220, 80, 120), (2, 28, 66, 38))
    return s


# ──────────────────────────────────────────────
#  BUBBLE TEA CUP  (item)
# ──────────────────────────────────────────────
def make_bubble_tea(color=None):
    if color is None:
        color = PINK
    s = _surf(30, 40)
    # cup body
    pygame.draw.polygon(s, color, [(4, 8), (26, 8), (23, 36), (7, 36)])
    # cup highlight
    pygame.draw.polygon(s, (255, 255, 255, 80), [(6, 8), (12, 8), (10, 20)])
    # lid
    pygame.draw.ellipse(s, (200, 200, 200), (2, 4, 26, 8))
    # straw
    pygame.draw.rect(s, (255, 100, 150), (14, 0, 4, 20))
    # bubbles
    for bx, by in [(10, 28), (16, 25), (21, 28)]:
        pygame.draw.circle(s, (80, 40, 20), (bx, by), 3)
    return s


# ──────────────────────────────────────────────
#  FOOD ITEM
# ──────────────────────────────────────────────
def make_food_item(kind=0):
    s = _surf(30, 30)
    if kind == 0:   # sandwich
        pygame.draw.rect(s, (220, 180, 80), (2, 8, 26, 14), border_radius=4)
        pygame.draw.rect(s, (200, 80, 40),  (4, 12, 22, 5))
        pygame.draw.rect(s, (80, 180, 60),  (4, 10, 22, 3))
    elif kind == 1:  # burger
        pygame.draw.ellipse(s, (220, 160, 60), (2, 4, 26, 14))
        pygame.draw.rect(s,   (180, 90, 40),   (4, 13, 22, 8))
        pygame.draw.ellipse(s, (200, 140, 50), (2, 18, 26, 10))
    elif kind == 2:  # cookie
        pygame.draw.circle(s, BROWN, (15, 15), 12)
        for cx, cy in [(10, 10), (18, 14), (12, 19), (20, 10)]:
            pygame.draw.circle(s, (60, 30, 10), (cx, cy), 2)
    else:            # donut
        pygame.draw.circle(s, (240, 160, 100), (15, 15), 12)
        pygame.draw.circle(s, (255, 200, 220), (15, 15), 6)
        pygame.draw.circle(s, (255, 255, 255, 0), (15, 15), 4)
    return s


# ──────────────────────────────────────────────
#  COIN  (floating money pickup)
# ──────────────────────────────────────────────
def make_coin():
    s = _surf(20, 20)
    pygame.draw.circle(s, YELLOW, (10, 10), 9)
    pygame.draw.circle(s, (200, 160, 0), (10, 10), 9, 2)
    font = pygame.font.SysFont("arial", 10, bold=True)
    t = font.render("$", True, (150, 100, 0))
    s.blit(t, (6, 5))
    return s


# ──────────────────────────────────────────────
#  BACKGROUND  (cafe interior)
# ──────────────────────────────────────────────
def make_background(w, h):
    s = pygame.Surface((w, h))

    # sky / wall gradient  (top area)
    wall_h = FLOOR_Y
    for y in range(wall_h):
        t = y / wall_h
        r = int(245 - t * 30)
        g = int(230 - t * 20)
        b = int(200 - t * 10)
        pygame.draw.line(s, (r, g, b), (0, y), (w, y))

    # window (left)
    pygame.draw.rect(s, LIGHT_BLUE, (60, 60, 180, 130), border_radius=6)
    pygame.draw.rect(s, SKY_BLUE,   (65, 65, 170, 120), border_radius=4)
    pygame.draw.rect(s, WHITE,      (60, 60, 180, 130), 4, border_radius=6)
    pygame.draw.line(s, WHITE, (150, 60), (150, 190), 3)
    pygame.draw.line(s, WHITE, (60, 125), (240, 125), 3)
    # clouds in window
    for cx, cy, cr in [(90, 90, 18), (115, 85, 22), (140, 92, 16), (170, 88, 20)]:
        pygame.draw.circle(s, (255, 255, 255, 200), (cx, cy), cr)

    # window (right)
    pygame.draw.rect(s, LIGHT_BLUE, (w - 240, 60, 180, 130), border_radius=6)
    pygame.draw.rect(s, SKY_BLUE,   (w - 235, 65, 170, 120), border_radius=4)
    pygame.draw.rect(s, WHITE,      (w - 240, 60, 180, 130), 4, border_radius=6)
    pygame.draw.line(s, WHITE, (w - 150, 60), (w - 150, 190), 3)
    pygame.draw.line(s, WHITE, (w - 240, 125), (w - 60, 125), 3)
    for cx, cy, cr in [(w - 200, 90, 16), (w - 170, 82, 22), (w - 140, 90, 18)]:
        pygame.draw.circle(s, (255, 255, 255, 200), (cx, cy), cr)

    # wall decorations
    font_big = pygame.font.SysFont("arial", 28, bold=True)
    sign = font_big.render("🧋 Bubble Tea Cafe 🧋", True, (120, 60, 20))
    s.blit(sign, (w // 2 - sign.get_width() // 2, 20))

    # menu board
    pygame.draw.rect(s, (60, 35, 15), (w // 2 - 140, 55, 280, 110), border_radius=8)
    pygame.draw.rect(s, (30, 20, 5),  (w // 2 - 135, 60, 270, 100), border_radius=6)
    mfont = pygame.font.SysFont("arial", 14, bold=True)
    lines = ["☕ MENU", "🧋 Bubble Tea  $3", "🍔 Burger       $3-5", "🥪 Sandwich   $3-5", "🍪 Cookie       $3-5"]
    for i, line in enumerate(lines):
        col = YELLOW if i == 0 else (200, 230, 200)
        txt = mfont.render(line, True, col)
        s.blit(txt, (w // 2 - 120, 65 + i * 19))

    # floor
    for y in range(FLOOR_Y, h, TILE_SIZE):
        for x in range(0, w, TILE_SIZE):
            shade = (180, 140, 100) if (x // TILE_SIZE + y // TILE_SIZE) % 2 == 0 else (165, 125, 90)
            pygame.draw.rect(s, shade, (x, y, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(s, (140, 100, 65), (x, y, TILE_SIZE, TILE_SIZE), 1)

    # floor-wall border
    pygame.draw.rect(s, WOOD, (0, FLOOR_Y - 12, w, 14))
    pygame.draw.rect(s, (100, 65, 30), (0, FLOOR_Y - 14, w, 4))

    # counter / bar
    pygame.draw.rect(s, WOOD, (0, FLOOR_Y, 300, 60))
    pygame.draw.rect(s, (110, 70, 30), (0, FLOOR_Y, 300, 6))
    pygame.draw.rect(s, (190, 140, 80), (0, FLOOR_Y + 6, 300, 54))

    return s


# ──────────────────────────────────────────────
#  RAIN DROP
# ──────────────────────────────────────────────
def make_rain_drop():
    s = _surf(3, 12)
    pygame.draw.line(s, (100, 150, 255, 180), (1, 0), (1, 11), 2)
    return s


# ──────────────────────────────────────────────
#  SPEECH BUBBLE
# ──────────────────────────────────────────────
def make_speech_bubble(text, font_size=14):
    font = pygame.font.SysFont("arial", font_size)
    txt  = font.render(text, True, (40, 40, 40))
    w    = txt.get_width() + 20
    h    = txt.get_height() + 14
    s    = _surf(w + 10, h + 16)
    pygame.draw.rect(s, WHITE,       (0, 0, w, h), border_radius=8)
    pygame.draw.rect(s, DARK_GRAY,   (0, 0, w, h), 2, border_radius=8)
    pygame.draw.polygon(s, WHITE,    [(w // 2 - 6, h), (w // 2 + 6, h), (w // 2, h + 10)])
    pygame.draw.polygon(s, DARK_GRAY,[(w // 2 - 6, h - 1), (w // 2 + 6, h - 1), (w // 2, h + 9)], 2)
    s.blit(txt, (10, 7))
    return s
