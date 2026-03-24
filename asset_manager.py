"""
asset_manager.py
Generates all game graphics programmatically with pygame.draw calls.
No external image files are required.
"""
# import pygame
# import math
# from game.constants import *


# def _surf(w, h, alpha=True):
#     s = pygame.Surface((w, h), pygame.SRCALPHA if alpha else 0)
#     return s


# # ──────────────────────────────────────────────
# #  PLAYER  (seller character)
# # ──────────────────────────────────────────────
# def make_player_sprite(direction="down"):
#     s = _surf(PLAYER_W, PLAYER_H)

#     body_color   = (70, 130, 200)
#     skin_color   = (255, 220, 180)
#     apron_color  = (255, 255, 255)
#     hair_color   = (60, 40, 20)

#     # legs
#     pygame.draw.rect(s, (40, 80, 160), (6, 36, 10, 20), border_radius=3)
#     pygame.draw.rect(s, (40, 80, 160), (20, 36, 10, 20), border_radius=3)
#     # shoes
#     pygame.draw.ellipse(s, (30, 30, 30), (4, 52, 14, 6))
#     pygame.draw.ellipse(s, (30, 30, 30), (18, 52, 14, 6))
#     # body
#     pygame.draw.rect(s, body_color, (4, 18, 28, 22), border_radius=4)
#     # apron
#     pygame.draw.rect(s, apron_color, (9, 20, 18, 18), border_radius=3)
#     # arms
#     pygame.draw.rect(s, body_color, (0, 20, 6, 16), border_radius=3)
#     pygame.draw.rect(s, body_color, (30, 20, 6, 16), border_radius=3)
#     # hands
#     pygame.draw.ellipse(s, skin_color, (0, 34, 8, 8))
#     pygame.draw.ellipse(s, skin_color, (28, 34, 8, 8))
#     # head
#     pygame.draw.ellipse(s, skin_color, (6, 2, 24, 20))
#     # hair
#     pygame.draw.ellipse(s, hair_color, (5, 1, 26, 12))
#     # eyes
#     if direction != "up":
#         pygame.draw.circle(s, (30, 30, 30), (13, 11), 2)
#         pygame.draw.circle(s, (30, 30, 30), (23, 11), 2)
#         # smile
#         pygame.draw.arc(s, (180, 80, 80), (11, 13, 14, 7), math.pi, 2 * math.pi, 2)

#     return s


# # ──────────────────────────────────────────────
# #  CUSTOMER
# # ──────────────────────────────────────────────
# _CUSTOMER_PALETTES = [
#     ((200, 80, 80),  (255, 210, 160), (150, 50, 50)),
#     ((80,  160, 80), (255, 220, 180), (50, 120, 50)),
#     ((80,  80,  200),(255, 200, 150), (50, 50, 150)),
#     ((200, 160, 80), (240, 200, 170), (150, 110, 40)),
#     ((160, 80,  200),(255, 215, 185), (100, 50, 160)),
# ]

# def make_customer_sprite(index=0):
#     s = _surf(CUSTOMER_W, CUSTOMER_H)
#     body, skin, dark = _CUSTOMER_PALETTES[index % len(_CUSTOMER_PALETTES)]

#     # legs
#     pygame.draw.rect(s, dark, (4, 30, 9, 20), border_radius=3)
#     pygame.draw.rect(s, dark, (17, 30, 9, 20), border_radius=3)
#     pygame.draw.ellipse(s, (20, 20, 20), (2, 46, 12, 6))
#     pygame.draw.ellipse(s, (20, 20, 20), (16, 46, 12, 6))
#     # body
#     pygame.draw.rect(s, body, (2, 14, 28, 20), border_radius=4)
#     # arms
#     pygame.draw.rect(s, body, (0, 16, 4, 14), border_radius=2)
#     pygame.draw.rect(s, body, (28, 16, 4, 14), border_radius=2)
#     pygame.draw.ellipse(s, skin, (0, 28, 6, 6))
#     pygame.draw.ellipse(s, skin, (26, 28, 6, 6))
#     # head
#     pygame.draw.ellipse(s, skin, (5, 1, 22, 18))
#     # hair
#     pygame.draw.ellipse(s, dark, (4, 0, 24, 10))
#     # eyes
#     pygame.draw.circle(s, (30, 30, 30), (11, 9), 2)
#     pygame.draw.circle(s, (30, 30, 30), (21, 9), 2)

#     return s


# # ──────────────────────────────────────────────
# #  BUBBLE TEA MACHINE
# # ──────────────────────────────────────────────
# def make_bubble_machine():
#     s = _surf(MACHINE_W, MACHINE_H)

