"""
🇨🇴 Colombia Pride Bot - Configuration
"""

import os
import discord
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN: str = os.getenv("DISCORD_BOT_TOKEN", "")
CHANNEL_ID: int = int(os.getenv("DISCORD_CHANNEL_ID", "0"))
POLL_CHANNEL_ID: int = int(os.getenv("DISCORD_POLL_CHANNEL_ID", "0"))

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

POLL_QUESTIONS: list[str] = [
    # Food
    "Are arepas better than empanadas?",
    "Is bandeja paisa the ultimate comfort food?",
    "Does Colombian coffee beat all other coffee?",
    "Is ajiaco the best soup ever?",
    "Should you put sugar in Colombian coffee?",
    "Is sancocho better on weekends?",
    "Are Colombian empanadas superior to Argentine ones?",
    "Is lulada the best drink ever?",
    "Does chocolate with cheese actually slap?",
    "Is colombian breakfast > american breakfast?",
    
    # Music & Culture
    "Is Shakira the greatest Colombian ever?",
    "Is vallenato the best Colombian music genre?",
    "Does Karol G represent Colombia well?",
    "Is cumbia the heartbeat of Colombia?",
    "Would you go to the Barranquilla Carnival?",
    "Is salsa caleña better than Cuban salsa?",
    "Does J Balvin represent reggaeton well?",
    "Is champeta underrated?",
    "Would you learn to dance salsa?",
    "Is Colombian music diverse enough?",
    
    # Cities & Travel
    "Is Medellín the best city in Colombia?",
    "Would you live in Bogotá?",
    "Is Cartagena overrated?",
    "Is Cali the salsa capital?",
    "Would you visit the Amazon in Colombia?",
    "Is San Andrés the best beach destination?",
    "Would you hike the Lost City trek?",
    "Is Bogotá's food scene underrated?",
    "Would you move to Colombia if you could?",
    "Is the Coffee Triangle worth visiting?",
    
    # Hot Takes
    "Is Colombia the most biodiverse country per km²?",
    "Do Colombians have the best Spanish accent?",
    "Is Colombian street food underrated?",
    "Are Colombians the friendliest people?",
    "Is Colombia safer than people think?",
    "Does Colombia get enough global recognition?",
    "Is the Colombian peso undervalued?",
    "Are Colombian flowers the best in the world?",
    "Is Colombia's biodiversity unmatched?",
    "Do Colombians work harder than most?",
    
    # Fun & Random
    "Would you try cuy (guinea pig)?",
    "Is panela the best sweetener?",
    "Would you wear a ruana?",
    "Is aguardiente better than rum?",
    "Would you live on the Caribbean coast?",
    "Is the Colombian national anthem fire?",
    "Would you try lulo juice?",
    "Is Colombian rum underrated?",
    "Would you visit Guatapé?",
    "Is Colombia's internet getting better?",
    
    # Culture & Identity
    "Is Colombian pride justified?",
    "Does Colombia represent Latin America well?",
    "Is the Colombian flag iconic?",
    "Are Colombian traditions worth preserving?",
    "Is Colombian Spanish the clearest?",
    "Does Colombia have the best biodiversity?",
    "Is Colombian culture diverse enough?",
    "Are Colombian values strong?",
    "Is Colombia's future bright?",
    "Does Colombia inspire you?",
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
