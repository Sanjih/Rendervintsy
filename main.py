import os
from flask import Flask, request, abort
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Fenoy amin'ny Token tena izy avy amin'ny BotFather
TOKEN = "8092994458:AAHI1Ud1fh2E06VaXy6826Db0KH4KAstn6E" 

# Tsy ilaina eto intsony ny WEBHOOK_URL satria ny set_webhook.py no mikarakara azy
# WEBHOOK_URL = os.getenv("WEBHOOK_URL", "https://telegram-bot-nk3n.onrender.com")

app = Flask(__name__)

# Mamorona ny Application object eo am-piandohana
application = Application.builder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Salama! Bot Telegram no nandray anao.")

application.add_handler(CommandHandler("start", start))

@app.route("/")
def home():
    return "Bot is running!"

@app.route("/webhook", methods=["POST"])
async def webhook():
    if request.method == "POST":
        json_data = request.get_json(force=True)
        update = Update.de_json(json_data, application.bot)

        # Mampiasa process_update_async izay async
        await application.process_update(update) 

        return "ok", 200
    abort(403)

if __name__ == "__main__":
    # Ny Flask server ihany no atao run eto
    port = int(os.environ.get("PORT", 5000))
    print(f"Flask app running on port {port}")
    app.run(host="0.0.0.0", port=port)