#     # body
#     pygame.draw.rect(s, (60, 60, 80), (5, 20, 70, 70), border_radius=8)
#     # top funnel
#     pygame.draw.polygon(s, (90, 90, 120), [(20, 0), (60, 0), (65, 20), (15, 20)])
#     # screen / display
#     pygame.draw.rect(s, (30, 200, 200), (15, 30, 50, 25), border_radius=4)
#     pygame.draw.rect(s, (0, 240, 240), (18, 33, 44, 19), border_radius=3)
#     # bubbles on screen
#     for bx, by in [(26, 40), (36, 43), (46, 39), (56, 42)]:
#         pygame.draw.circle(s, (0, 80, 80), (bx, by), 4)
#     # button panel
#     pygame.draw.rect(s, (50, 50, 70), (10, 60, 60, 20), border_radius=4)
#     for bx in [20, 35, 55]:
#         pygame.draw.circle(s, PINK, (bx, 70), 5)
#     # nozzle
#     pygame.draw.rect(s, (40, 40, 60), (32, 80, 16, 10))
#     pygame.draw.ellipse(s, TEAL, (30, 87, 20, 8))
#     # label
#     font = pygame.font.SysFont("arial", 9, bold=True)
#     lbl = font.render("BOBA", True, WHITE)
#     s.blit(lbl, (22, 50))
#     return s


# # ──────────────────────────────────────────────
# #  FOOD MACHINE
# # ──────────────────────────────────────────────
# def make_food_machine():
#     s = _surf(MACHINE_W, MACHINE_H)

#     # body
#     pygame.draw.rect(s, (180, 80, 50), (5, 15, 70, 75), border_radius=8)
#     # top
#     pygame.draw.rect(s, (220, 110, 70), (5, 10, 70, 12), border_radius=4)
#     # glass window
#     pygame.draw.rect(s, (200, 230, 255, 160), (12, 22, 56, 40), border_radius=4)
#     pygame.draw.rect(s, (150, 200, 240, 80), (14, 24, 52, 36), border_radius=3)
#     # food items inside window
#     pygame.draw.ellipse(s, YELLOW,  (18, 32, 18, 12))   # sandwich
#     pygame.draw.ellipse(s, ORANGE,  (42, 28, 16, 14))   # burger
#     pygame.draw.rect(s,   BROWN,    (20, 44, 14, 10), border_radius=2)  # cookie
#     # dispenser slot
#     pygame.draw.rect(s, (100, 40, 20), (20, 80, 40, 8), border_radius=3)
#     # buttons
#     pygame.draw.rect(s, (80, 30, 10), (12, 64, 56, 14), border_radius=4)
#     for bx in [22, 35, 48, 60]:
#         pygame.draw.circle(s, YELLOW, (bx, 71), 4)
#     # label
#     font = pygame.font.SysFont("arial", 9, bold=True)
#     lbl = font.render("FOOD", True, WHITE)
#     s.blit(lbl, (25, 50))
#     return s


# # ──────────────────────────────────────────────
# #  DROPPER  (cash register / floor money spot)
# # ──────────────────────────────────────────────
# def make_dropper():
#     s = _surf(DROPPER_W, DROPPER_H)

#     # base
#     pygame.draw.rect(s, (40, 160, 60), (5, 30, 60, 35), border_radius=6)
#     # cash register body
#     pygame.draw.rect(s, (50, 50, 50), (8, 5, 54, 32), border_radius=5)
#     # screen
#     pygame.draw.rect(s, (30, 200, 80), (12, 9, 46, 18), border_radius=3)
#     # dollar sign on screen
#     font = pygame.font.SysFont("arial", 16, bold=True)
#     txt = font.render("$", True, (0, 80, 30))
#     s.blit(txt, (30, 10))
#     # buttons row
#     pygame.draw.rect(s, (30, 30, 30), (10, 29, 50, 6), border_radius=2)
#     for bx in [18, 28, 38, 50]:
#         pygame.draw.circle(s, (200, 200, 200), (bx, 32), 2)
#     # coin slot
#     pygame.draw.rect(s, (20, 20, 20), (22, 46, 26, 6), border_radius=2)
#     # glow ring (indicates active)
#     pygame.draw.ellipse(s, (60, 220, 80, 120), (2, 28, 66, 38))
#     return s


# # ──────────────────────────────────────────────
# #  BUBBLE TEA CUP  (item)
# # ──────────────────────────────────────────────
# def make_bubble_tea(color=None):
#     if color is None:
#         color = PINK
#     s = _surf(30, 40)
#     # cup body
#     pygame.draw.polygon(s, color, [(4, 8), (26, 8), (23, 36), (7, 36)])
#     # cup highlight
#     pygame.draw.polygon(s, (255, 255, 255, 80), [(6, 8), (12, 8), (10, 20)])
#     # lid
#     pygame.draw.ellipse(s, (200, 200, 200), (2, 4, 26, 8))
#     # straw
#     pygame.draw.rect(s, (255, 100, 150), (14, 0, 4, 20))
#     # bubbles
#     for bx, by in [(10, 28), (16, 25), (21, 28)]:
#         pygame.draw.circle(s, (80, 40, 20), (bx, by), 3)
#     return s


