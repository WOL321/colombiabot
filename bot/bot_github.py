"""
🇨🇴 Colombia Pride Bot - GitHub Actions Version
Simple, focused, elegant.
"""

import os
import sys
import random
import asyncio
import logging
from datetime import datetime

import discord
from discord.ext import commands

from config import (
    BOT_TOKEN,
    CHANNEL_ID,
    MESSAGES,
    EMBED_COLORS,
    MIN_GAP_MINUTES,
    MAX_GAP_MINUTES,
    FOOTER,
)

# Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger("colombia_bot")

# ─── Bot Setup ───────────────────────────────────────────────────────────────

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents,
    description="🇨🇴 Celebrating Colombia with pride",
    help_command=None,
)

# Track stats
messages_sent = 0


# ─── Embed Builder ───────────────────────────────────────────────────────────

def create_embed(message_data: dict) -> discord.Embed:
    """Creates a beautiful, premium embed with Colombian flag colors."""
    color = random.choice(EMBED_COLORS)
    
    # Format message with emoji decoration
    emoji = message_data["emoji"]
    text = message_data["text"]
    author = message_data["author"]
    
    # Create the full message with emojis
    full_message = f"{emoji}\n**{text}**\n{emoji}"
    
    embed = discord.Embed(
        description=full_message,
        color=color,
        timestamp=datetime.utcnow(),
    )
    
    # Add themed author
    embed.set_author(name=author)
    
    # Add footer
    embed.set_footer(text=FOOTER)
    
    return embed


async def add_reactions(message: discord.Message, reactions: list):
    """Adds themed emoji reactions to a sent message."""
    # Pick 3-5 reactions from the message's reaction pool
    num_reactions = random.randint(3, 5)
    selected = random.sample(reactions, min(num_reactions, len(reactions)))
    
    for emoji in selected:
        try:
            await message.add_reaction(emoji)
            await asyncio.sleep(random.uniform(0.5, 1.5))
        except discord.HTTPException:
            continue
        except discord.Forbidden:
            logger.warning("Missing permission to add reactions")
            break


async def send_message():
    """Send one message with reactions."""
    global messages_sent
    
    channel = bot.get_channel(CHANNEL_ID)
    if not channel:
        try:
            channel = await bot.fetch_channel(CHANNEL_ID)
        except Exception as e:
            logger.error(f"Cannot access channel: {e}")
            return

    # Get random message with its style
    message_data = random.choice(MESSAGES)
    
    # Create and send embed
    embed = create_embed(message_data)

    try:
        sent_message = await channel.send(embed=embed)
        messages_sent += 1
        logger.info(f"✨ Sent: {message_data['text']}")

        # Add themed reactions
        await add_reactions(sent_message, message_data["reactions"])
        logger.info(f"✅ Added reactions")

    except Exception as e:
        logger.error(f"❌ Failed to send: {e}")


# ─── Commands ────────────────────────────────────────────────────────────────

@bot.command(name="ping", aliases=["status"])
async def ping(ctx):
    """Check if the bot is online."""
    latency = round(bot.latency * 1000)
    
    embed = discord.Embed(
        title="🇨🇴 Colombia Pride Bot",
        description="¡Estoy vivo!",
        color=random.choice(EMBED_COLORS),
        timestamp=datetime.utcnow(),
    )
    embed.add_field(name="⚡ Latency", value=f"{latency}ms", inline=True)
    embed.add_field(name="📊 Messages", value=str(messages_sent), inline=True)
    embed.set_footer(text=FOOTER)
    await ctx.send(embed=embed)


# ─── Bot Events ──────────────────────────────────────────────────────────────

@bot.event
async def on_ready():
    """Called when bot connects to Discord."""
    logger.info(f"🇨🇴 {bot.user.name} is online!")

    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="over Colombia 🇨🇴",
        ),
        status=discord.Status.online,
    )

    # Send a message (80% chance)
    if random.random() < 0.80:
        await asyncio.sleep(random.uniform(3, 10))
        await send_message()
    else:
        logger.info("💤 Skipping message this session")

    # Stay online for 2 minutes
    logger.info("👂 Listening for commands for 2 minutes...")
    await asyncio.sleep(120)

    logger.info("👋 Session ending...")
    await bot.close()


@bot.event
async def on_command_error(ctx, error):
    """Global error handler."""
    if isinstance(error, commands.CommandNotFound):
        return
    logger.error(f"Command error: {error}")


# ─── Entry Point ─────────────────────────────────────────────────────────────

def main():
    """Main entry point."""
    logger.info("🚀 Starting Colombia Pride Bot")

    try:
        bot.run(BOT_TOKEN)
    except Exception as e:
        logger.error(f"❌ Bot error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
