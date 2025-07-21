import os
from flask import Flask, request, abort
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import asyncio

# Raha mbola manana ity TOKEN ity ao anatin'ny code ianao, dia tokony ho azo antoka fa marina izy.
# Ny fomba tsara indrindra dia ny mampiasa Environment Variable.
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "8092994458:AAHI1Ud1fh2E06VaXy6826Db0KH4KAstn6E") 

app = Flask(__name__)

# Mamorona ny Application object fa aza initialize-na na start-ina eto.
# Hatao izany ao anatin'ny webhook function.
application = Application.builder().token(TOKEN).build()

# ***** FAMARITANA NY FUNCTION START ALOHA NY ADD_HANDLER *****
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Salama! Bot Telegram no nandray anao.")

application.add_handler(CommandHandler("start", start))

@app.route("/")
def home():
    return "Bot is running!"

@app.route("/webhook", methods=["POST"])
async def webhook():
    # ***** ZAVA-DEHIBE INDRINDRA ETO: Initialization sy fanombohana ny Application *****
    # Raha tsy initialized ny application (indraindray mitranga amin'ny WSGI servers),
    # dia initialized-na sy atombohy eto.
    # Ity dia hiantoka fa initialized sy running ny Application isaky ny mahazo request.
    
    # Ny `_initialized` sy `_running` dia attributes anatiny.
    # Raha ampiasaina amin'ny ptb v20.x, dia mila ampiasaina ny `initialize()` sy `start()`
    # raha tsy misy `check_running()`.

    # Aoka ho azo antoka fa initialized ny Application
    if not getattr(application, '_initialized', False):
        print("Application not initialized, initializing now...")
        await application.initialize()
        # Raha toa ka mila manomboka koa, dia ampidiro eto ny await application.start()
        # fa ny initialize no tena olana amin'ity Runtime Error ity
        
    if request.method == "POST":
        json_data = request.get_json(force=True)
        print("Received a webhook request!")
        print(f"Received JSON: {json_data}")
        update = Update.de_json(json_data, application.bot)
        
        await application.process_update(update) 
        
        return "ok", 200
    abort(403)

if __name__ == "__main__":
    # Hanomboka ny Flask app.
    # Ny initialization ny Telegram Application dia hikarakaraina ao anatin'ny webhook function.
    port = int(os.environ.get("PORT", 5000))
    print(f"Flask app running on port {port}")
    app.run(host="0.0.0.0", port=port)
