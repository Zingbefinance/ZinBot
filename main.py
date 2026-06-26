
from config import CHECK_INTERVAL, POST_INTERVAL
from price import get_price
from telegram_sender import send_or_edit_message
import time

print("🚀 ZinBot démarré")

last_post = 0

while True:
    try:
        data = get_price()

        if data:
            current_time = time.time()

            if current_time - last_post >= POST_INTERVAL:

                message = f"""💰 <b>ZING TOKEN</b>

📈 Prix actuel : <b>${data['price']}</b>
⏰ Mise à jour automatique

🔗 https://dexscreener.com/solana/{data['pair']}
"""

                send_or_edit_message(message)
                last_post = current_time
                print("✅ Message Telegram mis à jour.")

        else:
            print("Le token n'a pas encore de paire active.")

    except Exception as e:
        print("Erreur :", e)

    time.sleep(CHECK_INTERVAL)
