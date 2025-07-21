import os
from flask import Flask, request, abort
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import asyncio 

# Tena asaina mampiasa Environment Variable ho an'ny token
TOKEN = os.getenv("8092994458:AAGlzk0nJf3Yb4PsHQXh79Fr9r0oiHL0QZo") # Esory ny default value raha efa napetraka ao amin'ny Render

app = Flask(__name__)

# Mamorona ny Application object. Tsy initialize na start-ina eto.
application = Application.builder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Salama! Bot Telegram no nandray anao.")

application.add_handler(CommandHandler("start", start))

@app.route("/")
def home():
    return "Bot is running!"

@app.route("/webhook", methods=["POST"])
async def webhook():
    # Fanombohana ny Application raha mbola tsy started (miasa amin'ny v21.x)
    if not application.started:
        print("Application not started, initializing and starting now...")
        await application.initialize()
        await application.start() # Atombohy ny application
        
    if request.method == "POST":
        json_data = request.get_json(force=True)
        print("Received a webhook request!")
        print(f"Received JSON: {json_data}")
        update = Update.de_json(json_data, application.bot)
        
        await application.process_update(update) 
        
        return "ok", 200
    abort(403)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"Flask app running on port {port}")
    app.run(host="0.0.0.0", port=port)
