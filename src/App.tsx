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
              icon="🎉"
              title="Holiday Detection"
              description="Special celebration embeds on Colombian holidays — July 20, Christmas, Día de las Velitas, and more!"
              color={COLORS.red}
            />
            <FeatureCard
              icon="💬"
              title="Emoji Variations"
              description="24+ unique emoji combinations keep every message fresh and visually diverse."
              color={COLORS.blue}
            />
            <FeatureCard
              icon="🇨🇴"
              title="Auto Reactions"
              description="Bot reacts with 3-5 random Colombian emojis (🇨🇴 ☕ 🌺 🎉) after every message!"
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
              description="Ping, stats, holidays, and help commands with beautiful embeds to check bot health."
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
            <h2 className="text-3xl md:text-4xl font-bold mb-4">👀 Command Previews</h2>
            <p className="text-gray-400 text-lg">See what every command looks like in Discord</p>
          </div>

          {/* Regular Messages */}
          <div className="mb-12">
            <h3 className="text-xl font-bold mb-4">📝 Auto Messages</h3>
            <div className="bg-[#2b2d31] rounded-2xl p-6 shadow-2xl border border-white/5">
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
              <div className="space-y-6">
                <DiscordEmbed message="🇨🇴 ¡Viva Colombia! 🇨🇴" color={COLORS.yellow} index={0} reactions={["🇨🇴", "💛", "☕", "✨"]} />
                <DiscordEmbed message="☕ Colombian coffee: liquid gold in a cup. ✨" color={COLORS.blue} index={1} reactions={["💙", "☕", "🌺", "🌟"]} />
                <DiscordEmbed message="🦜 Biodiversity? Colombia has 10% of ALL species on Earth. 🌺" color={COLORS.red} index={2} reactions={["❤️", "🇨🇴", "🎉", "🏔️"]} />
              </div>
            </div>
          </div>

          {/* !fact Command */}
          <div className="mb-12">
            <h3 className="text-xl font-bold mb-4">💡 <code className="text-yellow-400">!fact</code> Command</h3>
            <div className="bg-[#2b2d31] rounded-2xl p-6 shadow-2xl border border-white/5">
              <div className="space-y-4">
                <div className="flex items-center gap-2 text-sm text-gray-400">
                  <span className="text-white font-semibold">You:</span>
                  <span className="bg-[#383a40] px-2 py-1 rounded">!fact</span>
                </div>
                <div className="bg-[#2b2d31] rounded-lg p-4 border-l-4" style={{ borderLeftColor: COLORS.yellow }}>
                  <div className="flex items-center gap-2 mb-2">
                    <div className="w-6 h-6 rounded-full flex items-center justify-center text-xs"
                      style={{ background: `linear-gradient(135deg, ${COLORS.yellow}, ${COLORS.red})` }}>
                      🇨🇴
                    </div>
                    <span className="text-sm font-semibold text-white">Colombia Pride Bot</span>
                  </div>
                  <div className="ml-8">
                    <div className="text-xs font-semibold mb-2" style={{ color: COLORS.yellow }}>🦜 Did You Know?</div>
                    <div className="bg-[#1e1f22] rounded-lg p-3 border-l-2" style={{ borderLeftColor: COLORS.yellow }}>
                      <p className="text-white text-sm">Colombia has more bird species than any other country — over 1,900!</p>
                    </div>
                    <div className="text-xs text-gray-500 mt-2">🇨🇴 Fun Colombian Facts</div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* !squad Command */}
          <div className="mb-12">
            <h3 className="text-xl font-bold mb-4">⚽ <code className="text-yellow-400">!squad</code> Command</h3>
            <div className="bg-[#2b2d31] rounded-2xl p-6 shadow-2xl border border-white/5">
              <div className="space-y-4">
                <div className="flex items-center gap-2 text-sm text-gray-400">
                  <span className="text-white font-semibold">You:</span>
                  <span className="bg-[#383a40] px-2 py-1 rounded">!squad</span>
                </div>
                <div className="bg-[#2b2d31] rounded-lg p-4 border-l-4" style={{ borderLeftColor: COLORS.yellow }}>
                  <div className="flex items-center gap-2 mb-2">
                    <div className="w-6 h-6 rounded-full flex items-center justify-center text-xs"
                      style={{ background: `linear-gradient(135deg, ${COLORS.yellow}, ${COLORS.red})` }}>
                      🇨🇴
                    </div>
                    <span className="text-sm font-semibold text-white">Colombia Pride Bot</span>
                  </div>
                  <div className="ml-8">
                    <div className="text-xs font-semibold mb-2" style={{ color: COLORS.yellow }}>🇨🇴 Colombia 2026 World Cup Squad</div>
                    <div className="bg-[#1e1f22] rounded-lg p-3 border-l-2" style={{ borderLeftColor: COLORS.yellow }}>
                      <p className="text-gray-400 text-xs mb-2">Manager: Néstor Lorenzo | Captain: James Rodríguez</p>
                      <p className="text-white text-xs font-semibold mb-1">Forwards:</p>
                      <p className="text-gray-300 text-xs">• Luis Díaz ⭐ (Bayern Munich)</p>
                      <p className="text-gray-300 text-xs">• Jhon Córdoba (Krasnodar)</p>
                      <p className="text-gray-300 text-xs">• Jhon Arias (Wolverhampton)</p>
                      <p className="text-white text-xs font-semibold mb-1 mt-2">Midfielders:</p>
                      <p className="text-gray-300 text-xs">• James Rodríguez ⭐ (Minnesota United)</p>
                      <p className="text-gray-300 text-xs">• Richard Ríos (Benfica)</p>
                      <p className="text-gray-300 text-xs">• Jefferson Lerma (Crystal Palace)</p>
                    </div>
                    <div className="text-xs text-gray-500 mt-2">🇨🇴 ¡Vamos Colombia! ⚽</div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* !quote Command */}
          <div className="mb-12">
            <h3 className="text-xl font-bold mb-4">💭 <code className="text-yellow-400">!quote</code> Command</h3>
            <div className="bg-[#2b2d31] rounded-2xl p-6 shadow-2xl border border-white/5">
              <div className="space-y-4">
                <div className="flex items-center gap-2 text-sm text-gray-400">
                  <span className="text-white font-semibold">You:</span>
                  <span className="bg-[#383a40] px-2 py-1 rounded">!quote</span>
                </div>
                <div className="bg-[#2b2d31] rounded-lg p-4 border-l-4" style={{ borderLeftColor: COLORS.blue }}>
                  <div className="flex items-center gap-2 mb-2">
                    <div className="w-6 h-6 rounded-full flex items-center justify-center text-xs"
                      style={{ background: `linear-gradient(135deg, ${COLORS.yellow}, ${COLORS.red})` }}>
                      🇨🇴
                    </div>
                    <span className="text-sm font-semibold text-white">Colombia Pride Bot</span>
                  </div>
                  <div className="ml-8">
                    <div className="text-xs font-semibold mb-2" style={{ color: COLORS.blue }}>💭 Colombian Wisdom</div>
                    <div className="bg-[#1e1f22] rounded-lg p-3 border-l-2" style={{ borderLeftColor: COLORS.blue }}>
                      <p className="text-white text-sm italic">"Life is not what one lived, but what one remembers."</p>
                    </div>
                    <div className="text-xs text-gray-500 mt-2">— Gabriel García Márquez 🇨🇴</div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* !flag Command */}
          <div className="mb-12">
            <h3 className="text-xl font-bold mb-4">🏳️ <code className="text-yellow-400">!flag</code> Command</h3>
            <div className="bg-[#2b2d31] rounded-2xl p-6 shadow-2xl border border-white/5">
              <div className="space-y-4">
                <div className="flex items-center gap-2 text-sm text-gray-400">
                  <span className="text-white font-semibold">You:</span>
                  <span className="bg-[#383a40] px-2 py-1 rounded">!flag</span>
                </div>
                <div className="bg-[#2b2d31] rounded-lg p-4 border-l-4" style={{ borderLeftColor: COLORS.yellow }}>
                  <div className="flex items-center gap-2 mb-2">
                    <div className="w-6 h-6 rounded-full flex items-center justify-center text-xs"
                      style={{ background: `linear-gradient(135deg, ${COLORS.yellow}, ${COLORS.red})` }}>
                      🇨🇴
                    </div>
                    <span className="text-sm font-semibold text-white">Colombia Pride Bot</span>
                  </div>
                  <div className="ml-8">
                    <div className="text-xs font-semibold mb-2" style={{ color: COLORS.yellow }}>🇨🇴 The Colombian Flag</div>
                    <div className="bg-[#1e1f22] rounded-lg p-3 border-l-2" style={{ borderLeftColor: COLORS.yellow }}>
                      <p className="text-gray-300 text-xs mb-2">The national flag symbolizes sovereignty, honor, and bravery.</p>
                      <p className="text-xs"><span style={{ color: COLORS.yellow }}>💛 Yellow:</span> <span className="text-gray-300">Sovereignty & justice</span></p>
                      <p className="text-xs"><span style={{ color: COLORS.blue }}>💙 Blue:</span> <span className="text-gray-300">Seas & loyalty</span></p>
                      <p className="text-xs"><span style={{ color: COLORS.red }}>❤️ Red:</span> <span className="text-gray-300">Blood of heroes</span></p>
                    </div>
                    <div className="text-xs text-gray-500 mt-2">🇨🇴 Ley 12 de 1967</div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Slash Commands - Kingdom Data */}
          <div className="mb-12">
            <h3 className="text-xl font-bold mb-4">🎮 <code className="text-yellow-400">/kingdom</code> Slash Command</h3>
            <p className="text-gray-400 text-sm mb-4">Connected to <a href="https://colombiadmc.site" className="text-yellow-400 hover:underline" target="_blank" rel="noopener noreferrer">colombiadmc.site</a> — your Minecraft kingdom!</p>
            <div className="bg-[#2b2d31] rounded-2xl p-6 shadow-2xl border border-white/5">
              <div className="space-y-4">
                <div className="flex items-center gap-2 text-sm text-gray-400">
                  <span className="text-white font-semibold">You:</span>
                  <span className="bg-[#383a40] px-2 py-1 rounded">/kingdom</span>
                </div>
                <div className="bg-[#2b2d31] rounded-lg p-4 border-l-4" style={{ borderLeftColor: COLORS.yellow }}>
                  <div className="flex items-center gap-2 mb-2">
                    <div className="w-6 h-6 rounded-full flex items-center justify-center text-xs"
                      style={{ background: `linear-gradient(135deg, ${COLORS.yellow}, ${COLORS.red})` }}>
                      🇨🇴
                    </div>
                    <span className="text-sm font-semibold text-white">Colombia Pride Bot</span>
                  </div>
                  <div className="ml-8">
                    <div className="text-xs font-semibold mb-2" style={{ color: COLORS.yellow }}>📊 Kingdom Statistics</div>
                    <div className="bg-[#1e1f22] rounded-lg p-3 border-l-2" style={{ borderLeftColor: COLORS.yellow }}>
                      <p className="text-gray-400 text-xs mb-2">Reino de Colombia · DiplomaticaMC</p>
                      <p className="text-xs"><span className="text-white font-semibold">👥 Population:</span> <span className="text-gray-300">577 citizens</span></p>
                      <p className="text-xs"><span className="text-white font-semibold">🏘️ Towns:</span> <span className="text-gray-300">34 imperial towns</span></p>
                      <p className="text-xs"><span className="text-white font-semibold">🏛️ Capital:</span> <span className="text-gray-300">Maicao</span></p>
                      <p className="text-xs"><span className="text-white font-semibold">🌎 Regions:</span> <span className="text-gray-300">Colombian, Central America, Caribbean, South America</span></p>
                      <p className="text-xs mt-2"><span className="text-white font-semibold">🎮 Server:</span> <span className="text-gray-300">DiplomaticaMC - 57 players online</span></p>
                    </div>
                    <div className="text-xs text-gray-500 mt-2">🇨🇴 Plus Ultra, further beyond</div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* /leadership Command */}
          <div className="mb-12">
            <h3 className="text-xl font-bold mb-4">👑 <code className="text-yellow-400">/leadership</code> Slash Command</h3>
            <div className="bg-[#2b2d31] rounded-2xl p-6 shadow-2xl border border-white/5">
              <div className="space-y-4">
                <div className="flex items-center gap-2 text-sm text-gray-400">
                  <span className="text-white font-semibold">You:</span>
                  <span className="bg-[#383a40] px-2 py-1 rounded">/leadership</span>
                </div>
                <div className="bg-[#2b2d31] rounded-lg p-4 border-l-4" style={{ borderLeftColor: COLORS.red }}>
                  <div className="flex items-center gap-2 mb-2">
                    <div className="w-6 h-6 rounded-full flex items-center justify-center text-xs"
                      style={{ background: `linear-gradient(135deg, ${COLORS.yellow}, ${COLORS.red})` }}>
                      🇨🇴
                    </div>
                    <span className="text-sm font-semibold text-white">Colombia Pride Bot</span>
                  </div>
                  <div className="ml-8">
                    <div className="text-xs font-semibold mb-2" style={{ color: COLORS.red }}>👑 Leadership of the Reino de Colombia</div>
                    <div className="bg-[#1e1f22] rounded-lg p-3 border-l-2" style={{ borderLeftColor: COLORS.red }}>
                      <p className="text-white text-xs font-semibold mb-1">👑 The Crown</p>
                      <p className="text-gray-300 text-xs">• <strong>9_88</strong> - King of Colombia</p>
                      <p className="text-gray-300 text-xs">• <strong>OliveTree316</strong> - Prime Minister</p>
                      <p className="text-white text-xs font-semibold mb-1 mt-2">🏛️ The Cabinet</p>
                      <p className="text-gray-300 text-xs">• <strong>Novum_Vetus</strong> - Min. of Foreign Affairs</p>
                      <p className="text-gray-300 text-xs">• <strong>Crowlia</strong> - Min. of Defense</p>
                      <p className="text-gray-300 text-xs">• <strong>qulipzz</strong> - Min. of Justice</p>
                      <p className="text-gray-300 text-xs">• <strong>pato541</strong> - Min. of Culture</p>
                    </div>
                    <div className="text-xs text-gray-500 mt-2">🇨🇴 Plus Ultra, further beyond</div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* /player Command */}
          <div className="mb-12">
            <h3 className="text-xl font-bold mb-4">🎮 <code className="text-yellow-400">/player</code> Slash Command</h3>
            <div className="bg-[#2b2d31] rounded-2xl p-6 shadow-2xl border border-white/5">
              <div className="space-y-4">
                <div className="flex items-center gap-2 text-sm text-gray-400">
                  <span className="text-white font-semibold">You:</span>
                  <span className="bg-[#383a40] px-2 py-1 rounded">/player name:9_88</span>
                </div>
                <div className="bg-[#2b2d31] rounded-lg p-4 border-l-4" style={{ borderLeftColor: COLORS.yellow }}>
                  <div className="flex items-center gap-2 mb-2">
                    <div className="w-6 h-6 rounded-full flex items-center justify-center text-xs"
                      style={{ background: `linear-gradient(135deg, ${COLORS.yellow}, ${COLORS.red})` }}>
                      🇨🇴
                    </div>
                    <span className="text-sm font-semibold text-white">Colombia Pride Bot</span>
                  </div>
                  <div className="ml-8">
                    <div className="text-xs font-semibold mb-2" style={{ color: COLORS.yellow }}>🎮 9_88</div>
                    <div className="bg-[#1e1f22] rounded-lg p-3 border-l-2" style={{ borderLeftColor: COLORS.yellow }}>
                      <p className="text-xs"><span className="text-white font-semibold">Role:</span> <span className="text-gray-300">King of Colombia 👑</span></p>
                      <p className="text-xs"><span className="text-white font-semibold">Town:</span> <span className="text-gray-300">Maicao 🏛️</span></p>
                    </div>
                    <div className="text-xs text-gray-500 mt-2">🇨🇴 Reino de Colombia · DiplomaticaMC</div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Holiday Preview */}
          <div className="mt-8">
            <h3 className="text-xl font-bold mb-4 text-center">🎉 Holiday Special Edition</h3>
            <div className="bg-[#2b2d31] rounded-2xl p-6 shadow-2xl border border-white/5">
              <div className="flex items-center gap-3 pb-4 mb-6 border-b border-white/10">
                <div className="w-10 h-10 rounded-full flex items-center justify-center text-xl"
                  style={{ background: `linear-gradient(135deg, ${COLORS.yellow}, ${COLORS.red})` }}>
                  🇨🇴
                </div>
                <div>
                  <div className="font-semibold text-white">Colombia Pride Bot</div>
                  <div className="text-xs text-yellow-400">🎉 Holiday Mode Active</div>
                </div>
              </div>
              <DiscordEmbed
                message="🇨🇴🎆 ¡200+ años de libertad! ¡Viva Colombia! 🎆🇨🇴"
                color={COLORS.yellow}
                index={0}
                isHoliday={true}
                reactions={["🇨🇴", "💛", "💙", "❤️", "🎉", "✨"]}
              />
            </div>
          </div>
        </div>
      </section>

      {/* Holidays & Reactions Section */}
      <section className="py-20 px-6">
        <div className="max-w-5xl mx-auto">
          <div className="grid md:grid-cols-2 gap-8">
            {/* Holidays */}
            <div className="bg-white/[0.02] rounded-2xl border border-white/5 p-8">
              <h3 className="text-2xl font-bold mb-6">🎉 Holiday Detection</h3>
              <p className="text-gray-400 mb-6 text-sm">
                The bot automatically detects Colombian holidays and sends special celebration embeds with extra reactions!
              </p>
              <div className="space-y-2 text-sm">
                <HolidayItem date="Jan 1" name="New Year's Day" emoji="🎆" />
                <HolidayItem date="May 1" name="Labor Day" emoji="💪" />
                <HolidayItem date="Jul 20" name="Independence Day" emoji="🇨🇴" />
                <HolidayItem date="Aug 7" name="Battle of Boyacá" emoji="⚔️" />
                <HolidayItem date="Oct 12" name="Día de la Raza" emoji="🌎" />
                <HolidayItem date="Nov 11" name="Cartagena Independence" emoji="🏰" />
                <HolidayItem date="Dec 7" name="Día de las Velitas" emoji="🕯️" />
                <HolidayItem date="Dec 8" name="Inmaculada Concepción" emoji="⭐" />
                <HolidayItem date="Dec 25" name="Christmas" emoji="🎄" />
              </div>
            </div>

            {/* Reactions */}
            <div className="bg-white/[0.02] rounded-2xl border border-white/5 p-8">
              <h3 className="text-2xl font-bold mb-6">🎯 Auto Reactions</h3>
              <p className="text-gray-400 mb-6 text-sm">
                Every message gets 3-5 random emoji reactions for extra Colombian flair!
              </p>
              <div className="grid grid-cols-4 gap-3 mb-6">
                {["🇨🇴", "💛", "💙", "❤️", "☕", "🌺", "🎉", "✨", "🌟", "🏔️", "🦜", "🌊"].map((emoji) => (
                  <div
                    key={emoji}
                    className="w-12 h-12 rounded-xl bg-white/5 flex items-center justify-center text-2xl hover:scale-110 transition-transform cursor-default"
                  >
                    {emoji}
                  </div>
                ))}
              </div>
              <div className="text-sm text-gray-500">
                <p>• <strong className="text-white">Normal:</strong> 3-5 random reactions</p>
                <p>• <strong className="text-white">Holiday:</strong> 5-7 reactions + 🇨🇴 guaranteed</p>
              </div>
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
                    <td className="px-6 py-4 text-sm text-gray-400">Check bot status and latency</td>
                  </tr>
                  <tr className="border-b border-white/5">
                    <td className="px-6 py-4 font-mono text-sm" style={{ color: COLORS.blue }}>!stats</td>
                    <td className="px-6 py-4 text-sm text-gray-400">View bot statistics</td>
                  </tr>
                  <tr className="border-b border-white/5">
                    <td className="px-6 py-4 font-mono text-sm" style={{ color: COLORS.red }}>!holidays</td>
                    <td className="px-6 py-4 text-sm text-gray-400">See Colombian holidays calendar</td>
                  </tr>
                  <tr className="border-b border-white/5">
                    <td className="px-6 py-4 font-mono text-sm" style={{ color: COLORS.yellow }}>!fact</td>
                    <td className="px-6 py-4 text-sm text-gray-400">Random Colombian fact</td>
                  </tr>
                  <tr className="border-b border-white/5">
                    <td className="px-6 py-4 font-mono text-sm" style={{ color: COLORS.blue }}>!quote</td>
                    <td className="px-6 py-4 text-sm text-gray-400">Inspirational Colombian quote</td>
                  </tr>
                  <tr className="border-b border-white/5">
                    <td className="px-6 py-4 font-mono text-sm" style={{ color: COLORS.red }}>!flag</td>
                    <td className="px-6 py-4 text-sm text-gray-400">Show the Colombian flag</td>
                  </tr>
                  <tr className="border-b border-white/5">
                    <td className="px-6 py-4 font-mono text-sm" style={{ color: COLORS.yellow }}>!color</td>
                    <td className="px-6 py-4 text-sm text-gray-400">Random flag color with meaning</td>
                  </tr>
                  <tr className="border-b border-white/5">
                    <td className="px-6 py-4 font-mono text-sm" style={{ color: COLORS.blue }}>!emoji</td>
                    <td className="px-6 py-4 text-sm text-gray-400">Random Colombian emojis</td>
                  </tr>
                  <tr className="border-b border-white/5">
                    <td className="px-6 py-4 font-mono text-sm" style={{ color: COLORS.red }}>!message</td>
                    <td className="px-6 py-4 text-sm text-gray-400">Random pride message</td>
                  </tr>
                  <tr className="border-b border-white/5">
                    <td className="px-6 py-4 font-mono text-sm" style={{ color: COLORS.yellow }}>!squad</td>
                    <td className="px-6 py-4 text-sm text-gray-400">Colombia's 2026 World Cup roster ⚽</td>
                  </tr>
                  <tr>
                    <td className="px-6 py-4 font-mono text-sm" style={{ color: COLORS.blue }}>!star</td>
                    <td className="px-6 py-4 text-sm text-gray-400">Key players to watch ⭐</td>
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

