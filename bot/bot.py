"""
🇨🇴 Colombia Pride Bot
A beautiful Discord bot that celebrates Colombia with style.
Posts elegant embeds with Colombian pride messages at natural intervals.
"""

import os
import sys
import random
import asyncio
import logging
from datetime import datetime, timedelta

import discord
from discord.ext import commands, tasks

from config import (
    BOT_TOKEN,
    CHANNEL_ID,
    MESSAGES,
    EMBED_COLORS,
    CYCLE_DURATION_HOURS,
    MIN_GAP_MINUTES,
    MAX_GAP_MINUTES,
    FOOTERS,
)

# ─── Logging Setup ───────────────────────────────────────────────────────────

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("colombia_bot")

# ─── Bot Setup ───────────────────────────────────────────────────────────────

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents,
    description="🇨🇴 Celebrating Colombia with pride and elegance",
)


# ─── Embed Builder ───────────────────────────────────────────────────────────

def create_pride_embed(message: str) -> discord.Embed:
    """
    Creates a beautiful, premium embed with Colombian flag colors.
    Randomly selects color and footer for variety.
    """
    color = random.choice(EMBED_COLORS)
    footer = random.choice(FOOTERS)

    embed = discord.Embed(
        description=message,
        color=color,
        timestamp=datetime.utcnow(),
    )

    embed.set_footer(text=footer)

    # Add subtle decorative elements based on color
    if color == discord.Color.from_hex("#FCD116"):
        embed.set_author(name="☀️ Golden Spirit")
    elif color == discord.Color.from_hex("#003893"):
        embed.set_author(name="🌊 Deep Blue Ocean")
    else:
        embed.set_author(name="🌹 Passionate Red")

    return embed


# ─── Core Messaging Loop ─────────────────────────────────────────────────────

class ColombiaCycle:
    """
    Manages the rolling 5-hour cycle with natural, unpredictable timing.
    Each cycle sends messages at random intervals (25-40 min gap).
    """

    def __init__(self):
        self.cycle_count = 0
        self.messages_sent = 0
        self.is_running = False

    def get_next_delay(self) -> float:
        """
        Returns a natural-feeling delay in seconds.
        Uses a weighted random to avoid robotic patterns.
        """
        base_minutes = random.uniform(MIN_GAP_MINUTES, MAX_GAP_MINUTES)

        # Add slight organic jitter (±2 minutes)
        jitter = random.uniform(-2, 2)
        delay_minutes = max(MIN_GAP_MINUTES, base_minutes + jitter)

        return delay_minutes * 60

    def get_messages_for_cycle(self) -> list:
        """
        Determines how many messages to send in this cycle.
        With 25-40 min gaps over 5 hours, we get ~7-12 messages.
        """
        return random.randint(7, 12)


cycle_manager = ColombiaCycle()


async def send_cycle_messages():
    """
    Main cycle loop - sends messages for one 5-hour cycle,
    then restarts automatically.
    """
    channel = bot.get_channel(CHANNEL_ID)

    if channel is None:
        try:
            channel = await bot.fetch_channel(CHANNEL_ID)
        except (discord.NotFound, discord.Forbidden) as e:
            logger.error(f"Cannot access channel {CHANNEL_ID}: {e}")
            return

    if not isinstance(channel, discord.TextChannel):
        logger.error(f"Channel {CHANNEL_ID} is not a text channel")
        return

    cycle_manager.cycle_count += 1
    cycle_manager.is_running = True
    messages_this_cycle = cycle_manager.get_messages_for_cycle()

    logger.info(
        f"🇨🇴 Starting cycle #{cycle_manager.cycle_count} "
        f"({messages_this_cycle} messages planned)"
    )

    for i in range(messages_this_cycle):
        if not cycle_manager.is_running:
            break

        # Select a random message
        message = random.choice(MESSAGES)
        embed = create_pride_embed(message)

        try:
            await channel.send(embed=embed)
            cycle_manager.messages_sent += 1
            logger.info(
                f"  ✨ Sent message {i + 1}/{messages_this_cycle}: "
                f'"{message}"'
            )
        except discord.HTTPException as e:
            logger.error(f"  ❌ Failed to send message: {e}")
        except discord.Forbidden:
            logger.error(
                f"  ❌ Missing permissions to send messages in channel {CHANNEL_ID}"
            )
            return

        # Wait before next message (unless it's the last one)
        if i < messages_this_cycle - 1:
            delay = cycle_manager.get_next_delay()
            delay_minutes = round(delay / 60, 1)
            logger.info(f"  ⏳ Next message in {delay_minutes} minutes")
            await asyncio.sleep(delay)

    cycle_manager.is_running = False
    logger.info(
        f"✅ Cycle #{cycle_manager.cycle_count} complete! "
        f"Total messages sent: {cycle_manager.messages_sent}"
    )

    # Start a new cycle after a brief pause
    logger.info("🔄 Starting new cycle in 30 seconds...")
    await asyncio.sleep(30)
    await send_cycle_messages()


