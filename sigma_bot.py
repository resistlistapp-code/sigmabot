# sigma_bot.py - Complete Telegram Bot for SigmaSession (Render-Ready)
import os
import logging
import random
from datetime import datetime
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# --- Read token from environment variable (for Render deployment) ---
BOT_TOKEN = os.environ.get("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("No BOT_TOKEN found! Set BOT_TOKEN environment variable.")

# --- Enable logging to see what your bot is doing ---
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", 
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# --- YOUR ACTUAL TRADING QUOTES (from tradingQuotesData.js) ---
TRADING_QUOTES = [
    "Markets are never wrong – opinions often are. — Jesse Livermore",
    "The big money is not in the buying and selling, but in the waiting. — Jesse Livermore",
    "Cut losses quickly, let winners run. Never average a loss. — Jesse Livermore",
    "There is nothing new in Wall Street. There can't be because speculation is as old as the hills. — Jesse Livermore",
    "Focus on protecting capital, not making money. — Paul Tudor Jones",
    "Don't focus on making money; focus on protecting what you have. — Paul Tudor Jones",
    "The secret to being successful from a trading perspective is to have an indefatigable and an undying and unquenchable thirst for information and knowledge. — Paul Tudor Jones",
    "I think the most important thing I've learned is that you have to be able to admit when you're wrong and get out. — Paul Tudor Jones",
    "Don't let ego stand in the way of learning. — Ray Dalio",
    "He who lives by the crystal ball will eat shattered glass. — Ray Dalio",
    "Principles are what allow you to live a life of meaning and success. — Ray Dalio",
    "Pain + Reflection = Progress. — Ray Dalio",
    "Your first loss is your best loss. Keep it small. — Linda Raschke",
    "Trade what you see, not what you think. — Linda Raschke",
    "The trend is your friend until it bends. — Linda Raschke",
    "Don't confuse a good trade with a winning trade. — Linda Raschke",
    "Your edge is your ability to stay disciplined. — Mark Minervini",
    "Only buy the very best setups. Don't compromise quality. — Mark Minervini",
    "It's not about being right, it's about making money when you're right. — Mark Minervini",
    "The best traders have no ego. You have to admit when you're wrong and get out. — Mark Minervini",
    "The consistency you seek is in your mind, not the markets. — Mark Douglas",
    "Think in probabilities, not certainties. — Mark Douglas",
    "Anything can happen in the markets. That's the only thing you can be certain of. — Mark Douglas",
    "Your beliefs about trading will determine your trading results. — Mark Douglas",
    "Amateurs look for tips. Professionals look for discipline. — Alexander Elder",
    "Master your emotions first. Then master the markets. — Alexander Elder",
    "The best investment you can make is in your own trading psychology. — Alexander Elder",
    "There are no bad trades, only bad risk management. — Alexander Elder",
    "Do not let a winning trade turn into a loser. Ever. — Tom Hougaard",
    "The trend is your friend, but discipline is your master. — Tom Hougaard",
    "Trade small, trade often, and let your winners run. — Tom Hougaard",
    "Your ego is not your amigo. — Tom Hougaard",
    "The true measure of success is what you take with you when you're done. — Matt 'PAX' Kenah",
    "Ego destroys accounts. Survive first, profit second. — Matt 'PAX' Kenah",
    "The less I trade, the happier I will be. I don't need every wiggle. — Matt 'PAX' Kenah",
    "A bad trade is a mistake. A big loss is a failure of risk. — Matt 'PAX' Kenah",
    "You must pick the loss side first. Everything else is biased. — Jim Paul",
    "Manage your losses, not predict your profits. — Jim Paul",
    "Success can be built on repeated failures when not taken personally. — Jim Paul",
    "If you have a position on but do something else, you made a crowd trade. — Jim Paul",
    "It's not about getting rich quick. It's about staying in the game long enough for consistency to compound. — Lance Breitstein",
    "If you pick random stocks to trade, you are sitting at a random slot machine. Over the long run, you will lose. — Lance Breitstein",
    "Rather than thinking about your P&L, focus on your expected value (EV) going up over time. — Lance Breitstein",
    "Slow down. Today's not your day. Take a break before you churn your account. — Lance Breitstein",
]

# --- Trading Psychology Tips ---
TRADING_TIPS = [
    "🧠 *Psychological Tip*: Keep a trading journal. Reviewing your trades helps separate skill from luck.",
    "⚖️ *Risk Tip*: Never risk more than 1-2% of your account on a single trade.",
    "📈 *Market Tip*: The first hour of the market open can often set the tone for the rest of the day.",
    "🧘 *Mindset Tip*: Focus on executing your process perfectly, not on the profit and loss of a single trade.",
    "🎯 *Discipline Tip*: Have a written trading plan and follow it without exception.",
    "😌 *Emotion Tip*: If you feel angry or revengeful after a loss, stop trading for the day.",
    "📊 *Analysis Tip*: Review your trades weekly to identify patterns in your winners and losers.",
    "🛡️ *Risk Tip*: A 2% loss requires a 2.04% gain to break even. A 50% loss requires a 100% gain. Protect your capital.",
    "⏰ *Timing Tip*: The best trades often come when you're patient enough to wait for them.",
    "💪 *Resilience Tip*: Every great trader has losing streaks. What separates them is how they respond.",
]

# --- Bot Command Handlers ---

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler for /start command."""
    user_name = update.effective_user.first_name
    welcome_message = (
        f"👋 Welcome to SigmaSession, {user_name}!\n\n"
        "I'm your trading psychology companion bot.\n\n"
        "📋 *Available Commands:*\n"
        "/quote - Get a random trading wisdom\n"
        "/tip - Get a psychological trading tip\n"
        "/markets - See current global session status\n"
        "/help - Show this list again\n\n"
        "Use me alongside the SigmaSession app to master your trading psychology! 📈"
    )
    await update.message.reply_text(welcome_message, parse_mode='Markdown')

async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler for /quote command."""
    random_quote = random.choice(TRADING_QUOTES)
    await update.message.reply_text(
        f'📖 *Trading Wisdom:*\n\n“{random_quote}”',
        parse_mode='Markdown'
    )

async def tip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler for /tip command."""
    random_tip = random.choice(TRADING_TIPS)
    await update.message.reply_text(random_tip, parse_mode='Markdown')

async def markets(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler for /markets command."""
    current_hour = datetime.now().hour
    
    if 0 <= current_hour < 7:
        session_status = "🌏 *Asian Session Active*\nSydney & Tokyo trading\nLow to medium volatility, range-bound movement."
    elif 7 <= current_hour < 13:
        session_status = "🇬🇧 *London Session Active*\nHigh volatility, major trends begin\nStrong momentum, London open."
    elif 13 <= current_hour < 22:
        session_status = "🇺🇸 *New York Session Active*\nVery high volatility, US economic data\nLondon overlap creates maximum liquidity."
    else:
        session_status = "🌙 *Markets Closed*\nLower liquidity during Asian hours\nUse this time for preparation and review."
    
    await update.message.reply_text(
        f"📊 *Current Market Outlook:*\n\n{session_status}",
        parse_mode='Markdown'
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler for /help command."""
    help_text = (
        "📋 *SigmaSession Bot Commands*\n\n"
        "/start - 👋 Welcome message\n"
        "/quote - 📖 Get a trading wisdom quote\n"
        "/tip - 🧠 Get a psychological trading tip\n"
        "/markets - 📊 See which global session is active\n"
        "/help - ❓ Show this help message\n\n"
        "💡 *Pro Tip:* Use these commands daily to stay in the right mindset!"
    )
    await update.message.reply_text(help_text, parse_mode='Markdown')

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler for unknown commands."""
    await update.message.reply_text(
        "❌ Sorry, I didn't understand that command.\n\n"
        "Try /help to see what I can do."
    )

# --- The Main Function to Run the Bot ---
def main():
    """Start the SigmaSession bot."""
    print("🤖 SigmaSession Bot is starting...")
    print(f"📊 Loaded {len(TRADING_QUOTES)} trading quotes")
    print(f"💡 Loaded {len(TRADING_TIPS)} trading tips")
    print("-" * 40)
    
    # Create the Application
    application = Application.builder().token(BOT_TOKEN).build()

    # Register command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("quote", quote))
    application.add_handler(CommandHandler("tip", tip))
    application.add_handler(CommandHandler("markets", markets))
    
    # This must be the last handler. It catches any unknown commands.
    application.add_handler(CommandHandler("unknown", unknown))

    # Start the bot (using polling)
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()