from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import CommandHandler, Dispatcher, CallbackContext
import os

# === CONFIGURATION ===
TOKEN = "7951239927:AAEZss5G4Qa0RL5fTh4c94j6DZARJwTvmhs"
WEBHOOK_URL = "https://your-app-name.onrender.com"  # Change this to your Render live URL

# === SETUP ===
app = Flask(__name__)
bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot=bot, update_queue=None, use_context=True)

# === HANDLERS ===
def start(update: Update, context: CallbackContext):
    user = update.effective_user.first_name
    update.message.reply_text(f"🙏 Welcome {user}! I'm Ranjeet Bhaiya - Your Career Guide. 🚀\n\nType /help to explore all features.")

def help_command(update: Update, context: CallbackContext):
    help_text = (
        "Here are some things you can do:\n"
        "/start - Begin your journey\n"
        "/vedicmath - Learn fast math tricks\n"
        "/abacus - Improve your mental calculation\n"
        "/ask - Ask any career/study question"
    )
    update.message.reply_text(help_text)

def vedicmath(update: Update, context: CallbackContext):
    update.message.reply_text("🧠 Vedic Math Tips Coming Soon! Stay tuned.")

def abacus(update: Update, context: CallbackContext):
    update.message.reply_text("🔢 Abacus training content coming soon.")

# === Register Handlers ===
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("help", help_command))
dispatcher.add_handler(CommandHandler("vedicmath", vedicmath))
dispatcher.add_handler(CommandHandler("abacus", abacus))

# === Webhook route ===
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok"

# === Set webhook before first request ===
@app.before_request
def set_webhook():
    bot.set_webhook(f"{WEBHOOK_URL}/{TOKEN}")

@app.route("/", methods=["GET"])
def index():
    return "Bot is live and running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