# # ──────────────────────────────────────────────
# #  FOOD ITEM
# # ──────────────────────────────────────────────
# def make_food_item(kind=0):
#     s = _surf(30, 30)
#     if kind == 0:   # sandwich
#         pygame.draw.rect(s, (220, 180, 80), (2, 8, 26, 14), border_radius=4)
#         pygame.draw.rect(s, (200, 80, 40),  (4, 12, 22, 5))
#         pygame.draw.rect(s, (80, 180, 60),  (4, 10, 22, 3))
#     elif kind == 1:  # burger
#         pygame.draw.ellipse(s, (220, 160, 60), (2, 4, 26, 14))
#         pygame.draw.rect(s,   (180, 90, 40),   (4, 13, 22, 8))
#         pygame.draw.ellipse(s, (200, 140, 50), (2, 18, 26, 10))
#     elif kind == 2:  # cookie
#         pygame.draw.circle(s, BROWN, (15, 15), 12)
#         for cx, cy in [(10, 10), (18, 14), (12, 19), (20, 10)]:
#             pygame.draw.circle(s, (60, 30, 10), (cx, cy), 2)
#     else:            # donut
#         pygame.draw.circle(s, (240, 160, 100), (15, 15), 12)
#         pygame.draw.circle(s, (255, 200, 220), (15, 15), 6)
#         pygame.draw.circle(s, (255, 255, 255, 0), (15, 15), 4)
#     return s


# # ──────────────────────────────────────────────
# #  COIN  (floating money pickup)
# # ──────────────────────────────────────────────
# def make_coin():
#     s = _surf(20, 20)
#     pygame.draw.circle(s, YELLOW, (10, 10), 9)
#     pygame.draw.circle(s, (200, 160, 0), (10, 10), 9, 2)
#     font = pygame.font.SysFont("arial", 10, bold=True)
#     t = font.render("$", True, (150, 100, 0))
#     s.blit(t, (6, 5))
#     return s


# # ──────────────────────────────────────────────
# #  BACKGROUND  (cafe interior)
# # ──────────────────────────────────────────────
# def make_background(w, h):
#     s = pygame.Surface((w, h))

#     # sky / wall gradient  (top area)
#     wall_h = FLOOR_Y
#     for y in range(wall_h):
#         t = y / wall_h
#         r = int(245 - t * 30)
#         g = int(230 - t * 20)
#         b = int(200 - t * 10)
#         pygame.draw.line(s, (r, g, b), (0, y), (w, y))

#     # window (left)
#     pygame.draw.rect(s, LIGHT_BLUE, (60, 60, 180, 130), border_radius=6)
#     pygame.draw.rect(s, SKY_BLUE,   (65, 65, 170, 120), border_radius=4)
#     pygame.draw.rect(s, WHITE,      (60, 60, 180, 130), 4, border_radius=6)
#     pygame.draw.line(s, WHITE, (150, 60), (150, 190), 3)
#     pygame.draw.line(s, WHITE, (60, 125), (240, 125), 3)
#     # clouds in window
#     for cx, cy, cr in [(90, 90, 18), (115, 85, 22), (140, 92, 16), (170, 88, 20)]:
#         pygame.draw.circle(s, (255, 255, 255, 200), (cx, cy), cr)

#     # window (right)
#     pygame.draw.rect(s, LIGHT_BLUE, (w - 240, 60, 180, 130), border_radius=6)
#     pygame.draw.rect(s, SKY_BLUE,   (w - 235, 65, 170, 120), border_radius=4)
#     pygame.draw.rect(s, WHITE,      (w - 240, 60, 180, 130), 4, border_radius=6)
#     pygame.draw.line(s, WHITE, (w - 150, 60), (w - 150, 190), 3)
#     pygame.draw.line(s, WHITE, (w - 240, 125), (w - 60, 125), 3)
#     for cx, cy, cr in [(w - 200, 90, 16), (w - 170, 82, 22), (w - 140, 90, 18)]:
#         pygame.draw.circle(s, (255, 255, 255, 200), (cx, cy), cr)

#     # wall decorations
#     font_big = pygame.font.SysFont("arial", 28, bold=True)
#     sign = font_big.render("🧋 Bubble Tea Cafe 🧋", True, (120, 60, 20))
#     s.blit(sign, (w // 2 - sign.get_width() // 2, 20))

#     # menu board
#     pygame.draw.rect(s, (60, 35, 15), (w // 2 - 140, 55, 280, 110), border_radius=8)
#     pygame.draw.rect(s, (30, 20, 5),  (w // 2 - 135, 60, 270, 100), border_radius=6)
#     mfont = pygame.font.SysFont("arial", 14, bold=True)
#     lines = ["☕ MENU", "🧋 Bubble Tea  $3", "🍔 Burger       $3-5", "🥪 Sandwich   $3-5", "🍪 Cookie       $3-5"]
#     for i, line in enumerate(lines):
#         col = YELLOW if i == 0 else (200, 230, 200)
#         txt = mfont.render(line, True, col)
#         s.blit(txt, (w // 2 - 120, 65 + i * 19))

