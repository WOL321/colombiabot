"""
🇨🇴 Colombia Pride Bot
A beautiful Discord bot that celebrates Colombia with style.
Posts elegant embeds with Colombian pride messages at natural intervals.

Features:
  🎨 Premium embeds with Colombian flag colors
  🇨🇴 Holiday detection with special messages
  💬 Emoji variations for fresh content
  🎉 Auto emoji reactions on every message
  🔄 Rolling 5-hour cycles with organic timing
"""

import os
import sys
import random
import asyncio
import logging
from datetime import datetime, timedelta

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
    CYCLE_DURATION_HOURS,
    MIN_GAP_MINUTES,
    MAX_GAP_MINUTES,
    FOOTERS,
    HOLIDAY_FOOTERS,
    get_todays_holiday,
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
    help_command=None,  # Disable built-in help to allow custom help command
)


# ─── Embed Builder ───────────────────────────────────────────────────────────

def get_random_emoji_message(base_message: str) -> str:
    """
    Returns a random emoji variation of a base message.
    Keeps content fresh and visually diverse.
    """
    variations = EMOJI_VARIATIONS.get(base_message, [base_message])
    return random.choice(variations)


def create_pride_embed(message: str, is_holiday: bool = False) -> discord.Embed:
    """
    Creates a beautiful, premium embed with Colombian flag colors.
    Randomly selects color and footer for variety.
    Special holiday styling when is_holiday=True.
    """
    color = random.choice(EMBED_COLORS)

    # Choose footer based on whether it's a holiday
    if is_holiday:
        footer = random.choice(HOLIDAY_FOOTERS)
    else:
        footer = random.choice(FOOTERS)

    embed = discord.Embed(
        description=message,
        color=color,
        timestamp=datetime.utcnow(),
    )

    embed.set_footer(text=footer)

    # Add decorative author based on color
    if color == discord.Color(0xFCD116):
        embed.set_author(name="☀️ Golden Spirit")
    elif color == discord.Color(0x003893):
        embed.set_author(name="🌊 Deep Blue Ocean")
    else:
        embed.set_author(name="🌹 Passionate Red")

    # Holiday special styling
    if is_holiday:
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Flag_of_Colombia.svg/1200px-Flag_of_Colombia.svg.png")
        embed.add_field(
            name="🎉",
            value="*Special Holiday Edition*",
            inline=False,
        )

    return embed


def get_holiday_message() -> str | None:
    """
    Check if today is a Colombian holiday and return a special message.
    Returns None if it's not a holiday.
    """
    holiday_key = get_todays_holiday()

    if holiday_key and holiday_key in HOLIDAY_MESSAGES:
        messages = HOLIDAY_MESSAGES[holiday_key]
        return random.choice(messages)

    return None


# ─── Reaction Handler ────────────────────────────────────────────────────────

async def add_reactions(message: discord.Message, is_holiday: bool = False):
    """
    Adds emoji reactions to a sent message.
    More reactions on holidays for extra celebration!
    """
    # Choose how many reactions to add
    if is_holiday:
        num_reactions = random.randint(MIN_REACTIONS + 1, MAX_REACTIONS + 2)
    else:
        num_reactions = random.randint(MIN_REACTIONS, MAX_REACTIONS)

    # Always include the flag on holidays
    reactions = []
    if is_holiday:
        reactions.append("🇨🇴")

    # Pick random unique reactions
    available = [e for e in REACTION_EMOJIS if e not in reactions]
    reactions.extend(random.sample(available, min(num_reactions - len(reactions), len(available))))

    # Add reactions with small delays for a natural feel
    for emoji in reactions:
        try:
            await message.add_reaction(emoji)
            await asyncio.sleep(random.uniform(0.5, 1.5))
        except discord.HTTPException:
            # Skip if emoji fails (e.g., custom emoji not available)
            continue
        except discord.Forbidden:
            logger.warning("Missing permission to add reactions")
            break


# ─── Core Messaging Loop ─────────────────────────────────────────────────────

class ColombiaCycle:
    """
    Manages the rolling 5-hour cycle with natural, unpredictable timing.
    Each cycle sends messages at random intervals (25-40 min gap).
    """

    def __init__(self):
        self.cycle_count = 0
        self.messages_sent = 0
        self.holiday_messages_sent = 0
        self.is_running = False
        self.last_holiday_check = None

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

    def get_messages_for_cycle(self) -> int:
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

    # Check for holidays at the start of each cycle
    holiday_message = get_holiday_message()
    is_holiday_today = holiday_message is not None

    if is_holiday_today:
        logger.info(f"🎉 HOLIDAY DETECTED! Special messages enabled today!")

    for i in range(messages_this_cycle):
        if not cycle_manager.is_running:
            break

        # Determine if this message should be a holiday message
        # Send a holiday message on the first post if it's a holiday
        use_holiday = is_holiday_today and i == 0

        if use_holiday:
            message = holiday_message
            logger.info(f"  🎊 Sending HOLIDAY special message!")
        else:
            # Pick a random base message and apply emoji variation
            base_message = random.choice(BASE_MESSAGES)
            message = get_random_emoji_message(base_message)

        embed = create_pride_embed(message, is_holiday=use_holiday)

        try:
            sent_message = await channel.send(embed=embed)
            cycle_manager.messages_sent += 1

            if use_holiday:
                cycle_manager.holiday_messages_sent += 1

            logger.info(
                f"  ✨ Sent message {i + 1}/{messages_this_cycle}: "
                f'"{message[:40]}..."'
            )

            # Add emoji reactions (the fun part!)
            await add_reactions(sent_message, is_holiday=use_holiday)

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

    # Check if today is a holiday
    holiday = get_todays_holiday()
    if holiday:
        logger.info(f"   🎉 Today is a Colombian holiday: {holiday}!")

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
            color=discord.Color(0xCE1126),
        )
    )


