"""
🇨🇴 Colombia Pride Bot - Configuration
Simple and focused.
"""

import os
import discord
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ─── Discord Configuration ───────────────────────────────────────────────────

BOT_TOKEN: str = os.getenv("DISCORD_BOT_TOKEN", "")
CHANNEL_ID: int = int(os.getenv("DISCORD_CHANNEL_ID", "0"))

# ─── Colombian Flag Colors ───────────────────────────────────────────────────

EMBED_COLORS: list[discord.Color] = [
    discord.Color(0xFCD116),  # Yellow
    discord.Color(0x003893),  # Blue
    discord.Color(0xCE1126),  # Red
]

# ─── Messages ────────────────────────────────────────────────────────────────

MESSAGES: list[str] = [
    "Que viva Colombia!",
    "Yellow. Blue. Red.",
    "We export more than just coffee ;)",
    "Colombia needs no explanation.",
    "The tricolor still means something.",
    "From the Caribbean to the Amazon.",
]

# ─── Timing ──────────────────────────────────────────────────────────────────

MIN_GAP_MINUTES: int = 25
MAX_GAP_MINUTES: int = 40

# ─── Footer ──────────────────────────────────────────────────────────────────

FOOTER: str = "🇨🇴 Colombia"

# ─── Validation ──────────────────────────────────────────────────────────────

def validate_config() -> bool:
    """Validate required configuration."""
    if not BOT_TOKEN:
        print("❌ DISCORD_BOT_TOKEN is not set")
        return False
    if not CHANNEL_ID:
        print("❌ DISCORD_CHANNEL_ID is not set")
        return False
    return True
