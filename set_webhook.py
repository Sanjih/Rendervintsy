import os
import asyncio
from telegram.ext import Application

TOKEN = "8092994458:AAHIlUdlfh2E06VaXy6826Db0KH4KAstn6E" 
WEBHOOK_URL = os.getenv("WEBHOOK_URL", "https://telegram-bot-nk3n.onrender.com/webhook")

async def main():
    application = (
        Application.builder()
        .token(TOKEN)
        .build()
    )

    # initialize-na eto koa
    await application.initialize() # <--- ATAOVY AZO ANTOKA FA await-ina ity

    print(f"Setting webhook to: {WEBHOOK_URL}")
    try:
        await application.bot.set_webhook(url=WEBHOOK_URL)
        print("Webhook set successfully!")
    except Exception as e:
        print(f"Error setting webhook: {e}")
        # Azo ampiana code fanampiny eto hijerena ny webhook_info raha ilaina
        # webhook_info = await application.bot.get_webhook_info()
        # print(f"Current Webhook Info: {webhook_info}")

if __name__ == "__main__":
    asyncio.run(main())