#     # floor
#     for y in range(FLOOR_Y, h, TILE_SIZE):
#         for x in range(0, w, TILE_SIZE):
#             shade = (180, 140, 100) if (x // TILE_SIZE + y // TILE_SIZE) % 2 == 0 else (165, 125, 90)
#             pygame.draw.rect(s, shade, (x, y, TILE_SIZE, TILE_SIZE))
#             pygame.draw.rect(s, (140, 100, 65), (x, y, TILE_SIZE, TILE_SIZE), 1)

#     # floor-wall border
#     pygame.draw.rect(s, WOOD, (0, FLOOR_Y - 12, w, 14))
#     pygame.draw.rect(s, (100, 65, 30), (0, FLOOR_Y - 14, w, 4))

#     # counter / bar
#     pygame.draw.rect(s, WOOD, (0, FLOOR_Y, 300, 60))
#     pygame.draw.rect(s, (110, 70, 30), (0, FLOOR_Y, 300, 6))
#     pygame.draw.rect(s, (190, 140, 80), (0, FLOOR_Y + 6, 300, 54))

#     return s


# def make_rain_drop():
#     s = _surf(3, 12)
#     pygame.draw.line(s, (100, 150, 255, 180), (1, 0), (1, 11), 2)
#     return s


# def make_speech_bubble(text, font_size=14):
#     font = pygame.font.SysFont("arial", font_size)
#     txt  = font.render(text, True, (40, 40, 40))
#     w    = txt.get_width() + 20
#     h    = txt.get_height() + 14
#     s    = _surf(w + 10, h + 16)
#     pygame.draw.rect(s, WHITE,       (0, 0, w, h), border_radius=8)
#     pygame.draw.rect(s, DARK_GRAY,   (0, 0, w, h), 2, border_radius=8)
#     pygame.draw.polygon(s, WHITE,    [(w // 2 - 6, h), (w // 2 + 6, h), (w // 2, h + 10)])
#     pygame.draw.polygon(s, DARK_GRAY,[(w // 2 - 6, h - 1), (w // 2 + 6, h - 1), (w // 2, h + 9)], 2)
#     s.blit(txt, (10, 7))
#     return s

"""
asset_manager.py

Завантажує зображення з  game/assets/images/
Якщо файл відсутній — малює запасний варіант через pygame.draw (fallback),
щоб гра не падала навіть без картинок.

Зображення можуть бути БУДЬ-ЯКОГО розміру — вони автоматично
масштабуються до потрібних розмірів зі збереженням пропорцій.

────────────────────────────────────────────────
Список очікуваних файлів у  game/assets/images/
────────────────────────────────────────────────
  Машинки (будь-який розмір, краще квадрат):
    bubble_machine.png    → масштаб до 80 × 90
    food_machine.png      → масштаб до 80 × 90

  Напої (будь-який розмір):
    bubble_tea.png        → масштаб до 40 × 50
    bubble_tea_blue.png   → масштаб до 40 × 50
    bubble_tea_green.png  → масштаб до 40 × 50
    bubble_tea_purple.png → масштаб до 40 × 50

  Їжа (будь-який розмір):
    food_sandwich.png     → масштаб до 40 × 40
    food_burger.png       → масштаб до 40 × 40
    food_cookie.png       → масштаб до 40 × 40
    food_donut.png        → масштаб до 40 × 40

  Дропер / каса (будь-який розмір):
    dropper.png           → масштаб до 70 × 70

Підтримувані формати: PNG (рекомендовано, підтримує прозорість), JPG.
Де взяти безкоштовні спрайти:
  • https://kenney.nl/assets
  • https://opengameart.org
  • https://itch.io/game-assets/free
  • ChatGPT / DALL-E / Stable Diffusion (пікселарт на прозорому фоні)
────────────────────────────────────────────────
"""

import os
import math
import pygame
from game.constants import *

# ──────────────────────────────────────────────
# Шлях до папки із зображеннями
# ──────────────────────────────────────────────
_HERE       = os.path.dirname(os.path.abspath(__file__))
_IMAGES_DIR = os.path.join(_HERE, "assets", "images")

# Кеш завантажених поверхонь: { "filename@WxH" -> Surface }
_cache: dict[str, pygame.Surface] = {}


def _surf(w: int, h: int, alpha: bool = True) -> pygame.Surface:
    """Створити порожню Surface з прозорістю."""
    return pygame.Surface((w, h), pygame.SRCALPHA if alpha else 0)


