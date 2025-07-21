import os
import asyncio
from telegram.ext import Application

# Use the environment variable name (key), not the token itself.
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN") 
# Use the environment variable name (key) for WEBHOOK_URL.
WEBHOOK_URL = os.getenv("WEBHOOK_URL") 

async def main():
    application = (
        Application.builder()
        .token(TOKEN)
        .build()
    )

    # Initialize and start here as well
    await application.initialize() # 
    await application.start() # Add this, as it often goes with initialize 

    print(f"Setting webhook to: {WEBHOOK_URL}") # 
    try:
        await application.bot.set_webhook(url=WEBHOOK_URL) # 
        print("Webhook set successfully!") # [cite: 6]
    except Exception as e: # [cite: 6]
        print(f"Error setting webhook: {e}") # [cite: 6]
        webhook_info = await application.bot.get_webhook_info() # [cite: 6]
        print(f"Current Webhook Info: {webhook_info}") # [cite: 6]
        raise # Re-raise the exception so the build fails if webhook setup fails [cite: 6]

if __name__ == "__main__": # [cite: 6]
    asyncio.run(main()) # [cite: 6]
