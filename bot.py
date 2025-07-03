from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from flask import Flask, request
import os

TOKEN = "7951239927:AAEZss5G4Qa0RL5fTh4c94j6DZARJwTvmhs"
WEBHOOK_URL = "https://your-app-name.onrender.com"

app = Flask(__name__)
telegram_app = ApplicationBuilder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_first_name = update.effective_user.first_name
    welcome_text = f"🙏 Welcome {user_first_name}! I'm Ranjeet Bhaiya - Your Career Guide. 🚀\n\nType /help to explore all features."
    await update.message.reply_text(welcome_text)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "Here are some things you can do:\n"
        "/start - Begin your journey\n"
        "/vedicmath - Learn fast math tricks\n"
        "/abacus - Improve your mental calculation\n"
        "/ask - Ask any career/study question"
    )
    await update.message.reply_text(help_text)

async def vedicmath(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🧠 Vedic Math Tips Coming Soon! Stay tuned.")

async def abacus(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔢 Abacus training content coming soon.")

telegram_app.add_handler(CommandHandler("start", start))
telegram_app.add_handler(CommandHandler("help", help_command))
telegram_app.add_handler(CommandHandler("vedicmath", vedicmath))
telegram_app.add_handler(CommandHandler("abacus", abacus))

@app.route(f'/7951239927:AAEZss5G4Qa0RL5fTh4c94j6DZARJwTvmhs', methods=["POST"])
async def webhook():
    await telegram_app.update_queue.put(Update.de_json(request.get_json(force=True), telegram_app.bot))
    return "ok"

@app.before_first_request
def set_webhook():
    from telegram import Bot
    bot = Bot(token=TOKEN)
    bot.set_webhook(url=f"{WEBHOOK_URL}/7951239927:AAEZss5G4Qa0RL5fTh4c94j6DZARJwTvmhs")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
