"""
🇨🇴 Colombia Pride Bot - Configuration
All configurable settings in one clean place.
"""

import os
import discord
from dotenv import load_dotenv
from datetime import date

# Load environment variables from .env file
load_dotenv()

# ─── Discord Configuration ───────────────────────────────────────────────────

BOT_TOKEN: str = os.getenv("DISCORD_BOT_TOKEN", "")
CHANNEL_ID: int = int(os.getenv("DISCORD_CHANNEL_ID", "0"))

# ─── Colombian Flag Colors ───────────────────────────────────────────────────
# Official colors of the Colombian flag (Ley 12 de 1967)
# Using integer constructor for cross-version compatibility

EMBED_COLORS: list[discord.Color] = [
    discord.Color(0xFCD116),  # Yellow - Sovereignty & Justice
    discord.Color(0x003893),  # Blue - Loyalty & Perseverance
    discord.Color(0xCE1126),  # Red - Valor & Blood of Heroes
]

# ─── Base Messages ───────────────────────────────────────────────────────────

BASE_MESSAGES: list[str] = [
    "¡Viva Colombia!",
    "We export more than just coffee.",
    "Yellow. Blue. Red.",
]

# ─── Emoji Variations ────────────────────────────────────────────────────────
# Each message gets a random emoji combo to keep things fresh

EMOJI_VARIATIONS: dict[str, list[str]] = {
    "¡Viva Colombia!": [
        "🇨🇴 ¡Viva Colombia! 🇨🇴",
        "🎉 ¡Viva Colombia! 🎊",
        "🇨🇴✨ ¡Viva Colombia! ✨🇨🇴",
        "💛💙❤️ ¡Viva Colombia! 💛💙❤️",
        "🌟 ¡Viva Colombia! 🌟",
        "🇨🇴🎆 ¡Viva Colombia! 🎆🇨🇴",
        "🏔️ ¡Viva Colombia! ☕",
        "🦜 ¡Viva Colombia! 🌺",
    ],
    "We export more than just coffee.": [
        "☕ We export more than just coffee. 🌎",
        "🌱 We export more than just coffee. 💚",
        "☕✨ We export more than just coffee. ✨",
        "🌍 We export more than just coffee. ☕",
        "💎 We export more than just coffee. 💛",
        "🌺 We export more than just coffee. 🌿",
        "☕🇨🇴 We export more than just coffee. 🇨🇴",
        "🏆 We export more than just coffee. ☕",
    ],
    "Yellow. Blue. Red.": [
        "💛 Yellow. 💙 Blue. ❤️ Red.",
        "🟡 Yellow. 🔵 Blue. 🔴 Red.",
        "💛💙❤️ Yellow. Blue. Red. 🇨🇴",
        "✨ Yellow. Blue. Red. ✨",
        "🌟 Yellow. 💎 Blue. 🔥 Red.",
        "🇨🇴 Yellow. Blue. Red. 🇨🇴",
        "☀️ Yellow. 🌊 Blue. 🌹 Red.",
        "💫 Yellow. Blue. Red. 💫",
    ],
}

# ─── Holiday Messages ────────────────────────────────────────────────────────
# Special messages for Colombian holidays

HOLIDAY_MESSAGES: dict[str, list[str]] = {
    "new_year": [
        "🎆🇨🇴 ¡Feliz Año Nuevo, Colombia! 🇨🇴🎆",
        "✨ New year, same pride. ¡Viva Colombia! 🇨🇴",
        "🎊 Starting the year with Colombian spirit! 💛💙❤️",
    ],
    "independence_day": [
        "🇨🇴🎆 ¡200+ años de libertad! ¡Viva Colombia! 🎆🇨🇴",
        "🎉 ¡Feliz Día de la Independencia! We are proud, we are free! 🇨🇴",
        "💛💙❤️ 20 de Julio — The day Colombia said YES to freedom! 🇨🇴✨",
        "🏔️ From the Andes to the Caribbean — ¡Viva la Independencia! 🌊",
    ],
    "battle_of_boyaca": [
        "⚔️🇨🇴 ¡7 de Agosto! The battle that sealed our freedom! 🇨🇴",
        "🏆 Boyacá — Where heroes were born. ¡Viva Colombia! ⚔️",
    ],
    "day_of_love_friendship": [
        "💛💙❤️ Día del Amor y la Amistad — Colombia sends love to the world! 🌍",
        "🌹 From Colombia with love. ¡Feliz día! 💕",
    ],
    "candelaria": [
        "🕯️✨ ¡Día de las Velitas! Colombia lights up the night! 🌟",
        "🕯️ Millions of candles, one proud nation. ¡Viva Colombia! 🇨🇴",
    ],
    "labor_day": [
        "💪🇨🇴 ¡Día del Trabajo! Honoring Colombian workers worldwide. 🌟",
        "☕🌱 From coffee farms to cities — thank you, Colombia! 💛",
    ],
    "race_day": [
        "🌎🇨🇴 Día de la Raza — Celebrating our rich heritage! 🏔️",
        "✨ Many roots, one nation. ¡Viva la diversidad colombiana! 🌺",
    ],
    "cartagena_independence": [
        "🏰🌊 ¡11 de Noviembre! Cartagena said YES to freedom! 🇨🇴",
        "🎉 The Heroic City celebrates! ¡Viva Cartagena, viva Colombia! 🏰",
    ],
    "immaculate_conception": [
        "⭐🇨🇴 Día de la Inmaculada — A day of light and tradition. 🕊️",
        "✨ December 8 — Colombia celebrates with faith and pride. 🙏",
    ],
    "christmas": [
        "🎄🇨🇴 ¡Feliz Navidad desde Colombia! 🎁💛💙❤️",
        "🌟 Merry Christmas! Colombia sends warmth to the world. 🎄✨",
    ],
}

