"""
🇨🇴 Colombia Pride Bot - GitHub Actions Version (Smart Mode)
Stays online for 2-3 minutes to respond to commands, then exits.
Uses ~1,500 minutes/month (under GitHub's 2,000 limit)
"""

import os
import sys
import random
import asyncio
import logging
from datetime import datetime

import discord
from discord.ext import commands
from discord import app_commands

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
from kingdom_data import get_kingdom_data, get_towns_with_residents, get_total_residents, get_town_count

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
    help_command=None,  # Disable built-in help to allow custom help command
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
        description="Celebrating Colombia with elegance and pride!\n\n**Slash Commands (/):**\n`/citizens` - View all citizens\n`/towns` - View all towns\n`/leadership` - View kingdom leadership\n`/stats` - View kingdom statistics\n`/player <name>` - Search for a player\n\n**Prefix Commands (!):**\n`!ping` - Check bot status\n`!stats` - View statistics\n`!holidays` - See Colombian holidays\n`!fact` - Random Colombian fact\n`!quote` - Inspirational Colombian quote\n`!flag` - Show the Colombian flag\n`!color` - Random flag color with meaning\n`!emoji` - Random Colombian emoji\n`!message` - Random pride message\n`!help` - Show this message",
        color=discord.Color(0x003893),
        timestamp=datetime.utcnow(),
    )
    embed.set_footer(text="🇨🇴 Reino de Colombia · DiplomaticaMC")
    await ctx.send(embed=embed)


# ─── Slash Commands (Kingdom Data) ───────────────────────────────────────────

@bot.tree.command(name="citizens", description="View citizens of the Reino de Colombia")
async def slash_citizens(interaction: discord.Interaction):
    """Show all citizens from the kingdom."""
    await interaction.response.defer()
    
    # Fetch live data
    data = await get_kingdom_data()
    total_residents = data.get("total_residents", 0)
    total_towns = data.get("total_towns", 0)
    
    embed = discord.Embed(
        title="👥 Citizens of the Reino de Colombia",
        description=f"**{total_residents} residents** across **{total_towns} active towns**\n\nVisit [colombiadmc.site](https://colombiadmc.site) for the full directory!",
        color=discord.Color(0xFCD116),
        timestamp=datetime.utcnow(),
    )
    
    embed.add_field(
        name="👑 The Crown",
        value="• **9_88** - King of Colombia\n• **OliveTree316** - Prime Minister",
        inline=False
    )
    
    embed.add_field(
        name="🏛️ The Cabinet",
        value="• **Novum_Vetus** - Min. of Foreign & Internal Affairs\n• **Crowlia** - Min. of Defense\n• **qulipzz** - Min. of Justice and Law\n• **pato541** - Min. of Culture",
        inline=False
    )
    
    embed.add_field(
        name="📊 Live Statistics",
        value=f"• Active Residents: **{total_residents}**\n• Active Towns: **{total_towns}**\n• Capital: **Maicao**",
        inline=False
    )
    
    embed.set_thumbnail(url="https://colombiadmc.site/assets/escudo.png")
    embed.set_footer(text="🇨🇴 Reino de Colombia · DiplomaticaMC · Live data")
    
    await interaction.followup.send(embed=embed)


@bot.tree.command(name="towns", description="View all towns in the Reino de Colombia")
async def slash_towns(interaction: discord.Interaction):
    """Show all towns from the kingdom."""
    await interaction.response.defer()
    
    # Fetch live data
    towns = await get_towns_with_residents()
    total_towns = len(towns)
    
    embed = discord.Embed(
        title="🏘️ Towns of the Reino de Colombia",
        description=f"**{total_towns} active towns** with residents\n\nVisit [colombiadmc.site](https://colombiadmc.site/#citizens) for the full list!",
        color=discord.Color(0x003893),
        timestamp=datetime.utcnow(),
    )
    
    # Show top towns (up to 10)
    if towns:
        top_towns = towns[:10]
        town_list = "\n".join([
            f"• **{town['name']}** - {town['residents']} resident{'s' if town['residents'] != 1 else ''}"
            for town in top_towns
        ])
        
        embed.add_field(
            name="🏘️ Towns with Residents",
            value=town_list,
            inline=False
        )
        
        # Show remaining towns if any
        if len(towns) > 10:
            remaining = [t["name"] for t in towns[10:]]
            embed.add_field(
                name=f"📊 {len(remaining)} More Towns",
                value=", ".join(remaining),
                inline=False
            )
    else:
        embed.add_field(
            name="🏘️ Towns",
            value="No towns with residents found. Check the [website](https://colombiadmc.site) for updates!",
            inline=False
        )
    
    embed.set_thumbnail(url="https://colombiadmc.site/assets/escudo.png")
    embed.set_footer(text="🇨🇴 Reino de Colombia · DiplomaticaMC · Live data")
    
    await interaction.followup.send(embed=embed)


