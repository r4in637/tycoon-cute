# 🧋 Bubble Tea Tycoon

A 2D tycoon game built with **Python + Pygame** using OOP.

## Setup

```bash
pip install pygame
python main.py
```

## Controls

| Key | Action |
|-----|--------|
| WASD / Arrow Keys | Move the seller |
| E / Space | Pick up item from machine  OR  collect dropper bonus |
| F | Sell item to nearest waiting customer |

## Gameplay

1. Walk to a **Machine** (left side counter) and press **E** to pick up Bubble Tea 🧋 or Food 🍔.
2. Walk to a **Customer** (waiting on the right side) and press **F** to sell them what they want.
3. Step on **Droppers** (green cash registers) to collect bonus money every few seconds.
4. Watch the **weather** change — it rains occasionally!
5. Earn as much money as possible!

## File Structure

```
bubble_tea_tycoon/
├── main.py                  # Entry point
├── requirements.txt
├── assets/
│   ├── images/              # (reserved for future sprites)
│   ├── sounds/              # (reserved for future sounds)
│   └── fonts/               # (reserved for future fonts)
└── game/
    ├── __init__.py
    ├── constants.py         # All magic numbers & colors
    ├── asset_manager.py     # Programmatic sprite generation
    ├── player.py            # Player class
    ├── machine.py           # Machine class
    ├── dropper.py           # Dropper class
    ├── customer.py          # Customer NPC class
    ├── weather.py           # WeatherSystem class
    ├── hud.py               # HUD class
    └── game.py              # Main Game controller class
```

## OOP Classes

| Class | File | Role |
|-------|------|------|
| `Player` | player.py | Seller controlled by keyboard |
| `Machine` | machine.py | Produces bubble tea / food |
| `Dropper` | dropper.py | Floor cash register for bonus money |
| `Customer` | customer.py | NPC that walks in, waits, and buys |
| `WeatherSystem` | weather.py | Manages clear/rain transitions |
| `HUD` | hud.py | On-screen UI elements |
| `Game` | game.py | Top-level controller |
