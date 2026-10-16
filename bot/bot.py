"""
🇨🇴 Colombia Pride Bot
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
    POLL_CHANNEL_ID,
    MESSAGES,
    POLL_QUESTIONS,
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
    """Creates a clean embed with Colombian flag colors."""
    color = random.choice(EMBED_COLORS)
    accent = message_data["accent"]
    text = message_data["text"]
    
    embed = discord.Embed(
        description=f"{accent} {text}",
        color=color,
        timestamp=datetime.utcnow(),
    )
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


async def send_poll():
    """Send a yes/no poll to the poll channel."""
    if not POLL_CHANNEL_ID:
        logger.info("⏭️ No poll channel configured, skipping poll")
        return
    
    poll_channel = bot.get_channel(POLL_CHANNEL_ID)
    if not poll_channel:
        try:
            poll_channel = await bot.fetch_channel(POLL_CHANNEL_ID)
        except Exception as e:
            logger.error(f"Cannot access poll channel: {e}")
            return
    
    question = random.choice(POLL_QUESTIONS)
    
    embed = discord.Embed(
        description=f"🤔 **{question}**",
        color=random.choice(EMBED_COLORS),
        timestamp=datetime.utcnow(),
    )
    embed.set_footer(text=FOOTER)
    
    try:
        poll_message = await poll_channel.send(embed=embed)
        await poll_message.add_reaction("✅")
        await asyncio.sleep(0.5)
        await poll_message.add_reaction("❌")
        logger.info(f"📊 Sent poll: {question}")
    except Exception as e:
        logger.error(f"❌ Failed to send poll: {e}")


# ─── Core Messaging Loop ─────────────────────────────────────────────────────

async def send_cycle_messages():
    """Main cycle loop - sends messages or polls with natural timing."""
    channel = bot.get_channel(CHANNEL_ID)
    
    if not channel:
        try:
            channel = await bot.fetch_channel(CHANNEL_ID)
        except Exception as e:
            logger.error(f"Cannot access channel: {e}")
            return

    messages_this_cycle = random.randint(7, 12)
    logger.info(f"🇨🇴 Starting cycle ({messages_this_cycle} messages)")

    for i in range(messages_this_cycle):
        # 70% chance to send pride message, 30% chance to send poll
        if POLL_CHANNEL_ID and random.random() < 0.3:
            await send_poll()
        else:
            # Get random message with its style
            message_data = random.choice(MESSAGES)
            embed = create_embed(message_data)

            try:
                sent_message = await channel.send(embed=embed)
                global messages_sent
                messages_sent += 1
                logger.info(f"✨ Sent: {message_data['text']}")

                # Add themed reactions
                await add_reactions(sent_message, message_data["reactions"])

            except Exception as e:
                logger.error(f"❌ Failed to send: {e}")

        # Wait before next message (unless it's the last one)
        if i < messages_this_cycle - 1:
            delay = random.uniform(MIN_GAP_MINUTES, MAX_GAP_MINUTES) * 60
            delay += random.uniform(-2, 2) * 60  # Add jitter
            delay = max(MIN_GAP_MINUTES * 60, delay)
            delay_minutes = round(delay / 60, 1)
            logger.info(f"⏳ Next message in {delay_minutes} minutes")
            await asyncio.sleep(delay)

    logger.info(f"✅ Cycle complete! Total messages: {messages_sent}")
    logger.info("🔄 Starting new cycle in 30 seconds...")
    await asyncio.sleep(30)
    await send_cycle_messages()


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

    # Start the messaging cycle
    bot.loop.create_task(send_cycle_messages())


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
