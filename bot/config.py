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

# ─── Messages with Emoji Styles ──────────────────────────────────────────────

MESSAGES: list[dict] = [
    {
        "text": "Que viva Colombia!",
        "emoji": "🎆🇨🇴🎆",
        "author": "no thoughts just colombia",
        "reactions": ["🇨🇴", "🎆", "💛", "💙", "❤️"],
    },
    {
        "text": "Yellow. Blue. Red.",
        "emoji": "💛💙❤️",
        "author": "the colors hit different",
        "reactions": ["💛", "💙", "❤️", "🇨🇴", "✨"],
    },
    {
        "text": "We export more than just coffee ;)",
        "emoji": "☕✨🌎",
        "author": "yes we're that country",
        "reactions": ["☕", "✨", "🌎", "💚", "🇨🇴"],
    },
    {
        "text": "Colombia needs no explanation.",
        "emoji": "🏔️🌊🦜",
        "author": "if you know you know",
        "reactions": ["🏔️", "🌊", "🦜", "🇨🇴", "💎"],
    },
    {
        "text": "The tricolor still means something.",
        "emoji": "🇨🇴🔥🇨🇴",
        "author": "real talk",
        "reactions": ["🇨🇴", "🔥", "💛", "💙", "❤️"],
    },
    {
        "text": "From the Caribbean to the Amazon.",
        "emoji": "🌴🌳🌊",
        "author": "try explaining this place",
        "reactions": ["🌴", "🌳", "🌊", "🦜", "🇨🇴"],
    },
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
