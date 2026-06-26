from config import CHECK_INTERVAL, POST_INTERVAL
from price import get_price
from telegram_sender import send_message
import time

print("🚀 ZinBot démarré")

last_post = 0
last_price = None

while True:
    try:
        data = get_price()

        if data:
            current_time = time.time()

            # Envoie uniquement si le prix a changé
            if last_price != data["price"]:
                last_price = data["price"]

                # Respecte l'intervalle minimum entre deux publications
                if current_time - last_post >= POST_INTERVAL:
                    send_message(data)
                    last_post = current_time
                    print("📤 Nouveau prix envoyé :", data["price"])
                else:
                    print("⏳ Prix changé mais intervalle non atteint.")
            else:
                print("⏸️ Aucun changement de prix.")

        else:
            print("❌ Aucune paire active trouvée.")

    except Exception as e:
        print("Erreur :", e)

    time.sleep(CHECK_INTERVAL)

                

                




            
