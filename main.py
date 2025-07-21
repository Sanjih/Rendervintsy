import os
from flask import Flask, request, abort
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import asyncio 

TOKEN = "8092994458:AAHIlUdlfh2E06VaXy6826Db0KH4KAstn6E" 

app = Flask(__name__)

# Mamorona ny Application object
application = Application.builder().token(TOKEN).build()

# ***** ATAOVY ETO NY FAMARITANA NY FUNCTION START *****
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Salama! Bot Telegram no nandray anao.")

# ***** ATAOVY ATO AORIAN'NY FAMARITANA NY START NY ADD_HANDLER *****
application.add_handler(CommandHandler("start", start))

# Initialization ny application. Tokony ho vita tsara izany raha toa ka mandeha tsara ny set_webhook.py.
# Raha mbola misy olana "Application not initialized", dia mety mila apetraka eto koa
# application.initialize() # Mety ilaina indray ity raha mbola misy Runtime Error

@app.route("/")
def home():
    return "Bot is running!"

@app.route("/webhook", methods=["POST"])
async def webhook():
    # ***** ESORY ITY BLOC ITY SATRIA TSY MISY 'STARTED' AMIN'NY V20.X *****
    # if not application.started:
    #     print("Application not started, starting now...")
    #     await application.start() 
    
    # Tokony efa initialized sy started ny application raha nandeha tsara ny set_webhook.py
    # ary raha ampiasaina araka ny tokony ho izy ny Start Command an'ny Render.

    if request.method == "POST":
        json_data = request.get_json(force=True)
        print("Received a webhook request!")
        print(f"Received JSON: {json_data}")
        update = Update.de_json(json_data, application.bot)
        
        # Mety ilaina ny miantso application.start() na application.initialize() aloha eto
        # raha tsy voakarakara tsara ny startup amin'ny Render.
        # Nefa tokony efa voakarakaran'ny set_webhook.py izany.
        
        await application.process_update(update) 
        
        return "ok", 200
    abort(403)

if __name__ == "__main__":
    # Raha mbola misy RuntimeWarning: coroutine 'Application.initialize' was never awaited,
    # dia mety mila ampiana eto ny asyncio.run(application.initialize())
    # na asyncio.run(application.start()) arakaraka ny filany.
    # Nefa ny fomba tsara indrindra ho an'ny Render dia ny miantoka fa ny set_webhook.py
    # no manao ny fanombohana voalohany.

    port = int(os.environ.get("PORT", 5000))
    print(f"Flask app running on port {port}")
    app.run(host="0.0.0.0", port=port)