@bot.tree.command(name="leadership", description="View the leadership of the Reino de Colombia")
async def slash_leadership(interaction: discord.Interaction):
    """Show the kingdom's leadership."""
    await interaction.response.defer()
    
    embed = discord.Embed(
        title="👑 Leadership of the Reino de Colombia",
        description="The Crown and Cabinet that guide the empire",
        color=discord.Color(0xCE1126),
        timestamp=datetime.utcnow(),
    )
    
    # The Crown
    embed.add_field(
        name="👑 The Crown",
        value=(
            "**King of Colombia**\n"
            "![9_88](https://mc-heads.net/avatar/9_88/64) **9_88**\n"
            "Founder of the Empire and sovereign of the Caribbean seat.\n\n"
            "**Prime Minister**\n"
            "![OliveTree316](https://mc-heads.net/avatar/OliveTree316/64) **OliveTree316**\n"
            "Runs day-to-day government, based in Medellín Antioquia."
        ),
        inline=False
    )
    
    # The Cabinet
    embed.add_field(
        name="🏛️ The Cabinet",
        value=(
            "🌎 **Min. of Foreign & Internal Affairs**\n"
            "![Novum_Vetus](https://mc-heads.net/avatar/Novum_Vetus/64) **Novum_Vetus**\n\n"
            "🛡️ **Min. of Defense**\n"
            "![Crowlia](https://mc-heads.net/avatar/Crowlia/64) **Crowlia**\n\n"
            "⚖️ **Min. of Justice and Law**\n"
            "![qulipzz](https://mc-heads.net/avatar/qulipzz/64) **qulipzz**\n\n"
            "🎨 **Min. of Culture**\n"
            "![pato541](https://mc-heads.net/avatar/pato541/64) **pato541**"
        ),
        inline=False
    )
    
    embed.set_thumbnail(url="https://colombiadmc.site/assets/escudo.png")
    embed.set_footer(text="🇨🇴 Plus Ultra, further beyond")
    
    await interaction.followup.send(embed=embed)


@bot.tree.command(name="kingdom", description="View kingdom statistics")
async def slash_kingdom(interaction: discord.Interaction):
    """Show kingdom statistics."""
    await interaction.response.defer()
    
    # Fetch live data
    data = await get_kingdom_data()
    total_residents = data.get("total_residents", 0)
    total_towns = data.get("total_towns", 0)
    
    embed = discord.Embed(
        title="📊 Kingdom Statistics",
        description="Reino de Colombia · DiplomaticaMC",
        color=discord.Color(0xFCD116),
        timestamp=datetime.utcnow(),
    )
    
    embed.add_field(
        name="👥 Population",
        value=f"**{total_residents}** residents",
        inline=True
    )
    
    embed.add_field(
        name="🏘️ Towns",
        value=f"**{total_towns}** active towns",
        inline=True
    )
    
    embed.add_field(
        name="🏛️ Leadership",
        value="**1** King\n**1** Prime Minister\n**5** Cabinet Ministers",
        inline=True
    )
    
    embed.add_field(
        name="🏛️ Capital",
        value="**Maicao**\nMain claim on the water",
        inline=True
    )
    
    embed.add_field(
        name="🌎 Regions",
        value="• Colombian Region\n• Central America\n• Caribbean\n• South America",
        inline=True
    )
    
    embed.add_field(
        name="🔗 Links",
        value="[Website](https://colombiadmc.site) | [Discord](https://discord.gg/YUyHgnpXwj) | [Wiki](https://wiki.diplomaticamc.com/wiki/Colombia)",
        inline=False
    )
    
    embed.set_thumbnail(url="https://colombiadmc.site/assets/escudo.png")
    embed.set_footer(text="🇨🇴 Plus Ultra, further beyond · Live data")
    
    await interaction.followup.send(embed=embed)


