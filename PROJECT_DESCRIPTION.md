# 🇨🇴 Colombia Pride Bot - Complete Project Description

## What This Is

A Discord bot that automatically posts Colombian pride messages in a server. Think of it like those patriotic slogans you see in different countries - "¡Viva Colombia!", "We export more than just coffee", etc. It's a fun, aesthetic bot that celebrates Colombian culture with style.

## Core Functionality

**Automatic Messages:**
- Posts a random Colombian pride message every 25-40 minutes
- Messages are wrapped in beautiful Discord embeds with official Colombian flag colors (yellow #FCD116, blue #003893, red #CE1126)
- Each message gets 3-5 random emoji reactions (🇨🇴 💛 💙 ❤️ ☕ 🌺 🎉 ✨ etc.)
- Runs 24/7 on GitHub Actions (free, no server needed)

**Holiday Detection:**
- Automatically detects Colombian holidays (July 20 Independence Day, Christmas, Día de las Velitas, etc.)
- Sends special celebration embeds on holidays with extra emoji reactions
- Shows "🎉 Special Holiday Edition" badge on holiday messages

**Interactive Commands:**
- `!fact` - Random Colombian facts (biodiversity, coffee, emeralds, etc.)
- `!quote` - Inspirational quotes from Colombians (García Márquez, Shakira, etc.)
- `!flag` - Shows the Colombian flag with color meanings
- `!color` - Random flag color with hex code and meaning
- `!emoji` - Random Colombian emoji sets
- `!message` - Random pride message on demand
- `!ping` - Check if bot is online
- `!stats` - View bot statistics
- `!holidays` - See Colombian holidays calendar
- `!help` - Show all commands

## Message Examples

The bot has 23 different base messages with 100+ emoji variations:

**Classic Pride:**
- 🇨🇴 ¡Viva Colombia! 🇨🇴
- ☕ We export more than just coffee. 🌎
- 💛 Yellow. 💙 Blue. ❤️ Red. 🇨🇴

**Cultural Pride:**
- 🏔️ From the Andes to the Caribbean — Colombia has it all. 🌊
- 📚 Gabriel García Márquez taught the world to dream in Spanish. ✨
- 💃 From salsa to vallenato — our rhythm is infectious. 🎶
- 🦜 Biodiversity? Colombia has 10% of ALL species on Earth. 🌺
- ☕ Colombian coffee: liquid gold in a cup. ✨

**Geographic Pride:**
- 🏰 Cartagena: where history meets the sea. 🌊
- 🌸 Medellín: City of Eternal Spring. 🌺
- 🏙️ Bogotá: the heart that beats at 2,640 meters. 💓
- 🌳 The Amazon starts here. So does the magic. ✨
- 🌊 From the Pacific to the Caribbean — we embrace both oceans. ⚓

**Food & Culture:**
- 🫓 Arepas, bandeja paisa, ajiaco — food that feeds the soul. 🍲
- 🌹 Colombia: more flowers than you can imagine. 🌺
- 💎 Colombia: where emeralds are born. ✨

## Technical Setup

**Hosting:**
- Runs on GitHub Actions (completely free)
- Bot stays online for 2 minutes every 50 minutes
- Uses ~1,500 minutes/month (under GitHub's 2,000 limit)
- No server, no credit card, no cost

**Architecture:**
- `bot_github.py` - Main bot file (GitHub Actions version)
- `config.py` - All messages, colors, holidays, emoji variations
- `.github/workflows/keep-alive.yml` - GitHub Actions workflow
- Uses discord.py library
- Environment variables for token and channel ID (secure)

**Key Features:**
- Cross-version compatible (fixed discord.Color.from_hex issue)
- Custom help command (disabled default to avoid conflicts)
- Holiday detection system with calendar
- Emoji reaction system with randomization
- Embed builder with color rotation
- Message variation system (100+ combinations)

## Visual Aesthetic

**Embed Design:**
- Clean, modern Discord embeds
- Random color from Colombian flag (yellow, blue, or red)
- Author line with thematic name (☀️ Golden Spirit, 🌊 Deep Blue Ocean, 🌹 Passionate Red)
- Footer with Colombian pride text
- Timestamp for authenticity
- Left border color matches embed color

**Emoji Reactions:**
- Pool of 12 Colombian-themed emojis
- Random selection of 3-5 per message
- More reactions on holidays (5-7)
- Flag emoji guaranteed on holidays

**Color Palette:**
- Yellow: #FCD116 (Sovereignty & Justice)
- Blue: #003893 (Loyalty & Perseverance)
- Red: #CE1126 (Valor & Blood of Heroes)

## Colombian Holidays Supported

- 🎆 New Year's Day (Jan 1)
- 💪 Labor Day (May 1)
- 🇨🇴 Independence Day (Jul 20)
- ⚔️ Battle of Boyacá (Aug 7)
- 🌎 Día de la Raza (Oct 12)
- 🏰 Cartagena Independence (Nov 11)
- 🕯️ Día de las Velitas (Dec 7)
- ⭐ Inmaculada Concepción (Dec 8)
- 🎄 Christmas (Dec 25)

## The Vibe

This isn't a corporate product or a serious tool. It's a fun, aesthetic Discord bot that:
- Celebrates Colombian culture
- Looks beautiful with flag colors
- Feels organic and natural (not robotic)
- Spreads positivity and pride
- Has personality (emoji reactions, varied messages)

Think of it like having a friend who randomly posts cool Colombian stuff in your Discord server, but it's automated and always looks good.

## What Makes It Cool

1. **Aesthetic** - Every message is wrapped in a premium embed
2. **Variety** - 100+ message combinations, never repetitive
3. **Interactive** - Commands for facts, quotes, flag info
4. **Smart** - Detects holidays automatically
5. **Free** - Runs on GitHub Actions, zero cost
6. **Simple** - Just works, no complex setup
7. **Proud** - Everything celebrates Colombia

## Use Cases

- Colombian Discord servers wanting to celebrate their culture
- International servers wanting to showcase Colombian pride
- Fun addition to any community
- Educational (teaches about Colombian culture through facts)
- Just vibes ✨

## What It's NOT

- Not a website (no frontend)
- Not a complex application
- Not a business tool
- Not connected to external APIs or databases
- Not a Minecraft server integration (we removed that)
- Not overcomplicated

It's just a bot that posts Colombian pride messages and looks good doing it.

## Files Structure

```
bot/
├── bot_github.py          # Main bot (GitHub Actions version)
├── bot.py                 # Local version (if running on own machine)
├── config.py              # All configuration (messages, colors, holidays)
├── requirements.txt       # Python dependencies
├── .env.example           # Environment variable template
├── .gitignore            # Git ignore rules
├── README.md             # Documentation
└── .github/
    └── workflows/
        └── keep-alive.yml # GitHub Actions workflow
```

## How to Use

1. Create Discord bot at discord.com/developers
2. Get bot token and channel ID
3. Add to GitHub repo
4. Add secrets (token + channel ID)
5. Bot runs automatically every 50 minutes
6. Messages appear in Discord with embeds and reactions
7. Users can type commands (!fact, !quote, etc.) during the 2-minute window

That's it. Simple, clean, effective. 🇨🇴