# ─── Commands ────────────────────────────────────────────────────────────────

@bot.command(name="ping", aliases=["status", "alive"])
async def ping(ctx):
    """Check if the bot is online and responsive."""
    latency = round(bot.latency * 1000)

    # Check if today is a holiday
    holiday = get_todays_holiday()
    holiday_text = f"\n🎉 **Holiday Today:** `{holiday}`" if holiday else ""

    embed = discord.Embed(
        title="🇨🇴 Colombia Pride Bot",
        description=f"¡Estoy vivo y orgulloso!{holiday_text}",
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
    embed.add_field(
        name="🎊 Holiday Posts",
        value=str(cycle_manager.holiday_messages_sent),
        inline=True,
    )
    embed.set_footer(text="🇨🇴 República de Colombia")
    await ctx.send(embed=embed)


@bot.command(name="stats")
async def stats(ctx):
    """Show bot statistics."""
    embed = discord.Embed(
        title="📊 Bot Statistics",
        color=discord.Color(0xFCD116),
        timestamp=datetime.utcnow(),
    )
    embed.add_field(
        name="🇨🇴 Total Messages",
        value=str(cycle_manager.messages_sent),
        inline=True,
    )
    embed.add_field(
        name="🔄 Cycles Completed",
        value=str(cycle_manager.cycle_count),
        inline=True,
    )
    embed.add_field(
        name="🎊 Holiday Specials",
        value=str(cycle_manager.holiday_messages_sent),
        inline=True,
    )
    embed.add_field(
        name="📡 Servers",
        value=str(len(bot.guilds)),
        inline=True,
    )
    embed.add_field(
        name="💬 Emoji Variations",
        value=str(sum(len(v) for v in EMOJI_VARIATIONS.values())),
        inline=True,
    )
    embed.add_field(
        name="🎉 Reaction Pool",
        value=str(len(REACTION_EMOJIS)),
        inline=True,
    )

    # Holiday info
    holiday = get_todays_holiday()
    if holiday:
        embed.add_field(
            name="🎉 Today's Holiday",
            value=f"`{holiday}`",
            inline=False,
        )

    embed.set_footer(text="🇨🇴 República de Colombia")
    await ctx.send(embed=embed)


@bot.command(name="help")
async def help_cmd(ctx):
    """Show available commands."""
    embed = discord.Embed(
        title="🇨🇴 Colombia Pride Bot - Commands",
        description="Celebrating Colombia with elegance, emojis, and pride!",
        color=discord.Color(0x003893),
        timestamp=datetime.utcnow(),
    )
    embed.add_field(
        name="`!ping`",
        value="Check if the bot is online",
        inline=False,
    )
    embed.add_field(
        name="`!stats`",
        value="View bot statistics and holiday info",
        inline=False,
    )
    embed.add_field(
        name="`!holidays`",
        value="See upcoming Colombian holidays",
        inline=False,
    )
    embed.add_field(
        name="`!help`",
        value="Show this help message",
        inline=False,
    )

    embed.add_field(
        name="✨ Features",
        value=(
            "• Premium embeds with flag colors\n"
            "• Holiday detection & special messages\n"
            "• Emoji variations for fresh content\n"
            "• Auto emoji reactions on every post\n"
            "• Natural 25-40 min intervals"
        ),
        inline=False,
    )
    embed.set_footer(text="🇨🇴 República de Colombia")
    await ctx.send(embed=embed)


@bot.command(name="holidays", aliases=["festivos", "calendar"])
async def holidays(ctx):
    """Show Colombian holidays the bot celebrates."""
    holiday_names = {
        "new_year": "🎆 New Year's Day (Jan 1)",
        "labor_day": "💪 Labor Day (May 1)",
        "independence_day": "🇨🇴 Independence Day (Jul 20)",
        "battle_of_boyaca": "⚔️ Battle of Boyacá (Aug 7)",
        "race_day": "🌎 Día de la Raza (Oct 12)",
        "cartagena_independence": "🏰 Cartagena Independence (Nov 11)",
        "candelaria": "🕯️ Día de las Velitas (Dec 7)",
        "immaculate_conception": "⭐ Inmaculada Concepción (Dec 8)",
        "christmas": "🎄 Christmas (Dec 25)",
    }

    holiday_list = "\n".join(f"• {name}" for name in holiday_names.values())

    embed = discord.Embed(
        title="🇨🇴 Colombian Holidays Calendar",
        description=(
            "The bot detects these holidays and sends special "
            "celebration embeds with extra reactions!\n\n"
            f"{holiday_list}"
        ),
        color=discord.Color(0xCE1126),
        timestamp=datetime.utcnow(),
    )

    # Check if today is a holiday
    today_holiday = get_todays_holiday()
    if today_holiday and today_holiday in holiday_names:
        embed.add_field(
            name="🎉 TODAY!",
            value=f"**{holiday_names[today_holiday]}**",
            inline=False,
        )
    else:
        embed.add_field(
            name="📅 Today",
            value="No holiday today — regular messages!",
            inline=False,
        )

    embed.set_footer(text="🇨🇴 República de Colombia")
    await ctx.send(embed=embed)


# ─── Entry Point ─────────────────────────────────────────────────────────────

def main():
    """Start the bot with proper error handling."""
    try:
        logger.info("🚀 Starting Colombia Pride Bot...")
        logger.info("   Features: Holiday Detection | Emoji Variations | Auto Reactions")
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