@bot.tree.command(name="player", description="Search for a player in the kingdom")
@app_commands.describe(name="Minecraft username to search for")
async def slash_player(interaction: discord.Interaction, name: str):
    """Search for a specific player."""
    await interaction.response.defer()
    
    # Sample player data - in production, this would fetch from your website API
    players = {
        "9_88": {"role": "King of Colombia", "town": "Maicao"},
        "OliveTree316": {"role": "Prime Minister", "town": "Iza"},
        "Novum_Vetus": {"role": "Min. of Foreign & Internal Affairs", "town": "Santa Maria"},
        "Crowlia": {"role": "Min. of Defense", "town": "Aldama"},
        "qulipzz": {"role": "Min. of Justice and Law", "town": "Santa Maria"},
        "pato541": {"role": "Min. of Culture", "town": "Maicao"},
        "Zaity1": {"role": "Citizen", "town": "Tegucigalpa"},
    }
    
    # Case-insensitive search
    player_data = None
    for player_name, data in players.items():
        if player_name.lower() == name.lower():
            player_data = data
            name = player_name
            break
    
    if not player_data:
        embed = discord.Embed(
            title="❌ Player Not Found",
            description=f"Could not find **{name}** in the kingdom directory.\n\nVisit [colombiadmc.site](https://colombiadmc.site/#citizens) to see all citizens!",
            color=discord.Color(0xCE1126),
            timestamp=datetime.utcnow(),
        )
        embed.set_footer(text="🇨🇴 Reino de Colombia · DiplomaticaMC")
        await interaction.followup.send(embed=embed)
        return
    
    embed = discord.Embed(
        title=f"🎮 {name}",
        description=f"**Role:** {player_data['role']}\n**Town:** {player_data['town']}",
        color=discord.Color(0xFCD116),
        timestamp=datetime.utcnow(),
    )
    
    embed.set_thumbnail(url=f"https://mc-heads.net/avatar/{name}/128")
    embed.set_footer(text="🇨🇴 Reino de Colombia · DiplomaticaMC")
    
    await interaction.followup.send(embed=embed)


@bot.command(name="fact", aliases=["dato", "sabias"])
async def fact(ctx):
    """Share a random Colombian fact."""
    facts = [
        ("🦜", "Colombia has more bird species than any other country — over 1,900!"),
        ("🌺", "Colombia produces 70% of the world's emeralds."),
        ("☕", "Colombian coffee is considered the best in the world."),
        ("🏔️", "Colombia is the only South American country with coastlines on both the Pacific and Caribbean."),
        ("🌳", "Colombia contains 10% of all species on Earth."),
        ("🎨", "Fernando Botero's art is recognized worldwide for its unique style."),
        ("🎵", "Colombia has 1,020 traditional rhythms and musical styles."),
        ("🌹", "Colombia is the second-largest flower exporter in the world."),
        ("🏛️", "Bogotá's Gold Museum houses the world's largest collection of pre-Columbian gold."),
        ("🌊", "Colombia has the most freshwater rivers in South America."),
        ("🦋", "Colombia has over 3,274 butterfly species — more than any other country."),
        ("🎭", "The Barranquilla Carnival is the second-largest in the world."),
        ("📚", "Gabriel García Márquez won the Nobel Prize in Literature in 1982."),
        ("🏆", "Colombia has won 37 Olympic medals throughout history."),
        ("🌿", "The Amazon rainforest covers 48% of Colombia's territory."),
    ]
    
    emoji, fact_text = random.choice(facts)
    
    embed = discord.Embed(
        title=f"{emoji} Did You Know?",
        description=fact_text,
        color=random.choice(EMBED_COLORS),
        timestamp=datetime.utcnow(),
    )
    embed.set_footer(text="🇨🇴 Fun Colombian Facts")
    await ctx.send(embed=embed)


@bot.command(name="quote", aliases=["frase", "inspiracion"])
async def quote(ctx):
    """Share an inspirational Colombian quote."""
    quotes = [
        ("Gabriel García Márquez", "Life is not what one lived, but what one remembers."),
        ("Gabriel García Márquez", "Human beings are not born once and for all on the day their mothers give birth to them."),
        ("Shakira", "I'm not a feminist, but I believe in women's power."),
        ("Fernando Botero", "Art is not about copying reality, but creating a new one."),
        ("Colombian Proverb", "El que mucho abarca, poco aprieta. (He who grasps at too much, holds little.)"),
        ("Colombian Proverb", "No hay mal que por bien no venga. (There's no bad from which good doesn't come.)"),
        ("Colombian Proverb", "Más vale pájaro en mano que ciento volando. (A bird in hand is worth two in the bush.)"),
        ("Juanes", "Music is the universal language that connects us all."),
        ("Carlos Vives", "Our roots make us who we are."),
        ("Nairo Quintana", "Every mountain is an opportunity."),
    ]
    
    author, quote_text = random.choice(quotes)
    
    embed = discord.Embed(
        title="💭 Colombian Wisdom",
        description=f'"{quote_text}"',
        color=random.choice(EMBED_COLORS),
        timestamp=datetime.utcnow(),
    )
    embed.set_footer(text=f"— {author} 🇨🇴")
    await ctx.send(embed=embed)


