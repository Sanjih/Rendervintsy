import os
import asyncio
from telegram.ext import Application

TOKEN = "8092994458:AAHIlUdlfh2E06VaXy6826Db0KH4KAstn6E" 
WEBHOOK_URL = os.getenv("WEBHOOK_URL", "https://telegram-bot-nk3n.onrender.com")

async def main():
    # Ity no tsipika manana olana
    # application = Application.builder().token(TOKEN).build()
    
    # Andramo ity fomba ity izay azo antoka kokoa amin'ny fanombohana application amin'ny v20+
    application = (
        Application.builder()
        .token(TOKEN)
        .build()
    )

    print(f"Setting webhook to: {WEBHOOK_URL}")
    try:
        await application.bot.set_webhook(url=WEBHOOK_URL)
        print("Webhook set successfully!")
    except Exception as e:
        print(f"Error setting webhook: {e}")
        # Aza ajanona ny dingana Build raha tsy azo atao ny mametraka ny webhook, 
        # fa mety efa napetraka izany teo aloha.
        # Afaka mampiasa get_webhook_info ianao mba hijerena raha napetraka izany
        webhook_info = await application.bot.get_webhook_info()
        print(f"Current Webhook Info: {webhook_info}")
        if webhook_info.url != WEBHOOK_URL:
            print("Webhook URL mismatch, retrying or manual intervention needed.")
            # Mety ho te hamoaka exception eto ianao raha tena ilaina ny fametrahana webhook vaovao.

if __name__ == "__main__":
    asyncio.run(main())
