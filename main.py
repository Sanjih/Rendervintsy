import os
from flask import Flask, request, abort
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import asyncio # Mila ampidirina ity

TOKEN = "8092994458:AAHI1Ud1fh2E06VaXy6826Db0KH4KAstn6E" 

app = Flask(__name__)

# Mamorona ny Application object
application = Application.builder().token(TOKEN).build()

# ***** ATAOVY ETO NY FAMARITANA NY FUNCTION START *****
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Salama! Bot Telegram no nandray anao.")

# ***** ATAOVY ATO AORIAN'NY FAMARITANA NY START NY ADD_HANDLER *****
application.add_handler(CommandHandler("start", start))

# Ny initialization ny application dia mila atao eto na ao amin'ny `__main__`
# fa ny fomba tsara indrindra ho an'ny Render dia ny manao azy ao amin'ny set_webhook.py
# sy manomboka azy ao anaty webhook function raha mbola tsy started.
# Avelao ny application.initialize() sy application.start() ho an'ny set_webhook.py sy ny webhook()

@app.route("/")
def home():
    return "Bot is running!"

@app.route("/webhook", methods=["POST"])
async def webhook():
    # Hamarino raha efa nanomboka ny application.start()
    if not application.started:
        print("Application not started, starting now...")
        await application.start() # Atombohy raha mbola tsy nanomboka
        
    if request.method == "POST":
        json_data = request.get_json(force=True)
        print("Received a webhook request!")
        print(f"Received JSON: {json_data}")
        update = Update.de_json(json_data, application.bot)
        
        await application.process_update(update) 
        
        return "ok", 200
    abort(403)

if __name__ == "__main__":
    # Tokony efa voakarakaran'ny Render izany fa aleo apetraka eto raha misy ilana azy ho an'ny local
    # Ny `application.start()` dia tokony atao any amin'ny set_webhook.py ihany
    # na rehefa voaray ny fangatahana webhook voalohany.
    port = int(os.environ.get("PORT", 5000))
    print(f"Flask app running on port {port}")
    app.run(host="0.0.0.0", port=port)