def _scale_to_fit(img: pygame.Surface, target_w: int, target_h: int) -> pygame.Surface:
    """
    Масштабує зображення будь-якого розміру до target_w × target_h
    зі збереженням пропорцій + центруванням на прозорому тлі.

    Наприклад: зображення 512×512 → вмістити у 80×90 →
      реальний розмір після fit: 80×80, розміщено по центру 80×90 canvas.
    """
    src_w, src_h = img.get_size()
    if src_w == target_w and src_h == target_h:
        return img  # вже потрібний розмір

    # вирахувати масштаб зі збереженням пропорцій
    scale = min(target_w / src_w, target_h / src_h)
    fit_w = max(1, int(src_w * scale))
    fit_h = max(1, int(src_h * scale))

    scaled = pygame.transform.smoothscale(img, (fit_w, fit_h))

    # якщо пропорції збігаються точно — повернути одразу
    if fit_w == target_w and fit_h == target_h:
        return scaled

    # інакше — центрувати на прозорому canvas потрібного розміру
    canvas = pygame.Surface((target_w, target_h), pygame.SRCALPHA)
    canvas.fill((0, 0, 0, 0))
    offset_x = (target_w - fit_w) // 2
    offset_y = (target_h - fit_h) // 2
    canvas.blit(scaled, (offset_x, offset_y))
    return canvas


def _load(filename: str, size: tuple[int, int] | None = None) -> pygame.Surface | None:
    """
    Завантажує зображення з game/assets/images/<filename>.
    Підтримує PNG, JPG та будь-який інший формат, що розуміє pygame.
    Автоматично масштабує до size зі збереженням пропорцій.
    Повертає None якщо файл не знайдено.
    Результат кешується.
    """
    key = f"{filename}@{size}"
    if key in _cache:
        return _cache[key]

    # шукаємо файл — якщо розширення не вказано, пробуємо PNG і JPG
    base = os.path.join(_IMAGES_DIR, filename)
    candidates = [base]
    if not os.path.splitext(filename)[1]:
        candidates = [base + ".png", base + ".jpg", base + ".jpeg"]

    path = None
    for c in candidates:
        if os.path.isfile(c):
            path = c
            break

    if path is None:
        return None  # файл не знайдено — буде використано fallback

    try:
        img = pygame.image.load(path).convert_alpha()

        if size is not None:
            img = _scale_to_fit(img, size[0], size[1])

        _cache[key] = img
        print(f"[asset_manager] ✓ Завантажено: {os.path.basename(path)}"
              f"  {pygame.image.load(path).get_size()} → {img.get_size()}")
        return img

    except pygame.error as e:
        print(f"[asset_manager] ✗ Помилка завантаження '{path}': {e}")
        return None


# ══════════════════════════════════════════════
#  PLAYER  (малюється вручну — без файлу)
# ══════════════════════════════════════════════
def make_player_sprite(direction: str = "down") -> pygame.Surface:
    s = _surf(PLAYER_W, PLAYER_H)

    body_color  = (70, 130, 200)
    skin_color  = (255, 220, 180)
    apron_color = (255, 255, 255)
    hair_color  = (60, 40, 20)

    pygame.draw.rect(s, (40, 80, 160),  (6,  36, 10, 20), border_radius=3)
    pygame.draw.rect(s, (40, 80, 160),  (20, 36, 10, 20), border_radius=3)
    pygame.draw.ellipse(s, (30, 30, 30),(4,  52, 14,  6))
    pygame.draw.ellipse(s, (30, 30, 30),(18, 52, 14,  6))
    pygame.draw.rect(s, body_color,     (4,  18, 28, 22), border_radius=4)
    pygame.draw.rect(s, apron_color,    (9,  20, 18, 18), border_radius=3)
    pygame.draw.rect(s, body_color,     (0,  20,  6, 16), border_radius=3)
    pygame.draw.rect(s, body_color,     (30, 20,  6, 16), border_radius=3)
    pygame.draw.ellipse(s, skin_color,  (0,  34,  8,  8))
    pygame.draw.ellipse(s, skin_color,  (28, 34,  8,  8))
    pygame.draw.ellipse(s, skin_color,  (6,   2, 24, 20))
    pygame.draw.ellipse(s, hair_color,  (5,   1, 26, 12))
    if direction != "up":
        pygame.draw.circle(s, (30, 30, 30), (13, 11), 2)
        pygame.draw.circle(s, (30, 30, 30), (23, 11), 2)
        pygame.draw.arc(s, (180, 80, 80), (11, 13, 14, 7), math.pi, 2 * math.pi, 2)
    return s


# ══════════════════════════════════════════════
#  CUSTOMER  (малюється вручну — без файлу)
# ══════════════════════════════════════════════
_CUSTOMER_PALETTES = [
    ((200, 80, 80),  (255, 210, 160), (150, 50, 50)),
    ((80, 160, 80),  (255, 220, 180), (50, 120, 50)),
    ((80,  80, 200), (255, 200, 150), (50,  50, 150)),
    ((200, 160, 80), (240, 200, 170), (150, 110, 40)),
    ((160, 80, 200), (255, 215, 185), (100,  50, 160)),
]