# ─── Colombian Holidays Calendar ─────────────────────────────────────────────
# (month, day) -> holiday key

COLOMBIAN_HOLIDAYS: dict[tuple[int, int], str] = {
    (1, 1): "new_year",
    (1, 6): "epiphany",
    (3, 19): "saint_joseph",
    (5, 1): "labor_day",
    (6, 29): "saints_peter_paul",
    (7, 20): "independence_day",
    (8, 7): "battle_of_boyaca",
    (9, 20): "spring_day",
    (10, 12): "race_day",
    (11, 1): "all_saints",
    (11, 11): "cartagena_independence",
    (12, 7): "candelaria",
    (12, 8): "immaculate_conception",
    (12, 25): "christmas",
    (12, 31): "new_year_eve",
}

# ─── Reaction Emojis ─────────────────────────────────────────────────────────
# Emojis the bot reacts with after sending each message

REACTION_EMOJIS: list[str] = [
    "🇨🇴",  # Colombian flag
    "💛",    # Yellow heart
    "💙",    # Blue heart
    "❤️",    # Red heart
    "☕",    # Coffee
    "🌺",    # Flower
    "🎉",    # Party
    "✨",    # Sparkles
    "🌟",    # Star
    "🏔️",    # Mountain (Andes)
    "🦜",    # Parrot (Colombian wildlife)
    "🌊",    # Ocean (Caribbean/Pacific)
]

# How many reactions to add per message (random range)
MIN_REACTIONS: int = 3
MAX_REACTIONS: int = 5

# ─── Messages (Combined) ─────────────────────────────────────────────────────

MESSAGES: list[str] = BASE_MESSAGES

# ─── Timing Configuration ────────────────────────────────────────────────────

CYCLE_DURATION_HOURS: int = 5
MIN_GAP_MINUTES: int = 25
MAX_GAP_MINUTES: int = 40

# ─── Footer Messages ─────────────────────────────────────────────────────────

FOOTERS: list[str] = [
    "🇨🇴 República de Colombia",
    "🇨🇴 Orgullo Colombiano",
    "🇨🇴 Hecho con amor en Colombia",
    "🇨🇴 Tierra de mil colores",
    "🇨🇴 El riesgo es que te quieras quedar",
    "🇨🇴 Desde las montañas hasta el mar",
    "🇨🇴 Biodiversidad que enamora",
    "🇨🇴 Sabor, ritmo y corazón",
]

# ─── Holiday Footer Messages ─────────────────────────────────────────────────

HOLIDAY_FOOTERS: list[str] = [
    "🇨🇴 ¡Celebrando con orgullo!",
    "🇨🇴✨ Día especial para Colombia",
    "🎉🇨🇴 ¡Que viva la fiesta!",
    "🇨🇴🎊 Celebración colombiana",
]

# ─── Validation ──────────────────────────────────────────────────────────────

def validate_config() -> bool:
    """Validate that all required configuration is present."""
    errors = []

    if not BOT_TOKEN:
        errors.append("DISCORD_BOT_TOKEN is not set")

    if not CHANNEL_ID or CHANNEL_ID == 0:
        errors.append("DISCORD_CHANNEL_ID is not set")

    if errors:
        for error in errors:
            print(f"❌ Configuration Error: {error}")
        print("\n📝 Please check your .env file. See .env.example for reference.")
        return False

    return True


def get_todays_holiday() -> str | None:
    """Check if today is a Colombian holiday."""
    today = date.today()
    return COLOMBIAN_HOLIDAYS.get((today.month, today.day))
