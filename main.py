import os
from flask import Flask, request, abort
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Fenoy amin'ny Token tena izy avy amin'ny BotFather
TOKEN = "8092994458:AAHIlUdlfh2E06VaXy6826Db0KH4KAstn6E" 

# Vakio avy amin'ny environment variable ny URL webhook, na apetraho mivantana
# Tsara kokoa ny mametraka azy ho environment variable ao amin'ny Render
WEBHOOK_URL = os.getenv("WEBHOOK_URL", "https://vintsy.onrender.com/webhook")

app = Flask(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Salama! Bot Telegram no nandray anao.")

# Ataovy global ny application object mba ho azo avy amin'ny webhook function
application = Application.builder().token(TOKEN).build()
application.add_handler(CommandHandler("start", start))

@app.route("/webhook", methods=["POST"])
def webhook():
    if request.method == "POST":
        # Ampiasao ny webhook_update_queue an'ny application
        update = Update.de_json(request.get_json(force=True), application.bot)
        application.update_queue.put(update)  # Ampidirina ao anaty queue ilay update
        return "ok", 200
    abort(403)

if __name__ == "__main__":
    # Tsy mila application.initialize() sy application.bot.set_webhook() eto
    # Satria ny Render no miantso ny /webhook endpoint
    # Ny fanombohana ny application dia atao rehefa voaray ny update voalohany
    
    # Raha te hanao debug ianao amin'ny local, dia azonao atao ny mampiasa polling
    # application.run_polling(poll_interval=3) 
    
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