def make_customer_sprite(index: int = 0) -> pygame.Surface:
    s = _surf(CUSTOMER_W, CUSTOMER_H)
    body, skin, dark = _CUSTOMER_PALETTES[index % len(_CUSTOMER_PALETTES)]

    pygame.draw.rect(s, dark,         (4,  30, 9, 20), border_radius=3)
    pygame.draw.rect(s, dark,         (17, 30, 9, 20), border_radius=3)
    pygame.draw.ellipse(s, (20,20,20),(2,  46, 12, 6))
    pygame.draw.ellipse(s, (20,20,20),(16, 46, 12, 6))
    pygame.draw.rect(s, body,         (2,  14, 28, 20), border_radius=4)
    pygame.draw.rect(s, body,         (0,  16,  4, 14), border_radius=2)
    pygame.draw.rect(s, body,         (28, 16,  4, 14), border_radius=2)
    pygame.draw.ellipse(s, skin,      (0,  28,  6, 6))
    pygame.draw.ellipse(s, skin,      (26, 28,  6, 6))
    pygame.draw.ellipse(s, skin,      (5,   1, 22, 18))
    pygame.draw.ellipse(s, dark,      (4,   0, 24, 10))
    pygame.draw.circle(s, (30,30,30), (11, 9), 2)
    pygame.draw.circle(s, (30,30,30), (21, 9), 2)
    return s


# ══════════════════════════════════════════════
#  BUBBLE TEA MACHINE
#  Файл: game/assets/images/bubble_machine.png
# ══════════════════════════════════════════════
def _fallback_bubble_machine() -> pygame.Surface:
    """Запасний варіант якщо bubble_machine.png відсутній."""
    s = _surf(MACHINE_W, MACHINE_H)
    pygame.draw.rect(s, (60, 60, 80),   (5, 20, 70, 70), border_radius=8)
    pygame.draw.polygon(s, (90, 90, 120), [(20,0),(60,0),(65,20),(15,20)])
    pygame.draw.rect(s, (30, 200, 200), (15, 30, 50, 25), border_radius=4)
    pygame.draw.rect(s, (0,  240, 240), (18, 33, 44, 19), border_radius=3)
    for bx, by in [(26,40),(36,43),(46,39),(56,42)]:
        pygame.draw.circle(s, (0, 80, 80), (bx, by), 4)
    pygame.draw.rect(s, (50, 50, 70),   (10, 60, 60, 20), border_radius=4)
    for bx in [20, 35, 55]:
        pygame.draw.circle(s, PINK, (bx, 70), 5)
    pygame.draw.rect(s, (40, 40, 60),   (32, 80, 16, 10))
    pygame.draw.ellipse(s, TEAL,        (30, 87, 20, 8))
    font = pygame.font.SysFont("arial", 9, bold=True)
    s.blit(font.render("BOBA", True, WHITE), (22, 50))
    return s

def make_bubble_machine() -> pygame.Surface:
    img = _load("bubble_machine.png", (MACHINE_W, MACHINE_H))
    return img if img is not None else _fallback_bubble_machine()


# ══════════════════════════════════════════════
#  FOOD MACHINE
#  Файл: game/assets/images/food_machine.png
# ══════════════════════════════════════════════
def _fallback_food_machine() -> pygame.Surface:
    s = _surf(MACHINE_W, MACHINE_H)
    pygame.draw.rect(s, (180, 80, 50),      (5, 15, 70, 75), border_radius=8)
    pygame.draw.rect(s, (220, 110, 70),     (5, 10, 70, 12), border_radius=4)
    pygame.draw.rect(s, (200, 230, 255, 160),(12, 22, 56, 40), border_radius=4)
    pygame.draw.ellipse(s, YELLOW,          (18, 32, 18, 12))
    pygame.draw.ellipse(s, ORANGE,          (42, 28, 16, 14))
    pygame.draw.rect(s,   BROWN,            (20, 44, 14, 10), border_radius=2)
    pygame.draw.rect(s, (100, 40, 20),      (20, 80, 40,  8), border_radius=3)
    pygame.draw.rect(s, (80,  30, 10),      (12, 64, 56, 14), border_radius=4)
    for bx in [22, 35, 48, 60]:
        pygame.draw.circle(s, YELLOW, (bx, 71), 4)
    font = pygame.font.SysFont("arial", 9, bold=True)
    s.blit(font.render("FOOD", True, WHITE), (25, 50))
    return s

def make_food_machine() -> pygame.Surface:
    img = _load("food_machine.png", (MACHINE_W, MACHINE_H))
    return img if img is not None else _fallback_food_machine()


# ══════════════════════════════════════════════
#  DROPPER  (каса / floor money spot)
#  Файл: game/assets/images/dropper.png
# ══════════════════════════════════════════════
def _fallback_dropper() -> pygame.Surface:
    s = _surf(DROPPER_W, DROPPER_H)
    pygame.draw.rect(s, (40, 160, 60),     (5, 30, 60, 35), border_radius=6)
    pygame.draw.rect(s, (50, 50, 50),      (8,  5, 54, 32), border_radius=5)
    pygame.draw.rect(s, (30, 200, 80),     (12,  9, 46, 18), border_radius=3)
    font = pygame.font.SysFont("arial", 16, bold=True)
    s.blit(font.render("$", True, (0,80,30)), (30, 10))
    pygame.draw.rect(s, (30, 30, 30),      (10, 29, 50,  6), border_radius=2)
    for bx in [18, 28, 38, 50]:
        pygame.draw.circle(s, (200,200,200), (bx, 32), 2)
    pygame.draw.rect(s, (20, 20, 20),      (22, 46, 26,  6), border_radius=2)
    pygame.draw.ellipse(s, (60, 220, 80, 120), (2, 28, 66, 38))
    return s

