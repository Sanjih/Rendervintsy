import os
from flask import Flask, request, abort
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import asyncio 

# Use the environment variable name (key), not the token itself.
# Make sure to set TELEGRAM_BOT_TOKEN in Render's environment variables.
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN") 

app = Flask(__name__)

# Create the Application object.
application = Application.builder().token(TOKEN).build() # [cite: 2]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Salama! Bot Telegram no nandray anao.")

application.add_handler(CommandHandler("start", start))

@app.route("/")
def home():
    return "Bot is running!"

@app.route("/webhook", methods=["POST"])
async def webhook(): # 
    # Start the Application if it's not already running (works for v21.x)
    if not application.started: # 
        print("Application not started, initializing and starting now...") # 
        await application.initialize() # 
        await application.start() # Start the application 
        
    if request.method == "POST": # 
        json_data = request.get_json(force=True) # 
        print("Received a webhook request!") # 
        print(f"Received JSON: {json_data}") # [cite: 4]
        update = Update.de_json(json_data, application.bot) # [cite: 4]
        
        await application.process_update(update) # [cite: 4]
        
        return "ok", 200 # [cite: 4]
    abort(403) # [cite: 4]

if __name__ == "__main__": # [cite: 4]
    port = int(os.environ.get("PORT", 5000)) # [cite: 4]
    print(f"Flask app running on port {port}") # [cite: 4]
    app.run(host="0.0.0.0", port=port) # [cite: 4]