@bot.command(name="flag", aliases=["bandera"])
async def flag(ctx):
    """Show the Colombian flag with pride."""
    embed = discord.Embed(
        title="🇨🇴 The Colombian Flag",
        description=(
            "The national flag of Colombia is a symbol of our sovereignty, "
            "honor, and bravery.\n\n"
            "**Yellow** (top half): Sovereignty, justice, and the rich soil\n"
            "**Blue** (quarter): The sky, the seas, loyalty, and perseverance\n"
            "**Red** (quarter): The blood of heroes who fought for freedom"
        ),
        color=discord.Color(0xFCD116),
        timestamp=datetime.utcnow(),
    )
    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Flag_of_Colombia.svg/1200px-Flag_of_Colombia.svg.png")
    embed.set_footer(text="🇨🇴 Ley 12 de 1967")
    await ctx.send(embed=embed)


@bot.command(name="color", aliases=["colour", "color"])
async def color_cmd(ctx):
    """Show a random flag color with its meaning."""
    colors = [
        {
            "name": "Yellow",
            "hex": "FCD116",
            "meaning": "Sovereignty, justice, and the rich Colombian soil",
            "emoji": "💛",
        },
        {
            "name": "Blue",
            "hex": "003893",
            "meaning": "The sky, the seas, loyalty, and perseverance",
            "emoji": "💙",
        },
        {
            "name": "Red",
            "hex": "CE1126",
            "meaning": "The blood of heroes who fought for our freedom",
            "emoji": "❤️",
        },
    ]
    
    color = random.choice(colors)
    
    embed = discord.Embed(
        title=f"{color['emoji']} {color['name']}",
        description=color['meaning'],
        color=discord.Color(int(color['hex'], 16)),
        timestamp=datetime.utcnow(),
    )
    embed.add_field(name="Hex Code", value=f"`#{color['hex']}`", inline=True)
    embed.set_footer(text="🇨🇴 Official Colombian Flag Colors")
    await ctx.send(embed=embed)


@bot.command(name="emoji", aliases=["emojis"])
async def emoji_cmd(ctx):
    """Show random Colombian-themed emojis."""
    emoji_sets = [
        ["🇨🇴", "💛", "💙", "❤️"],
        ["☕", "🌱", "🏔️", "🌺"],
        ["🦜", "🦋", "🐆", "🌳"],
        ["💃", "🕺", "🎵", "🎺"],
        ["🏔️", "🌊", "🌅", "⛰️"],
        ["🎉", "✨", "🌟", "💫"],
        ["🌹", "🌸", "🌻", "🌷"],
        ["📚", "🎨", "🎭", "🎬"],
    ]
    
    emojis = random.choice(emoji_sets)
    
    embed = discord.Embed(
        title="🇨🇴 Colombian Emojis",
        description=" ".join(emojis),
        color=random.choice(EMBED_COLORS),
        timestamp=datetime.utcnow(),
    )
    embed.set_footer(text="🇨🇴 Express your Colombian pride!")
    await ctx.send(embed=embed)


@bot.command(name="message", aliases=["msg", "random"])
async def message_cmd(ctx):
    """Show a random Colombian pride message."""
    base_message = random.choice(BASE_MESSAGES)
    message = get_random_emoji_message(base_message)
    
    embed = discord.Embed(
        description=message,
        color=random.choice(EMBED_COLORS),
        timestamp=datetime.utcnow(),
    )
    embed.set_footer(text="🇨🇴 República de Colombia")
    await ctx.send(embed=embed)


