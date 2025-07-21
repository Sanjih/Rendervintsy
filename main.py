import os
from flask import Flask, request, abort
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Fenoy amin'ny Token tena izy avy amin'ny BotFather
TOKEN = "8092994458:AAHI1Ud1fh2E06VaXy6826Db0KH4KAstn6E" 
# Esory ity tsipika ity. Tsy ilaina eto intsony ny WEBHOOK_URL.
# WEBHOOK_URL = os.getenv("https://telegram-bot-nk3n.onrender.com")

app = Flask(__name__)

# Mamorona ny Application object eo am-piandohana
application = Application.builder().token(TOKEN).build()

# Ampidiro ity tsipika ity mba hanombohana ny application
application.initialize() 

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Salama! Bot Telegram no nandray anao.")

application.add_handler(CommandHandler("start", start))

@app.route("/")
def home():
    return "Bot is running!"

@app.route("/webhook", methods=["POST"])
async def webhook():
    if request.method == "POST":
        json_data = request.get_json(force=True)
        # Ampiasao ireo print statements ireo hijerena ny log
        print("Received a webhook request!")
        print(f"Received JSON: {json_data}")
        update = Update.de_json(json_data, application.bot)
        
        # Mampiasa process_update_async izay async
        await application.process_update(update) 
        
        return "ok", 200
    abort(403)


