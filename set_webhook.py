import os
import asyncio
from telegram.ext import Application

TOKEN = os.getenv("8092994458:AAGlzk0nJf3Yb4PsHQXh79Fr9r0oiHL0QZo")
WEBHOOK_URL = os.getenv("https://telegram-bot-nk3n.onrender.com/webhook")

async def main():
    application = (
        Application.builder()
        .token(TOKEN)
        .build()
    )

    # Initialize sy start eto koa
    await application.initialize() 
    await application.start() # Ampio ity, satria miaraka amin'ny initialize matetika

    print(f"Setting webhook to: {WEBHOOK_URL}")
    try:
        await application.bot.set_webhook(url=WEBHOOK_URL)
        print("Webhook set successfully!")
    except Exception as e:
        print(f"Error setting webhook: {e}")
        # Raha misy olana, jereo ny info momba ny webhook
        webhook_info = await application.bot.get_webhook_info()
        print(f"Current Webhook Info: {webhook_info}")
        raise # Avereno ny exception mba tsy hahomby ny build

if __name__ == "__main__":
    asyncio.run(main())