function DiscordEmbed({ message, color, index, reactions, isHoliday }: {
  message: string;
  color: string;
  index: number;
  reactions?: string[];
  isHoliday?: boolean;
}) {
  const authors = ['☀️ Golden Spirit', '🌊 Deep Blue Ocean', '🌹 Passionate Red'];
  const footers = ['🇨🇴 República de Colombia', '🇨🇴 Orgullo Colombiano', '🇨🇴 Tierra de mil colores'];
  const holidayFooters = ['🇨🇴 ¡Celebrando con orgullo!', '🎉🇨🇴 ¡Que viva la fiesta!'];

  return (
    <div className="bg-[#2b2d31] rounded-lg p-4 border-l-4 max-w-sm" style={{ borderLeftColor: color }}>
      <div className="flex items-center gap-2 mb-2">
        <div className="w-6 h-6 rounded-full flex items-center justify-center text-xs"
          style={{ background: `linear-gradient(135deg, ${COLORS.yellow}, ${COLORS.red})` }}>
          🇨🇴
        </div>
        <span className="text-sm font-semibold text-white">Colombia Pride Bot</span>
        {isHoliday && (
          <span className="text-xs px-2 py-0.5 rounded-full bg-yellow-500/20 text-yellow-400 font-medium">
            🎉 Holiday
          </span>
        )}
        <span className="text-xs text-gray-500 ml-auto">Today at 12:00 PM</span>
      </div>
      <div className="ml-8">
        <div className="text-xs font-semibold mb-1" style={{ color }}>{authors[index]}</div>
        <div className="bg-[#1e1f22] rounded-lg p-3 border-l-2" style={{ borderLeftColor: color }}>
          <p className="text-white text-sm font-medium">{message}</p>
          {isHoliday && (
            <p className="text-xs text-gray-400 mt-1 italic">*Special Holiday Edition*</p>
          )}
        </div>
        <div className="text-xs text-gray-500 mt-2">
          {isHoliday ? holidayFooters[index % holidayFooters.length] : footers[index]}
        </div>
        {/* Reactions */}
        {reactions && reactions.length > 0 && (
          <div className="flex flex-wrap gap-1 mt-2">
            {reactions.map((emoji, i) => (
              <span
                key={i}
                className="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-[#2b2d31] border border-white/10 text-xs hover:bg-white/5 transition-colors cursor-default"
              >
                {emoji} <span className="text-gray-400">1</span>
              </span>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

function HolidayItem({ date, name, emoji }: { date: string; name: string; emoji: string }) {
  return (
    <div className="flex items-center gap-3 py-2 px-3 rounded-lg hover:bg-white/5 transition-colors">
      <span className="text-lg">{emoji}</span>
      <span className="text-gray-300 flex-1">{name}</span>
      <span className="text-gray-500 text-xs font-mono">{date}</span>
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
Holiday Detection | Emoji Variations | Auto Reactions
"""

import os, sys, random, asyncio, logging
from datetime import datetime
import discord
from discord.ext import commands
from config import *

# Bot Setup
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents,
    description="🇨🇴 Celebrating Colombia with pride",
)

def get_random_emoji_message(base_message: str) -> str:
    """Returns a random emoji variation of a base message."""
    variations = EMOJI_VARIATIONS.get(base_message, [base_message])
    return random.choice(variations)

def create_pride_embed(message: str, is_holiday=False) -> discord.Embed:
    """Creates a beautiful embed with Colombian flag colors."""
    color = random.choice(EMBED_COLORS)
    footer = random.choice(HOLIDAY_FOOTERS if is_holiday else FOOTERS)
    
    embed = discord.Embed(
        description=message,
        color=color,
        timestamp=datetime.utcnow(),
    )
    embed.set_footer(text=footer)
    
    if is_holiday:
        embed.set_thumbnail(url="flag_url_here")
        embed.add_field(name="🎉", value="*Special Holiday Edition*")
    
    return embed

async def add_reactions(message, is_holiday=False):
    """Adds emoji reactions — more on holidays!"""
    num = random.randint(
        MIN_REACTIONS + (1 if is_holiday else 0),
        MAX_REACTIONS + (2 if is_holiday else 0)
    )
    reactions = ["🇨🇴"] if is_holiday else []
    available = [e for e in REACTION_EMOJIS if e not in reactions]
    reactions.extend(random.sample(available, num - len(reactions)))
    
    for emoji in reactions:
        await message.add_reaction(emoji)
        await asyncio.sleep(random.uniform(0.5, 1.5))

async def send_cycle_messages():
    """Main cycle loop with holiday detection."""
    channel = bot.get_channel(CHANNEL_ID)
    holiday_message = get_holiday_message()
    is_holiday_today = holiday_message is not None
    
    if is_holiday_today:
        logger.info("🎉 HOLIDAY DETECTED!")
    
    for i in range(random.randint(7, 12)):
        use_holiday = is_holiday_today and i == 0
        
        if use_holiday:
            message = holiday_message
        else:
            base = random.choice(BASE_MESSAGES)
            message = get_random_emoji_message(base)
        
        embed = create_pride_embed(message, is_holiday=use_holiday)
        sent = await channel.send(embed=embed)
        
        # Auto-react with Colombian emojis!
        await add_reactions(sent, is_holiday=use_holiday)
        
        await asyncio.sleep(random.uniform(25, 40) * 60)

@bot.command(name="holidays")
async def holidays(ctx):
    """Show Colombian holidays the bot celebrates."""
    # ... displays holiday calendar
    await ctx.send(embed=embed)

bot.run(BOT_TOKEN)`;

const CONFIG_CODE = `"""
🇨🇴 Colombia Pride Bot - Configuration
Holidays | Emoji Variations | Reactions
"""

import os, discord
from dotenv import load_dotenv
from datetime import date

load_dotenv()

BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN", "")
CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID", "0"))

# ─── Colombian Flag Colors ───────────────────────
EMBED_COLORS = [
    discord.Color.from_hex("#FCD116"),  # Yellow
    discord.Color.from_hex("#003893"),  # Blue
    discord.Color.from_hex("#CE1126"),  # Red
]

# ─── Emoji Variations (24+ combos!) ──────────────
EMOJI_VARIATIONS = {
    "¡Viva Colombia!": [
        "🇨🇴 ¡Viva Colombia! 🇨🇴",
        "💛💙❤️ ¡Viva Colombia! 💛💙❤️",
        "🦜 ¡Viva Colombia! 🌺",
        # ... 8 variations total
    ],
    "We export more than just coffee.": [
        "☕ We export more than just coffee. 🌎",
        "🌱 We export more than just coffee. 💚",
        # ... 8 variations total
    ],
    "Yellow. Blue. Red.": [
        "💛 Yellow. 💙 Blue. ❤️ Red.",
        "☀️ Yellow. 🌊 Blue. 🌹 Red.",
        # ... 8 variations total
    ],
}

# ─── Holiday Messages ────────────────────────────
HOLIDAY_MESSAGES = {
    "independence_day": [
        "🇨🇴🎆 ¡200+ años de libertad!",
        "🎉 ¡Feliz Día de la Independencia!",
    ],
    "christmas": [
        "🎄🇨🇴 ¡Feliz Navidad desde Colombia!",
    ],
    # ... 10+ holidays supported
}

# ─── Reaction Emojis ─────────────────────────────
REACTION_EMOJIS = [
    "🇨🇴", "💛", "💙", "❤️", "☕",
    "🌺", "🎉", "✨", "🌟", "🏔️",
    "🦜", "🌊",
]
MIN_REACTIONS = 3
MAX_REACTIONS = 5

# ─── Holidays Calendar ───────────────────────────
COLOMBIAN_HOLIDAYS = {
    (1, 1): "new_year",
    (5, 1): "labor_day",
    (7, 20): "independence_day",
    (8, 7): "battle_of_boyaca",
    (12, 7): "candelaria",
    (12, 25): "christmas",
    # ... 15 holidays total
}

def get_todays_holiday():
    """Check if today is a Colombian holiday."""
    today = date.today()
    return COLOMBIAN_HOLIDAYS.get((today.month, today.day))`;

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
