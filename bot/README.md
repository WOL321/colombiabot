# 🇨🇴 Colombia Pride Bot

A simple, elegant Discord bot that celebrates Colombia with pride.

## What it does

Posts these 6 messages at random intervals:

- Que viva Colombia!
- Yellow. Blue. Red.
- We export more than just coffee ;)
- Colombia needs no explanation.
- The tricolor still means something.
- From the Caribbean to the Amazon.

Each message appears as a beautiful embed using the official Colombian flag colors (yellow, blue, red) with emoji reactions.

## Features

- **Clean embeds** with Colombian flag colors
- **Interactive polls** — yes/no questions in a separate channel (optional)
- **Natural timing** — messages every 25-40 minutes
- **Emoji reactions** — 🇨🇴 💛 💙 ❤️
- **Simple command** — `!ping` to check status
- **Free hosting** — runs on GitHub Actions

## Setup

### 1. Create Discord Bot

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application" → name it "Colombia Pride Bot"
3. Go to "Bot" tab → "Reset Token" → copy the token
4. Enable "Message Content Intent" under Privileged Gateway Intents
5. Go to "OAuth2" → "URL Generator"
6. Select scopes: `bot`, `applications.commands`
7. Select permissions: Send Messages, Embed Links, Add Reactions, Read Message History
8. Copy the generated URL and invite the bot to your server

### 2. Get Channel IDs

1. In Discord, enable Developer Mode (User Settings → Advanced)
2. Right-click the channel where you want pride messages → "Copy Channel ID"
3. (Optional) Right-click a different channel for polls → "Copy Channel ID"

### 3. Deploy to GitHub

1. Create a new GitHub repository
2. Upload all files from the `bot/` folder
3. Go to Settings → Secrets and variables → Actions
4. Add secrets:
   - `DISCORD_BOT_TOKEN` = your bot token
   - `DISCORD_CHANNEL_ID` = your pride messages channel ID
   - `DISCORD_POLL_CHANNEL_ID` = (optional) your polls channel ID
5. The bot will run automatically every 50 minutes

## Commands

- `!ping` — Check if the bot is online

## How it works

The bot runs on GitHub Actions:
- Stays online for 2 minutes every 50 minutes
- Posts a random pride message or poll
- 70% chance: pride message with emoji reactions
- 30% chance: yes/no poll (if poll channel is configured)
- Uses ~1,500 minutes/month (under GitHub's 2,000 limit)

## Files

```
bot/
├── bot.py              # Local version (runs continuously)
├── bot_github.py       # GitHub Actions version (2-minute sessions)
├── config.py           # Messages, colors, timing
├── requirements.txt    # Dependencies
├── .env.example        # Environment template
└── .github/workflows/
    └── keep-alive.yml  # GitHub Actions workflow
```

## License

MIT

---

Made with 🇨🇴 for Colombia