@bot.command(name="squad", aliases=["players", "team", "seleccion"])
async def squad(ctx):
    """Show Colombia's 2026 World Cup squad."""
    squad_data = {
        "Goalkeepers": [
            "Camilo Vargas (Atlas)",
            "David Ospina (Atletico Nacional)",
            "Álvaro Montero (Velez Sarsfield)",
        ],
        "Defenders": [
            "Johan Mojica (RCD Mallorca)",
            "Devier Machado (Nantes)",
            "Daniel Muñoz (Crystal Palace)",
            "Santiago Arias (Bahia)",
            "Yerry Mina (Cagliari)",
            "Davinson Sánchez (Galatasaray)",
            "Jhon Lucumí (Bologna)",
            "Willer Ditta (Cruz Azul)",
        ],
        "Midfielders": [
            "James Rodríguez ⭐ (Minnesota United)",
            "Jefferson Lerma (Crystal Palace)",
            "Richard Ríos (Benfica)",
            "Juan Fernando Quintero (Racing Club)",
            "Jorge Carrascal (Dinamo Moscow)",
            "Kevin Castaño (Krasnodar)",
            "Jaminton Campaz (Rosario Central)",
        ],
        "Forwards": [
            "Luis Díaz ⭐ (Bayern Munich)",
            "Carlos Andrés Gómez",
            "Jhon Córdoba (Krasnodar)",
            "Juan Camilo Hernández (Columbus)",
            "Jhon Arias (Wolverhampton)",
        ],
    }
    
    embed = discord.Embed(
        title="🇨🇴 Colombia 2026 World Cup Squad",
        description="**Manager:** Néstor Lorenzo\n**Captain:** James Rodríguez\n**Group:** Portugal, DR Congo, Uzbekistan",
        color=discord.Color(0xFCD116),
        timestamp=datetime.utcnow(),
    )
    
    for position, players in squad_data.items():
        embed.add_field(
            name=f"**{position}**",
            value="\n".join(f"• {player}" for player in players),
            inline=False,
        )
    
    embed.set_footer(text="🇨🇴 ¡Vamos Colombia! ⚽")
    await ctx.send(embed=embed)


@bot.command(name="star", aliases=["stars", "key"])
async def star_players(ctx):
    """Show Colombia's key players to watch."""
    stars = [
        {
            "name": "Luis Díaz",
            "position": "Forward",
            "club": "Bayern Munich",
            "info": "Star winger, 7 goals in qualifiers",
            "emoji": "⚡",
        },
        {
            "name": "James Rodríguez",
            "position": "Midfielder",
            "club": "Minnesota United",
            "info": "Captain, 2014 World Cup Golden Boot winner",
            "emoji": "👑",
        },
        {
            "name": "Richard Ríos",
            "position": "Midfielder",
            "club": "Benfica",
            "info": "Rising star, impressed under Mourinho",
            "emoji": "🌟",
        },
    ]
    
    embed = discord.Embed(
        title="⭐ Colombia's Stars to Watch",
        description="Key players for the 2026 World Cup",
        color=discord.Color(0xCE1126),
        timestamp=datetime.utcnow(),
    )
    
    for star in stars:
        embed.add_field(
            name=f"{star['emoji']} {star['name']}",
            value=f"**Position:** {star['position']}\n**Club:** {star['club']}\n**Info:** {star['info']}",
            inline=False,
        )
    
    embed.set_footer(text="🇨🇴 Los Cafeteros ⚽")
    await ctx.send(embed=embed)


# ─── Bot Events ──────────────────────────────────────────────────────────────

@bot.event
async def on_ready():
    """Called when bot connects to Discord."""
    global cycle_count
    cycle_count += 1
    
    logger.info(f"🇨🇴 {bot.user.name} is online!")
    logger.info(f"   Cycle #{cycle_count}")
    logger.info(f"   Will stay online for ~2 minutes (commands work!)")

    # Sync slash commands
    try:
        synced = await bot.tree.sync()
        logger.info(f"✅ Synced {len(synced)} slash commands")
    except Exception as e:
        logger.error(f"❌ Failed to sync slash commands: {e}")

    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="over Colombia 🇨🇴",
        ),
        status=discord.Status.online,
    )

    # Send a message immediately (80% chance)
    if random.random() < 0.80:
        await asyncio.sleep(random.uniform(3, 10))
        await send_message()
    else:
        logger.info("💤 Skipping message this session")

    # Stay online for 2 minutes to respond to commands
    logger.info("👂 Listening for commands for 2 minutes...")
    await asyncio.sleep(120)  # 2 minutes = 120 seconds

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
    logger.info("🚀 Starting Colombia Pride Bot (GitHub Actions - Smart Mode)")
    logger.info("   Bot will stay online for ~2 minutes")
    logger.info("   Commands work during this window!")
    logger.info("   Commands: !ping, !stats, !holidays, !help")

    try:
        bot.run(BOT_TOKEN)
    except Exception as e:
        logger.error(f"❌ Bot error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
