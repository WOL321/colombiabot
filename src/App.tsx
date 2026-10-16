import { useState, useEffect } from 'react';

const COLORS = {
  yellow: '#FCD116',
  blue: '#003893',
  red: '#CE1126',
};

const MESSAGES = [
  { text: 'Que viva Colombia!', accent: '🇨🇴', reactions: ['🇨🇴', '🎆', '💛', '💙', '❤️'] },
  { text: 'Yellow. Blue. Red.', accent: '💛💙❤️', reactions: ['💛', '💙', '❤️', '🇨🇴'] },
  { text: 'We export more than just coffee ;)', accent: '☕', reactions: ['☕', '✨', '🇨🇴', '💚'] },
  { text: 'Colombia needs no explanation.', accent: '🏔️', reactions: ['🏔️', '🌊', '🦜', '🇨🇴'] },
  { text: 'The tricolor still means something.', accent: '🔥', reactions: ['🇨🇴', '🔥', '💛', '💙', '❤️'] },
  { text: 'From the Caribbean to the Amazon.', accent: '🌴', reactions: ['🌴', '🌊', '🦜', '🇨🇴'] },
];

function App() {
  const [currentColor, setCurrentColor] = useState(0);
  const [currentMessage, setCurrentMessage] = useState(0);

  const colors = [COLORS.yellow, COLORS.blue, COLORS.red];

  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentColor((prev) => (prev + 1) % 3);
    }, 3000);
    return () => clearInterval(interval);
  }, []);

  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentMessage((prev) => (prev + 1) % MESSAGES.length);
    }, 4000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="min-h-screen bg-[#0a0a0f] text-white">
      {/* Hero */}
      <section className="min-h-screen flex items-center justify-center px-6 relative overflow-hidden">
        {/* Animated background */}
        <div className="absolute inset-0">
          <div
            className="absolute top-1/4 left-1/4 w-96 h-96 rounded-full opacity-20 blur-3xl transition-colors duration-1000"
            style={{ backgroundColor: colors[currentColor] }}
          />
          <div
            className="absolute bottom-1/4 right-1/4 w-80 h-80 rounded-full opacity-15 blur-3xl transition-colors duration-1000"
            style={{ backgroundColor: colors[(currentColor + 1) % 3] }}
          />
        </div>

        <div className="max-w-4xl mx-auto text-center relative z-10">
          {/* Flag stripe */}
          <div className="flex justify-center mb-8">
            <div className="flex rounded-full overflow-hidden shadow-2xl" style={{ boxShadow: `0 0 80px ${colors[currentColor]}40` }}>
              <div className="w-20 h-3" style={{ backgroundColor: COLORS.yellow }} />
              <div className="w-20 h-3" style={{ backgroundColor: COLORS.blue }} />
              <div className="w-20 h-3" style={{ backgroundColor: COLORS.red }} />
            </div>
          </div>

          <h1 className="text-6xl md:text-8xl font-black mb-6 leading-none">
            <span className="bg-clip-text text-transparent" style={{
              backgroundImage: `linear-gradient(135deg, ${COLORS.yellow}, ${COLORS.blue}, ${COLORS.red})`
            }}>
              Colombia
            </span>
            <br />
            <span className="text-white/90">Pride Bot</span>
          </h1>

          <p className="text-xl text-gray-400 mb-12 max-w-xl mx-auto">
            A simple Discord bot that celebrates Colombia with style.
          </p>

          {/* Live embed preview */}
          <div className="max-w-md mx-auto">
            <DiscordEmbed
              message={MESSAGES[currentMessage]}
              color={colors[currentMessage % 3]}
            />
          </div>
        </div>
      </section>

      {/* Messages */}
      <section className="py-32 px-6">
        <div className="max-w-3xl mx-auto">
          <h2 className="text-4xl font-bold mb-16 text-center">The messages</h2>
          
          <div className="space-y-6">
            {MESSAGES.map((message, index) => (
              <div key={index} className="flex items-center gap-4 p-6 rounded-xl bg-white/[0.02] border border-white/5">
                <div className="text-2xl">{message.accent}</div>
                <div className="text-lg">{message.text}</div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Features */}
      <section className="py-32 px-6 bg-white/[0.02]">
        <div className="max-w-3xl mx-auto">
          <h2 className="text-4xl font-bold mb-16 text-center">What it does</h2>
          
          <div className="space-y-12">
            <div className="flex gap-6">
              <div className="text-4xl">✨</div>
              <div>
                <h3 className="text-xl font-semibold mb-2">Beautiful embeds</h3>
                <p className="text-gray-400">Every message wrapped in a clean embed with Colombian flag colors and themed emojis.</p>
              </div>
            </div>

            <div className="flex gap-6">
              <div className="text-4xl">🇨🇴</div>
              <div>
                <h3 className="text-xl font-semibold mb-2">Cool reactions</h3>
                <p className="text-gray-400">Each message gets 3-5 themed emoji reactions that match the vibe.</p>
              </div>
            </div>

            <div className="flex gap-6">
              <div className="text-4xl">⏰</div>
              <div>
                <h3 className="text-xl font-semibold mb-2">Natural timing</h3>
                <p className="text-gray-400">Messages every 25-40 minutes. Never spammy, always organic.</p>
              </div>
            </div>

            <div className="flex gap-6">
              <div className="text-4xl">💯</div>
              <div>
                <h3 className="text-xl font-semibold mb-2">Simple & focused</h3>
                <p className="text-gray-400">Just the messages. No bloat. No complexity.</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Setup */}
      <section className="py-32 px-6">
        <div className="max-w-2xl mx-auto text-center">
          <h2 className="text-4xl font-bold mb-8">Get started</h2>
          <p className="text-gray-400 mb-12 text-lg">
            Free. Open source. Runs on GitHub Actions.
          </p>
          
          <a
            href="https://github.com"
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center gap-3 px-8 py-4 rounded-xl font-semibold text-black transition-all hover:scale-105"
            style={{ backgroundColor: COLORS.yellow }}
          >
            <i className="fab fa-github text-2xl"></i>
            View on GitHub
          </a>
        </div>
      </section>

      {/* Footer */}
      <footer className="py-12 px-6 border-t border-white/5">
        <div className="max-w-5xl mx-auto text-center">
          <div className="flex justify-center mb-4">
            <div className="flex rounded-full overflow-hidden">
              <div className="w-12 h-1.5" style={{ backgroundColor: COLORS.yellow }} />
              <div className="w-12 h-1.5" style={{ backgroundColor: COLORS.blue }} />
              <div className="w-12 h-1.5" style={{ backgroundColor: COLORS.red }} />
            </div>
          </div>
          <p className="text-gray-500 text-sm">
            Made with 🇨🇴 for Colombia
          </p>
        </div>
      </footer>
    </div>
  );
}

