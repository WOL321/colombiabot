"""
🇨🇴 Colombia Pride Bot - Configuration
"""

import os
import discord
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN: str = os.getenv("DISCORD_BOT_TOKEN", "")
CHANNEL_ID: int = int(os.getenv("DISCORD_CHANNEL_ID", "0"))

EMBED_COLORS: list[discord.Color] = [
    discord.Color(0xFCD116),
    discord.Color(0x003893),
    discord.Color(0xCE1126),
]

MESSAGES: list[dict] = [
    {
        "text": "Que viva Colombia!",
        "accent": "🇨🇴",
        "reactions": ["🇨🇴", "🎆", "💛", "💙", "❤️"],
    },
    {
        "text": "Yellow. Blue. Red.",
        "accent": "💛💙❤️",
        "reactions": ["💛", "💙", "❤️", "🇨🇴"],
    },
    {
        "text": "We export more than just coffee ;)",
        "accent": "☕",
        "reactions": ["☕", "✨", "🇨🇴", "💚"],
    },
    {
        "text": "Colombia needs no explanation.",
        "accent": "🏔️",
        "reactions": ["🏔️", "🌊", "🦜", "🇨🇴"],
    },
    {
        "text": "The tricolor still means something.",
        "accent": "🔥",
        "reactions": ["🇨🇴", "🔥", "💛", "💙", "❤️"],
    },
    {
        "text": "From the Caribbean to the Amazon.",
        "accent": "🌴",
        "reactions": ["🌴", "🌊", "🦜", "🇨🇴"],
    },
]

MIN_GAP_MINUTES: int = 25
MAX_GAP_MINUTES: int = 40
FOOTER: str = "🇨🇴 Colombia"

def validate_config() -> bool:
    if not BOT_TOKEN:
        print("❌ DISCORD_BOT_TOKEN is not set")
        return False
    if not CHANNEL_ID:
        print("❌ DISCORD_CHANNEL_ID is not set")
        return False
    return True
