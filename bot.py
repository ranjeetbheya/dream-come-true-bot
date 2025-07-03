
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_first_name = update.effective_user.first_name
    welcome_text = f"🙏 Welcome {user_first_name}! I'm Ranjeet Bhaiya - Your Career Guide. 🚀\n\nType /help to explore all features."
    await update.message.reply_text(welcome_text)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = "Here are some things you can do:\n" \                "/start - Begin your journey\n" \                "/vedicmath - Learn fast math tricks\n" \                "/abacus - Improve your mental calculation\n" \                "/ask - Ask any career/study question"
    await update.message.reply_text(help_text)

async def vedicmath(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🧠 Vedic Math Tips Coming Soon! Stay tuned.")

async def abacus(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔢 Abacus training content coming soon.")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("vedicmath", vedicmath))
app.add_handler(CommandHandler("abacus", abacus))

app.run_polling()
