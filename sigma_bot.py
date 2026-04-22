import logging
import random
from datetime import datetime
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# --- !!! IMPORTANT: PASTE YOUR BOT TOKEN HERE !!! ---
# You can get this from BotFather. It will look like '1234567890:ABCdefGHIjklMNOpqrsTUVwxyz'
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# --- Enable logging to see what your bot is doing ---
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# --- Your custom data (quotes, tips) ---
TRADING_QUOTES = [
    "The trend is your friend until the end.",
    "Cut your losses short and let your winners run.",
    "Risk comes from not knowing what you're doing.",
    "The goal of a successful trader is to make the best trades, not to make money.",
    "Amateurs look for confirmation; professionals look for evidence.",
]

TRADING_TIPS = [
    "🧠 *Psychological Tip*: Keep a trading journal. Reviewing your trades helps separate skill from luck.",
    "⚖️ *Risk Tip*: Never risk more than 1-2% of your account on a single trade.",
    "📈 *Market Tip*: The first hour of the market open can often set the tone for the rest of the day.",
    "🧘 *Mindset Tip*: Focus on executing your process perfectly, not on the profit and loss of a single trade.",
]

# --- The Core Bot Functions (Handlers) ---

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler for the /start command."""
    welcome_message = (
        "👋 Welcome to the SigmaSession Companion Bot!\n\n"
        "I'm here to help you master your trading psychology.\n\n"
        "Use the commands below to get started:\n"
        "/quote - Get a random trading wisdom\n"
        "/tip - Get a psychological trading tip\n"
        "/markets - See current global session status\n"
        "/help - Show this list again"
    )
    await update.message.reply_text(welcome_message)

async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler for the /quote command."""
    random_quote = random.choice(TRADING_QUOTES)
    await update.message.reply_text(f'📖 *Trading Wisdom:*\n\n“{random_quote}”', parse_mode='Markdown')

async def tip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler for the /tip command."""
    random_tip = random.choice(TRADING_TIPS)
    await update.message.reply_text(random_tip, parse_mode='Markdown')

async def markets(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler for the /markets command."""
    current_hour = datetime.now().hour
    if 0 <= current_hour < 7:
        session_status = "🌏 *Asian Session Active* - Low to medium volatility."
    elif 7 <= current_hour < 13:
        session_status = "🇬🇧 *London Session Active* - High volatility, major trends begin."
    elif 13 <= current_hour < 22:
        session_status = "🇺🇸 *New York Session Active* - Very high volatility, major news."
    else:
        session_status = "🌙 *Market Session Closed* - Generally lower liquidity."

    await update.message.reply_text(f"📊 *Current Market Outlook:*\n\n{session_status}", parse_mode='Markdown')

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler for any unknown command."""
    await update.message.reply_text("❌ Sorry, I didn't understand that command. Try /help to see what I can do.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler for the /help command."""
    help_text = (
        "Here's how you can use me:\n\n"
        "/quote - 📖 Get a random trading wisdom quote\n"
        "/tip - 🧠 Get a psychological trading tip\n"
        "/markets - 📊 See which global trading session is active\n"
        "/start - 👋 See the welcome message again\n"
        "/help - ❓ Show this help message"
    )
    await update.message.reply_text(help_text)


# --- The Main Function to Run the Bot ---
def main():
    """Start the bot."""
    # 1. Create the Application
    application = Application.builder().token(BOT_TOKEN).build()

    # 2. Register command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("quote", quote))
    application.add_handler(CommandHandler("tip", tip))
    application.add_handler(CommandHandler("markets", markets))
    
    # This must be the last handler. It catches any unknown commands.
    application.add_handler(CommandHandler("unknown", unknown))

    # 3. Start the bot (using polling, which is fine for testing)
    print("🤖 Bot is starting... Press Ctrl+C to stop.")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()