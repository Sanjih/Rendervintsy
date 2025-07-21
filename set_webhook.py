import os
import asyncio
from telegram.ext import Application

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "8092994458:AAHI1Ud1fh2E06VaXy6826Db0KH4KAstn6E") 
WEBHOOK_URL = os.getenv("WEBHOOK_URL", "https://telegram-bot-nk3n.onrender.com/webhook") # Tokony ho hita ao amin'ny Render io URL io

async def main():
    application = (
        Application.builder()
        .token(TOKEN)
        .build()
    )

    # initialize-na eto koa, satria Build Command ity
    await application.initialize() 

    print(f"Setting webhook to: {WEBHOOK_URL}")
    try:
        await application.bot.set_webhook(url=WEBHOOK_URL)
        print("Webhook set successfully!")
    except Exception as e:
        print(f"Error setting webhook: {e}")
        # Mety ilaina ny mamoaka exception eto raha diso ny fametrahana webhook
        # raise e 

if __name__ == "__main__":
    asyncio.run(main())
