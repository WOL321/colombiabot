import { useState, useEffect } from 'react';

// Colombian flag colors
const COLORS = {
  yellow: '#FCD116',
  blue: '#003893',
  red: '#CE1126',
};

function App() {
  const [activeTab, setActiveTab] = useState<'bot' | 'config' | 'env'>('bot');
  const [currentColor, setCurrentColor] = useState(0);
  const [embedPreview, setEmbedPreview] = useState(0);

  const colors = [COLORS.yellow, COLORS.blue, COLORS.red];
  const messages = [
    '¡Viva Colombia!',
    'We export more than just coffee.',
    'Yellow. Blue. Red.',
  ];

  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentColor((prev) => (prev + 1) % 3);
    }, 3000);
    return () => clearInterval(interval);
  }, []);

  useEffect(() => {
    const interval = setInterval(() => {
      setEmbedPreview((prev) => (prev + 1) % 3);
    }, 4000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="min-h-screen bg-[#0a0a0f] text-white overflow-x-hidden">
      {/* Animated Background */}
      <div className="fixed inset-0 pointer-events-none">
        <div
          className="absolute top-0 left-1/4 w-96 h-96 rounded-full opacity-10 blur-3xl transition-colors duration-1000"
          style={{ backgroundColor: colors[currentColor] }}
        />
        <div
          className="absolute bottom-1/4 right-1/4 w-80 h-80 rounded-full opacity-8 blur-3xl transition-colors duration-1000"
          style={{ backgroundColor: colors[(currentColor + 1) % 3] }}
        />
        <div
          className="absolute top-1/2 left-1/2 w-64 h-64 rounded-full opacity-5 blur-3xl transition-colors duration-1000"
          style={{ backgroundColor: colors[(currentColor + 2) % 3] }}
        />
      </div>

      {/* Navigation */}
      <nav className="fixed top-0 left-0 right-0 z-50 backdrop-blur-xl bg-[#0a0a0f]/80 border-b border-white/5">
        <div className="max-w-7xl mx-auto px-6 py-4 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-8 h-8 rounded-lg flex items-center justify-center text-lg"
              style={{ background: `linear-gradient(135deg, ${COLORS.yellow}, ${COLORS.blue}, ${COLORS.red})` }}>
              🇨🇴
            </div>
            <span className="font-bold text-lg">Colombia Pride Bot</span>
          </div>
          <div className="hidden md:flex items-center gap-6 text-sm text-gray-400">
            <a href="#features" className="hover:text-white transition-colors">Features</a>
            <a href="#preview" className="hover:text-white transition-colors">Preview</a>
            <a href="#code" className="hover:text-white transition-colors">Code</a>
            <a href="#setup" className="hover:text-white transition-colors">Setup</a>
          </div>
          <a
            href="https://github.com"
            target="_blank"
            rel="noopener noreferrer"
            className="flex items-center gap-2 px-4 py-2 rounded-lg bg-white/5 hover:bg-white/10 border border-white/10 transition-all text-sm"
          >
            <i className="fab fa-github"></i>
            <span className="hidden sm:inline">GitHub</span>
          </a>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="relative pt-32 pb-20 px-6">
        {/* Hero Background Image */}
        <div className="absolute inset-0 overflow-hidden opacity-20">
          <img
            src="https://image.qwenlm.ai/generated-images/c0798cca-579b-4f32-b16f-2b133c1742e3/_result.png"
            alt=""
            className="w-full h-full object-cover"
          />
          <div className="absolute inset-0 bg-gradient-to-b from-[#0a0a0f] via-transparent to-[#0a0a0f]" />
        </div>

        <div className="max-w-5xl mx-auto text-center relative z-10">
          {/* Flag Stripe */}
          <div className="flex justify-center mb-8">
            <div className="flex rounded-full overflow-hidden shadow-2xl" style={{ boxShadow: `0 0 60px ${colors[currentColor]}30` }}>
              <div className="w-16 h-2" style={{ backgroundColor: COLORS.yellow }} />
              <div className="w-16 h-2" style={{ backgroundColor: COLORS.blue }} />
              <div className="w-16 h-2" style={{ backgroundColor: COLORS.red }} />
            </div>
          </div>

          <h1 className="text-5xl md:text-7xl font-black mb-6 leading-tight">
            <span className="bg-clip-text text-transparent" style={{
              backgroundImage: `linear-gradient(135deg, ${COLORS.yellow}, ${COLORS.blue}, ${COLORS.red})`
            }}>
              Colombia Pride
            </span>
            <br />
            <span className="text-white/90">Discord Bot</span>
          </h1>

          <p className="text-xl text-gray-400 max-w-2xl mx-auto mb-10 leading-relaxed">
            A beautiful, production-ready Discord bot that celebrates Colombia with
            premium embeds, natural timing, and elegant design.
          </p>

          {/* Live Embed Preview */}
          <div className="max-w-md mx-auto mb-12">
            <DiscordEmbed
              message={messages[embedPreview]}
              color={colors[embedPreview]}
              index={embedPreview}
            />
          </div>

          {/* CTA Buttons */}
          <div className="flex flex-wrap justify-center gap-4">
            <a
              href="#setup"
              className="px-8 py-3 rounded-xl font-semibold text-black transition-all hover:scale-105 hover:shadow-lg"
              style={{ backgroundColor: COLORS.yellow }}
            >
              <i className="fas fa-rocket mr-2"></i>
              Get Started
            </a>
            <a
              href="#code"
              className="px-8 py-3 rounded-xl font-semibold text-white bg-white/5 border border-white/10 hover:bg-white/10 transition-all hover:scale-105"
            >
              <i className="fas fa-code mr-2"></i>
              View Source
            </a>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section id="features" className="py-20 px-6">
        <div className="max-w-6xl mx-auto">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold mb-4">✨ Features</h2>
            <p className="text-gray-400 text-lg">Everything you need for a proud, elegant bot</p>
          </div>

          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
            <FeatureCard
              icon="🎨"
              title="Premium Embeds"
              description="Every message wrapped in a stunning Discord embed with official Colombian flag colors."
              color={COLORS.yellow}
            />
            <FeatureCard
              icon="⏰"
              title="Natural Timing"
              description="Messages appear at organic, unpredictable intervals (25-40 min gaps) — never spammy."
              color={COLORS.blue}
            />
            <FeatureCard
              icon="🔄"
              title="Infinite Cycles"
              description="5-hour rolling cycles that automatically restart. Runs forever without intervention."
              color={COLORS.red}
            />
            <FeatureCard
              icon="📊"
              title="Built-in Commands"
              description="Ping, stats, and help commands with beautiful embeds to check bot health."
              color={COLORS.yellow}
            />
            <FeatureCard
              icon="🛡️"
              title="Error Handling"
              description="Robust logging, graceful error recovery, and clean configuration validation."
              color={COLORS.blue}
            />
            <FeatureCard
              icon="🇨🇴"
              title="Proud Identity"
              description="Every detail celebrates Colombia — from colors to footers to the bot's personality."
              color={COLORS.red}
            />
          </div>
        </div>
      </section>

      {/* Preview Section */}
      <section id="preview" className="py-20 px-6">
        <div className="max-w-4xl mx-auto">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold mb-4">👀 Live Preview</h2>
            <p className="text-gray-400 text-lg">See what the bot looks like in Discord</p>
          </div>

          <div className="bg-[#2b2d31] rounded-2xl p-6 shadow-2xl border border-white/5">
            {/* Discord Header */}
            <div className="flex items-center gap-3 pb-4 mb-6 border-b border-white/10">
              <div className="w-10 h-10 rounded-full flex items-center justify-center text-xl"
                style={{ background: `linear-gradient(135deg, ${COLORS.yellow}, ${COLORS.red})` }}>
                🇨🇴
              </div>
              <div>
                <div className="font-semibold text-white">Colombia Pride Bot</div>
                <div className="text-xs text-green-400">● Online</div>
              </div>
            </div>

            {/* Messages */}
            <div className="space-y-6">
              <DiscordEmbed message="¡Viva Colombia!" color={COLORS.yellow} index={0} />
              <DiscordEmbed message="We export more than just coffee." color={COLORS.blue} index={1} />
              <DiscordEmbed message="Yellow. Blue. Red." color={COLORS.red} index={2} />
            </div>
          </div>
        </div>
      </section>

      {/* Code Section */}
      <section id="code" className="py-20 px-6">
        <div className="max-w-5xl mx-auto">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold mb-4">💻 Source Code</h2>
            <p className="text-gray-400 text-lg">Clean, well-structured, and ready for production</p>
          </div>

          {/* Tab Navigation */}
          <div className="flex gap-2 mb-4">
            <button
              onClick={() => setActiveTab('bot')}
              className={`px-4 py-2 rounded-lg text-sm font-medium transition-all ${
                activeTab === 'bot'
                  ? 'bg-white/10 text-white border border-white/20'
                  : 'text-gray-400 hover:text-white hover:bg-white/5'
              }`}
            >
              <i className="fas fa-robot mr-2"></i>bot.py
            </button>
            <button
              onClick={() => setActiveTab('config')}
              className={`px-4 py-2 rounded-lg text-sm font-medium transition-all ${
                activeTab === 'config'
                  ? 'bg-white/10 text-white border border-white/20'
                  : 'text-gray-400 hover:text-white hover:bg-white/5'
              }`}
            >
              <i className="fas fa-cog mr-2"></i>config.py
            </button>
            <button
              onClick={() => setActiveTab('env')}
              className={`px-4 py-2 rounded-lg text-sm font-medium transition-all ${
                activeTab === 'env'
                  ? 'bg-white/10 text-white border border-white/20'
                  : 'text-gray-400 hover:text-white hover:bg-white/5'
              }`}
            >
              <i className="fas fa-key mr-2"></i>.env.example
            </button>
          </div>

          {/* Code Display */}
          <div className="bg-[#1a1b26] rounded-2xl border border-white/5 overflow-hidden">
            <div className="flex items-center justify-between px-4 py-3 bg-[#16161e] border-b border-white/5">
              <div className="flex items-center gap-2">
                <div className="w-3 h-3 rounded-full bg-red-500/80" />
                <div className="w-3 h-3 rounded-full bg-yellow-500/80" />
                <div className="w-3 h-3 rounded-full bg-green-500/80" />
              </div>
              <span className="text-xs text-gray-500 font-mono">
                {activeTab === 'bot' ? 'bot.py' : activeTab === 'config' ? 'config.py' : '.env.example'}
              </span>
            </div>
            <div className="p-6 overflow-x-auto">
              <pre className="text-sm font-mono leading-relaxed text-gray-300">
                <code>{activeTab === 'bot' ? BOT_CODE : activeTab === 'config' ? CONFIG_CODE : ENV_CODE}</code>
              </pre>
            </div>
          </div>
        </div>
      </section>

      {/* Setup Section */}
      <section id="setup" className="py-20 px-6">
        <div className="max-w-4xl mx-auto">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold mb-4">🚀 Quick Setup</h2>
            <p className="text-gray-400 text-lg">Get running in under 5 minutes</p>
          </div>

          <div className="space-y-6">
            <SetupStep
              number={1}
              title="Clone & Install"
              code={`git clone https://github.com/yourusername/colombia-pride-bot.git
cd colombia-pride-bot
python -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate
pip install -r requirements.txt`}
            />
            <SetupStep
              number={2}
              title="Configure Environment"
              code={`cp .env.example .env
# Edit .env with your bot token and channel ID`}
            />
            <SetupStep
              number={3}
              title="Run the Bot"
              code={`python bot.py`}
            />
          </div>

          {/* Commands Table */}
          <div className="mt-16">
            <h3 className="text-xl font-bold mb-6 text-center">📋 Commands</h3>
            <div className="bg-[#1a1b26] rounded-2xl border border-white/5 overflow-hidden">
              <table className="w-full text-left">
                <thead>
                  <tr className="border-b border-white/5">
                    <th className="px-6 py-4 text-sm font-semibold text-gray-300">Command</th>
                    <th className="px-6 py-4 text-sm font-semibold text-gray-300">Description</th>
                  </tr>
                </thead>
                <tbody>
                  <tr className="border-b border-white/5">
                    <td className="px-6 py-4 font-mono text-sm" style={{ color: COLORS.yellow }}>!ping</td>
                    <td className="px-6 py-4 text-sm text-gray-400">Check if the bot is online and responsive</td>
                  </tr>
                  <tr className="border-b border-white/5">
                    <td className="px-6 py-4 font-mono text-sm" style={{ color: COLORS.blue }}>!stats</td>
                    <td className="px-6 py-4 text-sm text-gray-400">View bot statistics (messages, cycles, servers)</td>
                  </tr>
                  <tr>
                    <td className="px-6 py-4 font-mono text-sm" style={{ color: COLORS.red }}>!help</td>
                    <td className="px-6 py-4 text-sm text-gray-400">Show available commands</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </section>

      {/* Project Structure */}
      <section className="py-20 px-6">
        <div className="max-w-4xl mx-auto">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold mb-4">📁 Project Structure</h2>
            <p className="text-gray-400 text-lg">Clean, organized, and GitHub-ready</p>
          </div>

          <div className="bg-[#1a1b26] rounded-2xl border border-white/5 p-8 font-mono text-sm">
            <div className="space-y-1">
              <div className="text-yellow-400">colombia-pride-bot/</div>
              <div className="pl-4 text-gray-300">├── <span className="text-green-400">bot.py</span>          <span className="text-gray-500"># Main bot logic</span></div>
              <div className="pl-4 text-gray-300">├── <span className="text-blue-400">config.py</span>       <span className="text-gray-500"># Configuration management</span></div>
              <div className="pl-4 text-gray-300">├── <span className="text-purple-400">requirements.txt</span> <span className="text-gray-500"># Python dependencies</span></div>
              <div className="pl-4 text-gray-300">├── <span className="text-red-400">.env.example</span>    <span className="text-gray-500"># Environment template</span></div>
              <div className="pl-4 text-gray-300">├── <span className="text-gray-400">.gitignore</span>       <span className="text-gray-500"># Git ignore rules</span></div>
              <div className="pl-4 text-gray-300">└── <span className="text-white">README.md</span>        <span className="text-gray-500"># Documentation</span></div>
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="py-12 px-6 border-t border-white/5">
        <div className="max-w-5xl mx-auto text-center">
          {/* Flag Stripe */}
          <div className="flex justify-center mb-6">
            <div className="flex rounded-full overflow-hidden">
              <div className="w-12 h-1.5" style={{ backgroundColor: COLORS.yellow }} />
              <div className="w-12 h-1.5" style={{ backgroundColor: COLORS.blue }} />
              <div className="w-12 h-1.5" style={{ backgroundColor: COLORS.red }} />
            </div>
          </div>
          <p className="text-gray-400 mb-2">
            Made with 🇨🇴 pride for Colombia
          </p>
          <p className="text-gray-600 text-sm">
            Yellow • Blue • Red — We export more than just coffee ☕
          </p>
        </div>
      </footer>
    </div>
  );
}

// ─── Components ──────────────────────────────────────────────────────────────

function FeatureCard({ icon, title, description, color }: {
  icon: string;
  title: string;
  description: string;
  color: string;
}) {
  return (
    <div className="group p-6 rounded-2xl bg-white/[0.02] border border-white/5 hover:border-white/10 transition-all hover:bg-white/[0.04] hover:-translate-y-1">
      <div className="w-12 h-12 rounded-xl flex items-center justify-center text-2xl mb-4 transition-transform group-hover:scale-110"
        style={{ backgroundColor: `${color}15`, boxShadow: `0 0 20px ${color}10` }}>
        {icon}
      </div>
      <h3 className="text-lg font-semibold mb-2">{title}</h3>
      <p className="text-gray-400 text-sm leading-relaxed">{description}</p>
    </div>
  );
}

function DiscordEmbed({ message, color, index }: {
  message: string;
  color: string;
  index: number;
}) {
  const authors = ['☀️ Golden Spirit', '🌊 Deep Blue Ocean', '🌹 Passionate Red'];
  const footers = ['🇨🇴 República de Colombia', '🇨🇴 Orgullo Colombiano', '🇨🇴 Tierra de mil colores'];

  return (
    <div className="bg-[#2b2d31] rounded-lg p-4 border-l-4 max-w-sm" style={{ borderLeftColor: color }}>
      <div className="flex items-center gap-2 mb-2">
        <div className="w-6 h-6 rounded-full flex items-center justify-center text-xs"
          style={{ background: `linear-gradient(135deg, ${COLORS.yellow}, ${COLORS.red})` }}>
          🇨🇴
        </div>
        <span className="text-sm font-semibold text-white">Colombia Pride Bot</span>
        <span className="text-xs text-gray-500 ml-auto">Today at 12:00 PM</span>
      </div>
      <div className="ml-8">
        <div className="text-xs font-semibold mb-1" style={{ color }}>{authors[index]}</div>
        <div className="bg-[#1e1f22] rounded-lg p-3 border-l-2" style={{ borderLeftColor: color }}>
          <p className="text-white text-sm font-medium">{message}</p>
        </div>
        <div className="text-xs text-gray-500 mt-2">{footers[index]}</div>
      </div>
    </div>
  );
}

function SetupStep({ number, title, code }: {
  number: number;
  title: string;
  code: string;
}) {
  return (
    <div className="flex gap-4">
      <div className="flex-shrink-0 w-10 h-10 rounded-full flex items-center justify-center font-bold text-sm"
        style={{
          background: `linear-gradient(135deg, ${COLORS.yellow}, ${COLORS.blue})`,
          color: '#000'
        }}>
        {number}
      </div>
      <div className="flex-1">
        <h3 className="text-lg font-semibold mb-2">{title}</h3>
        <div className="bg-[#1a1b26] rounded-xl p-4 border border-white/5 overflow-x-auto">
          <pre className="text-sm font-mono text-gray-300 whitespace-pre-wrap">{code}</pre>
        </div>
      </div>
    </div>
  );
}

// ─── Code Snippets ───────────────────────────────────────────────────────────

const BOT_CODE = `"""
🇨🇴 Colombia Pride Bot
A beautiful Discord bot that celebrates Colombia with style.
"""

import os, sys, random, asyncio, logging
from datetime import datetime
import discord
from discord.ext import commands
from config import *

# Logging Setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger("colombia_bot")

# Bot Setup
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents,
    description="🇨🇴 Celebrating Colombia with pride",
)

def create_pride_embed(message: str) -> discord.Embed:
    """Creates a beautiful embed with Colombian flag colors."""
    color = random.choice(EMBED_COLORS)
    footer = random.choice(FOOTERS)
    
    embed = discord.Embed(
        description=message,
        color=color,
        timestamp=datetime.utcnow(),
    )
    embed.set_footer(text=footer)
    
    if color == discord.Color.from_hex("#FCD116"):
        embed.set_author(name="☀️ Golden Spirit")
    elif color == discord.Color.from_hex("#003893"):
        embed.set_author(name="🌊 Deep Blue Ocean")
    else:
        embed.set_author(name="🌹 Passionate Red")
    
    return embed

async def send_cycle_messages():
    """Main cycle loop with natural timing."""
    channel = bot.get_channel(CHANNEL_ID)
    if not channel:
        channel = await bot.fetch_channel(CHANNEL_ID)
    
    messages_this_cycle = random.randint(7, 12)
    
    for i in range(messages_this_cycle):
        message = random.choice(MESSAGES)
        embed = create_pride_embed(message)
        await channel.send(embed=embed)
        
        if i < messages_this_cycle - 1:
            delay = random.uniform(25, 40) * 60
            jitter = random.uniform(-2, 2) * 60
            await asyncio.sleep(delay + jitter)
    
    await asyncio.sleep(30)
    await send_cycle_messages()

@bot.event
async def on_ready():
    logger.info(f"🇨🇴 {bot.user.name} is online!")
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="over Colombia 🇨🇴",
        )
    )
    bot.loop.create_task(send_cycle_messages())

@bot.command(name="ping")
async def ping(ctx):
    latency = round(bot.latency * 1000)
    embed = discord.Embed(
        title="🇨🇴 Colombia Pride Bot",
        description="¡Estoy vivo y orgulloso!",
        color=random.choice(EMBED_COLORS),
    )
    embed.add_field(name="⚡ Latency", value=f"{latency}ms")
    embed.set_footer(text="🇨🇴 República de Colombia")
    await ctx.send(embed=embed)

bot.run(BOT_TOKEN)`;

const CONFIG_CODE = `"""
🇨🇴 Colombia Pride Bot - Configuration
All configurable settings in one clean place.
"""

import os
import discord
from dotenv import load_dotenv

load_dotenv()

# ─── Discord Configuration ───────────────────────

BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN", "")
CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID", "0"))

# ─── Colombian Flag Colors ───────────────────────
# Official colors (Ley 12 de 1967)

EMBED_COLORS = [
    discord.Color.from_hex("#FCD116"),  # Yellow
    discord.Color.from_hex("#003893"),  # Blue
    discord.Color.from_hex("#CE1126"),  # Red
]

# ─── Messages ────────────────────────────────────

MESSAGES = [
    "¡Viva Colombia!",
    "We export more than just coffee.",
    "Yellow. Blue. Red.",
]

# ─── Timing ──────────────────────────────────────

CYCLE_DURATION_HOURS = 5
MIN_GAP_MINUTES = 25
MAX_GAP_MINUTES = 40

# ─── Footers ─────────────────────────────────────

FOOTERS = [
    "🇨🇴 República de Colombia",
    "🇨🇴 Orgullo Colombiano",
    "🇨🇴 Hecho con amor en Colombia",
    "🇨🇴 Tierra de mil colores",
    "🇨🇴 El riesgo es que te quieras quedar",
]

def validate_config() -> bool:
    """Validate required configuration."""
    if not BOT_TOKEN:
        print("❌ DISCORD_BOT_TOKEN is not set")
        return False
    if not CHANNEL_ID:
        print("❌ DISCORD_CHANNEL_ID is not set")
        return False
    return True`;

const ENV_CODE = `# 🇨🇴 Colombia Pride Bot - Environment Configuration
# Copy this file to .env and fill in your values
# DO NOT commit your actual .env file to git!

# Your Discord bot token
# Get one at: https://discord.com/developers/applications
DISCORD_BOT_TOKEN=your_bot_token_here

# The channel ID where the bot will send messages
# Right-click a channel in Discord → Copy ID
DISCORD_CHANNEL_ID=your_channel_id_here`;

export default App;
