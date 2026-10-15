# 🇨🇴 Colombia Pride Bot

<div align="center">

![Discord](https://img.shields.io/badge/Discord-Bot-7289DA?style=for-the-badge&logo=discord)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**A beautiful Discord bot that celebrates Colombia with pride, emoji reactions, and holiday detection**

*Yellow • Blue • Red*

</div>

---

## ✨ Features

### 🎨 Premium Embeds
Every message is wrapped in a stunning, modern Discord embed using official Colombian flag colors.

### 🎉 Holiday Detection
The bot automatically detects Colombian holidays and sends **special celebration embeds** with extra reactions!

Supported holidays:
- 🎆 New Year's Day (Jan 1)
- 💪 Labor Day (May 1)
- 🇨🇴 Independence Day (Jul 20)
- ⚔️ Battle of Boyacá (Aug 7)
- 🌎 Día de la Raza (Oct 12)
- 🏰 Cartagena Independence (Nov 11)
- 🕯️ Día de las Velitas (Dec 7)
- ⭐ Inmaculada Concepción (Dec 8)
- 🎄 Christmas (Dec 25)

### 💬 Emoji Variations
**24+ unique emoji combinations** keep every message fresh and visually diverse. Each of the 3 base messages has 8 different emoji variations!

### 🎯 Auto Emoji Reactions
Every message gets **3-5 random Colombian emoji reactions** automatically:
🇨🇴 💛 💙 ❤️ ☕ 🌺 🎉 ✨ 🌟 🏔️ 🦜 🌊

On holidays, the bot adds **5-7 reactions** with the flag guaranteed!

### ⏰ Natural Timing
Messages appear at organic, unpredictable intervals (25-40 min gaps) — never spammy.

### 🔄 Infinite Cycles
5-hour rolling cycles that automatically restart. Runs forever without intervention.

### 📊 Built-in Commands
- `!ping` — Check bot status with holiday info
- `!stats` — View detailed statistics
- `!holidays` — See Colombian holidays calendar
- `!help` — Show all commands

## 📸 Preview

```
┌─────────────────────────────────────────┐
│  🇨🇴 Colombia Pride Bot    🎉 Holiday   │
│                                         │
│  ☀️ Golden Spirit                       │
│  ┌─────────────────────────────────┐    │
│  │ 🇨🇴🎆 ¡200+ años de libertad!  │    │
│  │    ¡Viva Colombia! 🎆🇨🇴        │    │
│  │                                 │    │
│  │ *Special Holiday Edition*       │    │
│  └─────────────────────────────────┘    │
│                                         │
│  Reactions: 🇨🇴 💛 💙 ❤️ 🎉 ✨ 🏔️     │
│                                         │
│  🇨🇴 ¡Celebrando con orgullo!          │
└─────────────────────────────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or higher
- A Discord bot token ([Get one here](https://discord.com/developers/applications))

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/colombia-pride-bot.git
cd colombia-pride-bot

# Create a virtual environment
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Configuration

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your credentials
nano .env  # or use your preferred editor
```

Fill in your `.env` file:
```env
DISCORD_BOT_TOKEN=your_actual_bot_token
DISCORD_CHANNEL_ID=your_target_channel_id
```

### Running the Bot

```bash
python bot.py
```

You should see:
```
🚀 Starting Colombia Pride Bot...
   Features: Holiday Detection | Emoji Variations | Auto Reactions
🇨🇴 Colombia Pride Bot is online and proud!
```

## 🌩️ Cloud Deployment (No Local Setup)

### Discloud (Recommended for beginners)
1. Go to [discloud.app](https://discloud.app)
2. Sign up and upload a ZIP of the bot folder
3. Set env variables in their dashboard
4. Deploy — done!

### Railway
1. Push to GitHub
2. Deploy from repo on [railway.app](https://railway.app)
3. Add env variables
4. Set start command: `python bot.py`

## 📋 Commands

| Command | Description |
|---------|-------------|
| `!ping` | Check if the bot is online (shows holiday status) |
| `!stats` | View bot statistics (messages, cycles, holidays) |
| `!holidays` | See Colombian holidays the bot celebrates |
| `!help` | Show available commands |

## 🏗️ Project Structure

```
colombia-pride-bot/
├── bot.py              # Main bot logic with all features
├── config.py           # Configuration, holidays, emojis
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variable template
├── .gitignore          # Git ignore rules
├── README.md           # This file
└── LICENSE             # MIT License
```

## ⚙️ Configuration

All settings are in `config.py` and can be customized:

| Setting | Default | Description |
|---------|---------|-------------|
| `CYCLE_DURATION_HOURS` | 5 | Duration of each messaging cycle |
| `MIN_GAP_MINUTES` | 25 | Minimum time between messages |
| `MAX_GAP_MINUTES` | 40 | Maximum time between messages |
| `MIN_REACTIONS` | 3 | Minimum emoji reactions per message |
| `MAX_REACTIONS` | 5 | Maximum emoji reactions per message |
| `EMOJI_VARIATIONS` | 24 combos | Emoji variations per message |
| `COLOMBIAN_HOLIDAYS` | 15 dates | Holiday detection calendar |

## 🔒 Security

- **Never** commit your `.env` file
- Keep your bot token private
- Use `.gitignore` to protect sensitive files

## 📝 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## 🇨🇴 Made with Love

Built with pride for Colombia. Features include holiday detection, 24+ emoji variations, and automatic Colombian emoji reactions on every message.

*¡Viva Colombia!* 🎉

---

<div align="center">

**Yellow • Blue • Red**

*We export more than just coffee.* ☕

</div>
