"""
🇨🇴 Colombia Pride Bot - GitHub Actions Version (Extended)
Stays online for ~15 minutes to respond to commands and send messages.
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

# Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger("colombia_bot_github")

# ─── Bot Setup ───────────────────────────────────────────────────────────────

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents,
    description="🇨🇴 Celebrating Colombia with pride and elegance",
)

# Track stats
messages_sent = 0
cycle_count = 0


# ─── Embed Builder ───────────────────────────────────────────────────────────

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

    if color == discord.Color(0xFCD116):
        embed.set_author(name="☀️ Golden Spirit")
    elif color == discord.Color(0x003893):
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


async def add_reactions(message: discord.Message, is_holiday: bool = False):
    """Adds emoji reactions to a sent message."""
    if is_holiday:
        num_reactions = random.randint(MIN_REACTIONS + 1, MAX_REACTIONS + 2)
    else:
        num_reactions = random.randint(MIN_REACTIONS, MAX_REACTIONS)

    reactions = []
    if is_holiday:
        reactions.append("🇨🇴")

    available = [e for e in REACTION_EMOJIS if e not in reactions]
    reactions.extend(random.sample(available, min(num_reactions - len(reactions), len(available))))

    for emoji in reactions:
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
        messages_sent += 1
        logger.info(f"✨ Sent: {message[:50]}...")

        # Add reactions
        await add_reactions(sent_message, is_holiday=is_holiday)
        logger.info(f"✅ Added reactions")

    except Exception as e:
        logger.error(f"❌ Failed to send: {e}")


# ─── Commands ────────────────────────────────────────────────────────────────

@bot.command(name="ping", aliases=["status", "alive"])
async def ping(ctx):
    """Check if the bot is online and responsive."""
    latency = round(bot.latency * 1000)
    holiday = get_todays_holiday()
    holiday_text = f"\n🎉 **Holiday Today:** `{holiday}`" if holiday else ""

    embed = discord.Embed(
        title="🇨🇴 Colombia Pride Bot",
        description=f"¡Estoy vivo y orgulloso!{holiday_text}",
        color=random.choice(EMBED_COLORS),
        timestamp=datetime.utcnow(),
    )
    embed.add_field(name="⚡ Latency", value=f"{latency}ms", inline=True)
    embed.add_field(name="📊 Messages Sent", value=str(messages_sent), inline=True)
    embed.add_field(name="🔄 Cycles", value=str(cycle_count), inline=True)
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
    embed.add_field(name="🇨🇴 Messages Sent", value=str(messages_sent), inline=True)
    embed.add_field(name="🔄 Cycles", value=str(cycle_count), inline=True)
    embed.add_field(name="📡 Servers", value=str(len(bot.guilds)), inline=True)
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
        description=f"The bot detects these holidays:\n\n{holiday_list}",
        color=discord.Color(0xCE1126),
        timestamp=datetime.utcnow(),
    )

    today_holiday = get_todays_holiday()
    if today_holiday and today_holiday in holiday_names:
        embed.add_field(name="🎉 TODAY!", value=f"**{holiday_names[today_holiday]}**", inline=False)
    else:
        embed.add_field(name="📅 Today", value="No holiday today", inline=False)

    embed.set_footer(text="🇨🇴 República de Colombia")
    await ctx.send(embed=embed)


@bot.command(name="help")
async def help_cmd(ctx):
    """Show available commands."""
    embed = discord.Embed(
        title="🇨🇴 Colombia Pride Bot - Commands",
        description="Celebrating Colombia with elegance and pride!",
        color=discord.Color(0x003893),
        timestamp=datetime.utcnow(),
    )
    embed.add_field(name="`!ping`", value="Check bot status", inline=False)
    embed.add_field(name="`!stats`", value="View statistics", inline=False)
    embed.add_field(name="`!holidays`", value="See Colombian holidays", inline=False)
    embed.add_field(name="`!help`", value="Show this message", inline=False)
    embed.set_footer(text="🇨🇴 República de Colombia")
    await ctx.send(embed=embed)


# ─── Bot Events ──────────────────────────────────────────────────────────────

@bot.event
async def on_ready():
    """Called when bot connects to Discord."""
    global cycle_count
    cycle_count += 1
    
    logger.info(f"🇨🇴 {bot.user.name} is online!")
    logger.info(f"   Cycle #{cycle_count}")
    logger.info(f"   Will stay online for ~15 minutes")

    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="over Colombia 🇨🇴",
        ),
        status=discord.Status.online,
    )

    # Random decision: should we send a message this session?
    should_send = random.random() < 0.60

    if should_send:
        # Wait a bit before sending (natural feel)
        await asyncio.sleep(random.uniform(5, 30))
        await send_message()
    else:
        logger.info("💤 Skipping message this session (natural timing)")

    # Stay online for 15 minutes to respond to commands
    logger.info("👂 Listening for commands...")
    await asyncio.sleep(900)  # 15 minutes = 900 seconds

    # Time to shut down
    logger.info("👋 Session ending, shutting down...")
    await bot.close()


@bot.event
async def on_command_error(ctx, error):
    """Global error handler for commands."""
    if isinstance(error, commands.CommandNotFound):
        return
    logger.error(f"Command error: {error}")


# ─── Entry Point ─────────────────────────────────────────────────────────────

def main():
    """Main entry point."""
    logger.info("🚀 Starting Colombia Pride Bot (GitHub Actions - Extended Mode)")
    logger.info("   Bot will stay online for ~15 minutes")
    logger.info("   Commands: !ping, !stats, !holidays, !help")

    try:
        bot.run(BOT_TOKEN)
    except Exception as e:
        logger.error(f"❌ Bot error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
