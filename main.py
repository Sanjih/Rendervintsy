import os
import asyncio # Mila izy ity ho an'ny fampandehanana ny Application as async
from flask import Flask, request, abort
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Fenoy amin'ny Token tena izy avy amin'ny BotFather
TOKEN = "8092994458:AAHI1Ud1fh2E06VaXy6826Db0KH4KAstn6E" 

# Vakio avy amin'ny environment variable ny URL webhook, na apetraho mivantana
# Tsara kokoa ny mametraka azy ho environment variable ao amin'ny Render
WEBHOOK_URL = os.getenv("WEBHOOK_URL", "https://telegram-bot-nk3n.onrender.com/webhook")

app = Flask(__name__)

# Manao Application object global mba ho azo avy amin'ny Flask route
application: Application = None # Hatao none aloha, fa hofenoina any aoriana

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Salama! Bot Telegram no nandray anao.")

@app.route("/")
def home():
    return "Bot is running!"

@app.route("/webhook", methods=["POST"])
async def webhook(): # Ataovy async ity function ity
    if request.method == "POST":
        json_data = request.get_json(force=True)
        update = Update.de_json(json_data, application.bot)
        
        # Mampiasa process_update_async izay async
        await application.process_update(update) 
        
        return "ok", 200
    abort(403)

# Function iray hanombohana sy hametrahana ny webhook
async def setup_bot():
    global application
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))

    # Apetraho ny webhook. Izany dia tsy mila atao afa-tsy indray mandeha.
    # Raha efa napetraka izy ary tsy miova ny URL, dia tsy mila averina.
    # Azonao atao ny manao ity anaty script misaraka na miantso azy mandeha ho azy.
    # Amin'ny Render, azonao atao ny mametraka build command na cron job ho an'ity.
    print(f"Setting webhook to: {WEBHOOK_URL}")
    await application.bot.set_webhook(url=WEBHOOK_URL)
    print("Webhook set successfully!")

if __name__ == "__main__":
    # Tokony hatao async ny fanombohana ny bot
    # Eto izany dia atao ao anatin'ny event loop
    try:
        # Initialisation ny application sy fametrahana webhook
        # Ity dia tokony atao indray mandeha mandritra ny fametrahana ny serivisy
        # Tsy mila miverimberina isaky ny manomboka ny app
        asyncio.run(setup_bot())
    except Exception as e:
        print(f"Error during bot setup or webhook setting: {e}")
        # Aza ajanona ny app raha misy olana amin'ny fametrahana webhook
        # Satria mety efa napetraka ilay izy teo aloha
    
    # Ampiasaina ny Flask server
    port = int(os.environ.get("PORT", 5000))
    print(f"Flask app running on port {port}")
    app.run(host="0.0.0.0", port=port)