# ─── Bot Events ──────────────────────────────────────────────────────────────

@bot.event
async def on_ready():
    """Called when the bot successfully connects to Discord."""
    logger.info(f"🇨🇴 {bot.user.name} is online and proud!")
    logger.info(f"   Bot ID: {bot.user.id}")
    logger.info(f"   Servers: {len(bot.guilds)}")
    logger.info(f"   Target Channel: {CHANNEL_ID}")

    # Set a cute status
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="over Colombia 🇨🇴",
        ),
        status=discord.Status.online,
    )

    # Start the messaging cycle
    if not cycle_manager.is_running:
        bot.loop.create_task(send_cycle_messages())


@bot.event
async def on_command_error(ctx, error):
    """Global error handler for commands."""
    if isinstance(error, commands.CommandNotFound):
        return
    logger.error(f"Command error: {error}")
    await ctx.send(
        embed=discord.Embed(
            description="❌ Something went wrong. Please try again.",
            color=discord.Color.from_hex("#CE1126"),
        )
    )


# ─── Commands ────────────────────────────────────────────────────────────────

@bot.command(name="ping", aliases=["status", "alive"])
async def ping(ctx):
    """Check if the bot is online and responsive."""
    latency = round(bot.latency * 1000)
    embed = discord.Embed(
        title="🇨🇴 Colombia Pride Bot",
        description="¡Estoy vivo y orgulloso!",
        color=random.choice(EMBED_COLORS),
        timestamp=datetime.utcnow(),
    )
    embed.add_field(name="⚡ Latency", value=f"{latency}ms", inline=True)
    embed.add_field(
        name="📊 Messages Sent",
        value=str(cycle_manager.messages_sent),
        inline=True,
    )
    embed.add_field(
        name="🔄 Current Cycle",
        value=f"#{cycle_manager.cycle_count}",
        inline=True,
    )
    embed.set_footer(text="🇨🇴 República de Colombia")
    await ctx.send(embed=embed)


@bot.command(name="stats")
async def stats(ctx):
    """Show bot statistics."""
    uptime_embed = discord.Embed(
        title="📊 Bot Statistics",
        color=discord.Color.from_hex("#FCD116"),
        timestamp=datetime.utcnow(),
    )
    uptime_embed.add_field(
        name="🇨🇴 Total Messages",
        value=str(cycle_manager.messages_sent),
        inline=True,
    )
    uptime_embed.add_field(
        name="🔄 Cycles Completed",
        value=str(cycle_manager.cycle_count),
        inline=True,
    )
    uptime_embed.add_field(
        name="📡 Servers",
        value=str(len(bot.guilds)),
        inline=True,
    )
    uptime_embed.set_footer(text="🇨🇴 República de Colombia")
    await ctx.send(embed=uptime_embed)


@bot.command(name="help")
async def help_cmd(ctx):
    """Show available commands."""
    embed = discord.Embed(
        title="🇨🇴 Colombia Pride Bot - Commands",
        description="Celebrating Colombia with elegance and pride!",
        color=discord.Color.from_hex("#003893"),
        timestamp=datetime.utcnow(),
    )
    embed.add_field(
        name="`!ping`",
        value="Check if the bot is online",
        inline=False,
    )
    embed.add_field(
        name="`!stats`",
        value="View bot statistics",
        inline=False,
    )
    embed.add_field(
        name="`!help`",
        value="Show this help message",
        inline=False,
    )
    embed.set_footer(text="🇨🇴 República de Colombia")
    await ctx.send(embed=embed)


# ─── Entry Point ─────────────────────────────────────────────────────────────

def main():
    """Start the bot with proper error handling."""
    try:
        logger.info("🚀 Starting Colombia Pride Bot...")
        bot.run(BOT_TOKEN)
    except KeyboardInterrupt:
        logger.info("👋 Bot shutting down gracefully...")
    except discord.LoginFailure:
        logger.critical("❌ Invalid bot token! Check your .env file.")
        sys.exit(1)
    except Exception as e:
        logger.critical(f"❌ Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
