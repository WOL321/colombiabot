# 🇨🇴 Colombia Pride Bot

<div align="center">

![Discord](https://img.shields.io/badge/Discord-Bot-7289DA?style=for-the-badge&logo=discord)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**A beautiful Discord bot that celebrates Colombia with pride and elegance**

*Yellow • Blue • Red*

</div>

---

## ✨ Features

- 🎨 **Premium Embeds** — Every message is wrapped in a stunning, modern Discord embed using official Colombian flag colors
- 🇨🇴 **Proud Messages** — Rotates between iconic Colombian phrases
- ⏰ **Natural Timing** — Messages appear at organic, unpredictable intervals (25-40 min gaps)
- 🔄 **Infinite Cycles** — Runs forever with automatic 5-hour rolling cycles
- 📊 **Stats & Ping** — Built-in commands to check bot health
- 🛡️ **Error Handling** — Robust logging and graceful error recovery

## 📸 Preview

```
┌─────────────────────────────────────────┐
│  ☀️ Golden Spirit                       │
│                                         │
│  ¡Viva Colombia!                        │
│                                         │
│  🇨🇴 República de Colombia    12:00 PM │
└─────────────────────────────────────────┘
```

The bot randomly uses three color themes:
- 🟡 **Yellow (#FCD116)** — Sovereignty & Justice
- 🔵 **Blue (#003893)** — Loyalty & Perseverance
- 🔴 **Red (#CE1126)** — Valor & Blood of Heroes

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
🇨🇴 Colombia Pride Bot is online and proud!
```

## 📋 Commands

| Command | Description |
|---------|-------------|
| `!ping` | Check if the bot is online and responsive |
| `!stats` | View bot statistics (messages sent, cycles, etc.) |
| `!help` | Show available commands |

## 🏗️ Project Structure

```
colombia-pride-bot/
├── bot.py              # Main bot logic
├── config.py           # Configuration management
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variable template
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## ⚙️ Configuration

All settings are in `config.py` and can be customized:

| Setting | Default | Description |
|---------|---------|-------------|
| `CYCLE_DURATION_HOURS` | 5 | Duration of each messaging cycle |
| `MIN_GAP_MINUTES` | 25 | Minimum time between messages |
| `MAX_GAP_MINUTES` | 40 | Maximum time between messages |
| `MESSAGES` | 3 phrases | Messages the bot rotates through |
| `FOOTERS` | 5 options | Elegant footer texts |

## 🔒 Security

- **Never** commit your `.env` file
- Keep your bot token private
- Use `.gitignore` to protect sensitive files

## 📝 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## 🇨🇴 Made with Love

Built with pride for Colombia. 

*¡Viva Colombia!* 🎉

---

<div align="center">

**Yellow • Blue • Red**

*We export more than just coffee.* ☕

</div>
