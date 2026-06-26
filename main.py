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

📈 <b>Prix :</b> ${data['price']}

🤖 Mise à jour automatique toutes les 30 minutes

🔗 <a href="{data['pair']}">Voir sur DexScreener</a>
"""

                send_or_edit_message(message)
                last_post = current_time
                print("✅ Message Telegram envoyé.")

        else:
            print("Aucune paire trouvée.")

    except Exception as e:
        print("Erreur :", e)

    time.sleep(CHECK_INTERVAL)