def make_dropper() -> pygame.Surface:
    img = _load("dropper.png", (DROPPER_W, DROPPER_H))
    return img if img is not None else _fallback_dropper()


# ══════════════════════════════════════════════
#  BUBBLE TEA CUP  (предмет інвентарю)
#  Файли: bubble_tea.png / bubble_tea_blue.png /
#          bubble_tea_green.png / bubble_tea_purple.png
# ══════════════════════════════════════════════

# Розмір іконки предмету
_ITEM_W, _ITEM_H = 40, 50

_BUBBLE_TEA_FILES = [
    "bubble_tea.png",
    "bubble_tea_blue.png",
    "bubble_tea_green.png",
    "bubble_tea_purple.png",
]
_BUBBLE_TEA_FALLBACK_COLORS = [
    PINK,
    (180, 220, 255),
    (180, 255, 180),
    PURPLE,
]

def _fallback_bubble_tea(color: tuple) -> pygame.Surface:
    s = _surf(_ITEM_W, _ITEM_H)
    # чашка
    pygame.draw.polygon(s, color, [(5,10),(35,10),(32,46),(8,46)])
    pygame.draw.polygon(s, (255,255,255,60), [(7,10),(14,10),(12,24)])
    pygame.draw.ellipse(s, (200,200,200), (3, 6, 34, 10))
    pygame.draw.rect(s, (255,100,150),   (17, 0,  5, 24))
    for bx, by in [(13,36),(20,32),(27,36)]:
        pygame.draw.circle(s, (80, 40, 20), (bx, by), 4)
    return s

def make_bubble_tea_surfaces() -> list[pygame.Surface]:
    """
    Повертає список із 4-х поверхонь для різних кольорів bubble tea.
    Спочатку намагається завантажити PNG, інакше малює fallback.
    """
    result = []
    for fname, color in zip(_BUBBLE_TEA_FILES, _BUBBLE_TEA_FALLBACK_COLORS):
        img = _load(fname, (_ITEM_W, _ITEM_H))
        result.append(img if img is not None else _fallback_bubble_tea(color))
    return result

# ── залишаємо make_bubble_tea для сумісності з іншим кодом ──
def make_bubble_tea(color=None) -> pygame.Surface:
    """Повертає одну іконку bubble tea (перший варіант із списку)."""
    surfs = make_bubble_tea_surfaces()
    return surfs[0]


# ══════════════════════════════════════════════
#  FOOD ITEMS  (предмети їжі)
#  Файли: food_sandwich.png / food_burger.png /
#          food_cookie.png / food_donut.png
# ══════════════════════════════════════════════

_FOOD_FILES = [
    "food_sandwich.png",
    "food_burger.png",
    "food_cookie.png",
    "food_donut.png",
]
_FOOD_SIZE = (40, 40)

def _fallback_food(kind: int) -> pygame.Surface:
    s = _surf(*_FOOD_SIZE)
    if kind == 0:   # бутерброд
        pygame.draw.rect(s, (220,180, 80), (2,10, 36, 18), border_radius=5)
        pygame.draw.rect(s, (200, 80, 40), (4,18, 32,  6))
        pygame.draw.rect(s, (80, 180, 60), (4,14, 32,  5))
    elif kind == 1:  # бургер
        pygame.draw.ellipse(s, (220,160, 60), (2, 4, 36, 18))
        pygame.draw.rect(s,   (180, 90, 40),  (4,18, 32, 10))
        pygame.draw.ellipse(s, (200,140, 50), (2,26, 36, 12))
    elif kind == 2:  # печиво
        pygame.draw.circle(s, BROWN, (20, 20), 16)
        for cx, cy in [(13,13),(23,18),(15,25),(27,13)]:
            pygame.draw.circle(s, (60,30,10), (cx,cy), 3)
    else:            # пончик
        pygame.draw.circle(s, (240,160,100), (20, 20), 16)
        pygame.draw.circle(s, (255,200,220), (20, 20),  8)
        pygame.draw.circle(s, (0,0,0,0),     (20, 20),  5)
    return s

def make_food_surfaces() -> list[pygame.Surface]:
    """
    Повертає список із 4-х поверхонь для різних видів їжі.
    Спочатку намагається завантажити PNG, інакше малює fallback.
    """
    result = []
    for i, fname in enumerate(_FOOD_FILES):
        img = _load(fname, _FOOD_SIZE)
        result.append(img if img is not None else _fallback_food(i))
    return result

