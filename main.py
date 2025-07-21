import os
from flask import Flask, request, abort
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8092994458:AAHI1Ud1fh2E06VaXy6826Db0KH4KAstn6E"
WEBHOOK_URL = os.getenv("https://web-production-760a2.up.railway.app/webhook")

app = Flask(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Salama! Bot Telegram no nandray anao.")

application = Application.builder().token(TOKEN).build()
application.add_handler(CommandHandler("start", start))

@app.route("/webhook", methods=["POST"])
def webhook():
    if request.method == "POST":
        json_data = request.get_json(force=True)
        update = Update.de_json(json_data, application.bot)
        application.process_update(update)
        return "ok", 200
    abort(403)

if __name__ == "__main__":
    application.initialize()
    application.bot.set_webhook(WEBHOOK_URL)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