function DiscordEmbed({ message, color }: {
  message: typeof MESSAGES[0];
  color: string;
}) {
  return (
    <div className="bg-[#2b2d31] rounded-lg p-4 border-l-4" style={{ borderLeftColor: color }}>
      <div className="flex items-center gap-2 mb-3">
        <div className="w-8 h-8 rounded-full flex items-center justify-center text-sm"
          style={{ background: `linear-gradient(135deg, ${COLORS.yellow}, ${COLORS.red})` }}>
          🇨🇴
        </div>
        <div>
          <div className="text-sm font-semibold text-white">Colombia Pride Bot</div>
          <div className="text-xs text-gray-500">Today at 12:00 PM</div>
        </div>
      </div>
      <div className="ml-10">
        <div className="bg-[#1e1f22] rounded-lg p-3 border-l-2" style={{ borderLeftColor: color }}>
          <p className="text-white text-sm">
            {message.accent} {message.text}
          </p>
        </div>
        <div className="text-xs text-gray-500 mt-2">🇨🇴 Colombia</div>
        <div className="flex gap-2 mt-2 flex-wrap">
          {message.reactions.slice(0, 4).map((emoji, i) => (
            <span key={i} className="text-xs px-2 py-1 rounded-full bg-[#2b2d31] border border-white/10">
              {emoji} 1
            </span>
          ))}
        </div>
      </div>
    </div>
  );
}

export default App;