# ── залишаємо make_food_item для сумісності з machine.py ──
def make_food_item(kind: int = 0) -> pygame.Surface:
    surfs = make_food_surfaces()
    return surfs[kind % len(surfs)]


# ══════════════════════════════════════════════
#  COIN  (анімована частинка грошей)
#  Малюється вручну — без файлу.
# ══════════════════════════════════════════════
def make_coin() -> pygame.Surface:
    s = _surf(20, 20)
    pygame.draw.circle(s, YELLOW,        (10, 10), 9)
    pygame.draw.circle(s, (200, 160,  0),(10, 10), 9, 2)
    font = pygame.font.SysFont("arial", 10, bold=True)
    s.blit(font.render("$", True, (150,100,0)), (6, 5))
    return s


# ══════════════════════════════════════════════
#  BACKGROUND  (інтер'єр кафе — малюється вручну)
# ══════════════════════════════════════════════
def make_background(w: int, h: int) -> pygame.Surface:
    s = pygame.Surface((w, h))

    wall_h = FLOOR_Y
    for y in range(wall_h):
        t = y / wall_h
        pygame.draw.line(s, (int(245 - t*30), int(230 - t*20), int(200 - t*10)), (0, y), (w, y))

    def _window(x, y, ww, wh):
        pygame.draw.rect(s, LIGHT_BLUE, (x, y, ww, wh), border_radius=6)
        pygame.draw.rect(s, SKY_BLUE,   (x+5, y+5, ww-10, wh-10), border_radius=4)
        pygame.draw.rect(s, WHITE,      (x, y, ww, wh), 4, border_radius=6)
        pygame.draw.line(s, WHITE, (x + ww//2, y), (x + ww//2, y + wh), 3)
        pygame.draw.line(s, WHITE, (x, y + wh//2), (x + ww, y + wh//2), 3)

    _window(60, 60, 180, 130)
    _window(w - 240, 60, 180, 130)

    font_big = pygame.font.SysFont("arial", 28, bold=True)
    sign = font_big.render("Bubble Tea Cafe", True, (120, 60, 20))
    s.blit(sign, (w//2 - sign.get_width()//2, 20))

    pygame.draw.rect(s, (60,35,15), (w//2-140, 55, 280, 110), border_radius=8)
    pygame.draw.rect(s, (30,20, 5), (w//2-135, 60, 270, 100), border_radius=6)
    mfont = pygame.font.SysFont("arial", 14, bold=True)
    for i, line in enumerate(["== MENU ==","Bubble Tea  $3","Burger      $3-5","Sandwich    $3-5","Cookie      $3-5"]):
        col = YELLOW if i == 0 else (200, 230, 200)
        s.blit(mfont.render(line, True, col), (w//2-120, 65 + i*19))

    for ty in range(FLOOR_Y, h, TILE_SIZE):
        for tx in range(0, w, TILE_SIZE):
            shade = (180,140,100) if (tx//TILE_SIZE + ty//TILE_SIZE) % 2 == 0 else (165,125,90)
            pygame.draw.rect(s, shade,       (tx, ty, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(s, (140,100,65),(tx, ty, TILE_SIZE, TILE_SIZE), 1)

    pygame.draw.rect(s, WOOD,         (0, FLOOR_Y-12, w, 14))
    pygame.draw.rect(s, (100,65,30),  (0, FLOOR_Y-14, w,  4))
    pygame.draw.rect(s, WOOD,         (0, FLOOR_Y,    300, 60))
    pygame.draw.rect(s, (110,70,30),  (0, FLOOR_Y,    300,  6))
    pygame.draw.rect(s, (190,140,80), (0, FLOOR_Y+6,  300, 54))

    return s


# ══════════════════════════════════════════════
#  RAIN DROP  (малюється вручну)
# ══════════════════════════════════════════════
def make_rain_drop() -> pygame.Surface:
    s = _surf(3, 12)
    pygame.draw.line(s, (100,150,255,180), (1,0), (1,11), 2)
    return s


# ══════════════════════════════════════════════
#  SPEECH BUBBLE  (малюється вручну)
# ══════════════════════════════════════════════
def make_speech_bubble(text: str, font_size: int = 14) -> pygame.Surface:
    font = pygame.font.SysFont("arial", font_size)
    txt  = font.render(text, True, (40,40,40))
    w    = txt.get_width()  + 20
    h    = txt.get_height() + 14
    s    = _surf(w+10, h+16)
    pygame.draw.rect(s, WHITE,     (0,0,w,h), border_radius=8)
    pygame.draw.rect(s, DARK_GRAY, (0,0,w,h), 2, border_radius=8)
    pygame.draw.polygon(s, WHITE,     [(w//2-6,h),(w//2+6,h),(w//2,h+10)])
    pygame.draw.polygon(s, DARK_GRAY, [(w//2-6,h-1),(w//2+6,h-1),(w//2,h+9)], 2)
    s.blit(txt, (10,7))
    return s