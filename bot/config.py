"""
🇨🇴 Colombia Pride Bot - Configuration
All configurable settings in one clean place.
"""

import os
import discord
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ─── Discord Configuration ───────────────────────────────────────────────────

BOT_TOKEN: str = os.getenv("DISCORD_BOT_TOKEN", "")
CHANNEL_ID: int = int(os.getenv("DISCORD_CHANNEL_ID", "0"))

# ─── Colombian Flag Colors ───────────────────────────────────────────────────
# Official colors of the Colombian flag (Ley 12 de 1967)

EMBED_COLORS: list[discord.Color] = [
    discord.Color.from_hex("#FCD116"),  # Yellow - Sovereignty & Justice
    discord.Color.from_hex("#003893"),  # Blue - Loyalty & Perseverance
    discord.Color.from_hex("#CE1126"),  # Red - Valor & Blood of Heroes
]

# ─── Messages ────────────────────────────────────────────────────────────────

MESSAGES: list[str] = [
    "¡Viva Colombia!",
    "We export more than just coffee.",
    "Yellow. Blue. Red.",
]

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
