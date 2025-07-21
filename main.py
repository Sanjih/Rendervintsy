import os
from flask import Flask, request, abort
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import asyncio # Mila ampidirina ity

TOKEN = "8092994458:AAHI1Ud1fh2E06VaXy6826Db0KH4KAstn6E" 
# Esory ity tsipika ity. Tsy ilaina eto intsony ny WEBHOOK_URL.
# WEBHOOK_URL = os.getenv("https://vintsy.onrender.com/webhook")

app = Flask(__name__)

# Mamorona ny Application object
application = Application.builder().token(TOKEN).build()

# Manao initialize ny application ao anatin'ny asyncio event loop
# Ampiasao ity mba hahazoana antoka fa voaantso tsara ny initialize
async def init_application():
    await application.initialize()

# Mampiasa loop_initialized mba hiantsoana ny init_application mandeha ho azy
# alohan'ny hanombohana ny Flask server.
# Ity dia fomba iray hiantsoana async function ao anatin'ny synchronous code.
# Na izany aza, ity fomba ity dia mety miteraka olana hafa amin'ny flask raha tsy ampiasaina tsara.
# Mety ho tsara kokoa ny mamindra ny initialization ho any amin'ny context iray hafa.

# Vahaolana tsara kokoa ho an'ny Flask sy Async:
# Ampiasao ny Application.start() sy Application.stop() amin'ny alalan'ny Flask lifecycle
# Izany dia hialana amin'ny fampiasana asyncio.run() izay mety hiteraka fifanolanana.

# Aleo izao ampidiro ny handlers aloha
application.add_handler(CommandHandler("start", start))

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Salama! Bot Telegram no nandray anao.")

@app.route("/")
def home():
    return "Bot is running!"

@app.route("/webhook", methods=["POST"])
async def webhook():
    # Raha mbola miseho ny RuntimeWarning, dia mety mila manomboka ny application eto isika
    # na miantoka fa efa nanomboka izy tany aloha.
    if not application.started: # Hamarino raha efa nanomboka ny application
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
    # Hanomboka ny application rehefa manomboka ny server.
    # Izany dia hiantoka fa initialized sy started ny application.
    asyncio.run(application.start()) 
    
    port = int(os.environ.get("PORT", 5000))
    print(f"Flask app running on port {port}")
    app.run(host="0.0.0.0", port=port)
