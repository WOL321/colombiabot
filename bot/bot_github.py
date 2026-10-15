"""
🇨🇴 Colombia Pride Bot - GitHub Actions Version
Sends ONE message and exits. Perfect for scheduled execution.
"""

import os
import sys
import random
import logging
from datetime import datetime

import discord
from discord.ext import commands

from config import (
    BOT_TOKEN,
    CHANNEL_ID,
    BASE_MESSAGES,
    EMOJI_VARIATIONS,
    HOLIDAY_MESSAGES,
    REACTION_EMOJIS,
    MIN_REACTIONS,
    MAX_REACTIONS,
    EMBED_COLORS,
    FOOTERS,
    HOLIDAY_FOOTERS,
    get_todays_holiday,
)

# Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger("colombia_bot_github")


def get_random_emoji_message(base_message: str) -> str:
    """Returns a random emoji variation of a base message."""
    variations = EMOJI_VARIATIONS.get(base_message, [base_message])
    return random.choice(variations)


def create_pride_embed(message: str, is_holiday: bool = False) -> discord.Embed:
    """Creates a beautiful embed with Colombian flag colors."""
    color = random.choice(EMBED_COLORS)
    footer = random.choice(HOLIDAY_FOOTERS if is_holiday else FOOTERS)

    embed = discord.Embed(
        description=message,
        color=color,
        timestamp=datetime.utcnow(),
    )
    embed.set_footer(text=footer)

    if color == discord.Color.from_hex("#FCD116"):
        embed.set_author(name="☀️ Golden Spirit")
    elif color == discord.Color.from_hex("#003893"):
        embed.set_author(name="🌊 Deep Blue Ocean")
    else:
        embed.set_author(name="🌹 Passionate Red")

    if is_holiday:
        embed.add_field(
            name="🎉",
            value="*Special Holiday Edition*",
            inline=False,
        )

    return embed


async def send_single_message():
    """Send one message with reactions and exit."""
    
    # Setup bot
    intents = discord.Intents.default()
    bot = commands.Bot(command_prefix="!", intents=intents)
    
    @bot.event
    async def on_ready():
        logger.info(f"🇨🇴 {bot.user.name} is online!")
        
        # Get channel
        channel = bot.get_channel(CHANNEL_ID)
        if not channel:
            try:
                channel = await bot.fetch_channel(CHANNEL_ID)
            except Exception as e:
                logger.error(f"Cannot access channel: {e}")
                await bot.close()
                return
        
        # Check for holiday
        holiday_key = get_todays_holiday()
        is_holiday = holiday_key is not None and holiday_key in HOLIDAY_MESSAGES
        
        # Get message
        if is_holiday:
            message = random.choice(HOLIDAY_MESSAGES[holiday_key])
            logger.info(f"🎉 HOLIDAY: {holiday_key}")
        else:
            base_message = random.choice(BASE_MESSAGES)
            message = get_random_emoji_message(base_message)
        
        # Create and send embed
        embed = create_pride_embed(message, is_holiday=is_holiday)
        
        try:
            sent_message = await channel.send(embed=embed)
            logger.info(f"✨ Sent: {message[:50]}...")
            
            # Add reactions
            num_reactions = random.randint(
                MIN_REACTIONS + (1 if is_holiday else 0),
                MAX_REACTIONS + (2 if is_holiday else 0)
            )
            reactions = ["🇨🇴"] if is_holiday else []
            available = [e for e in REACTION_EMOJIS if e not in reactions]
            reactions.extend(random.sample(
                available, 
                min(num_reactions - len(reactions), len(available))
            ))
            
            for emoji in reactions:
                try:
                    await sent_message.add_reaction(emoji)
                except:
                    pass
            
            logger.info(f"✅ Added {len(reactions)} reactions")
            
        except Exception as e:
            logger.error(f"❌ Failed to send: {e}")
        
        # Close bot
        await bot.close()
    
    # Run bot
    try:
        await bot.start(BOT_TOKEN)
    except Exception as e:
        logger.error(f"❌ Bot error: {e}")
        sys.exit(1)


def main():
    """Main entry point for GitHub Actions."""
    logger.info("🚀 Starting Colombia Pride Bot (GitHub Actions mode)")
    
    # Random decision: should we send a message this time?
    # Runs every 20 min, we want 25-40 min gaps, so ~60% chance to send
    should_send = random.random() < 0.60
    
    if not should_send:
        logger.info("⏸️  Skipping this run (natural timing simulation)")
        logger.info("💤 Bot will try again in 20 minutes")
        return
    
    logger.info("✨ Sending a message this run!")
    
    import asyncio
    asyncio.run(send_single_message())
    
    logger.info("✅ Done! Bot will run again at next scheduled time.")


if __name__ == "__main__":
    main()
