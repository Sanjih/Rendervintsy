import os
import asyncio
from telegram.ext import Application

# Fenoy amin'ny Token tena izy avy amin'ny BotFather
TOKEN = "8092994458:AAHI1Ud1fh2E06VaXy6826Db0KH4KAstn6E" 

# Vakio avy amin'ny environment variable ny URL webhook
WEBHOOK_URL = os.getenv("WEBHOOK_URL", "https://telegram-bot-nk3n.onrender.com/webhook")

async def main():
    application = Application.builder().token(TOKEN).build()
    print(f"Setting webhook to: {WEBHOOK_URL}")
    await application.bot.set_webhook(url=WEBHOOK_URL)
    print("Webhook set successfully!")

if __name__ == "__main__":
    asyncio.run(main())