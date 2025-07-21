import os
from flask import Flask, request, abort
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import asyncio # Mila ampidirina ity

# Fenoy amin'ny Token tena izy avy amin'ny BotFather
TOKEN = "8092994458:AAHIlUdlfh2E06VaXy6826Db0KH4KAstn6E" 

app = Flask(__name__)

# Mamorona ny Application object eo am-piandohana
# Hanao initialization sy startup izy rehefa voaray ny fangatahana voalohany
application = Application.builder().token(TOKEN).build()

# ***** FAMARITANA NY FUNCTION START ALOHA NY ADD_HANDLER *****
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Salama! Bot Telegram no nandray anao.")

application.add_handler(CommandHandler("start", start))

@app.route("/")
def home():
    return "Bot is running!"

@app.route("/webhook", methods=["POST"])
async def webhook(): # Ataovy async ity function ity
    # Raha toa ka mbola tsy initialized ny application, ataovy izao
    if not application.check_running(): # Ampiasaina `check_running` ho solon'ny `started` (v20.x)
        print("Application not running, initializing and starting now...")
        await application.initialize()
        await application.start() # Atombohy ny application
        
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

# Raha te hanao debug ianao amin'ny local, dia azonao atao ny mampiasa ity block ity
if __name__ == "__main__":
    # Ny Flask server ihany no atao run eto
    port = int(os.environ.get("PORT", 5000))
    print(f"Flask app running on port {port}")
    app.run(host="0.0.0.0", port=port)
