from config import CHECK_INTERVAL, POST_INTERVAL
from price import get_price
from telegram_sender import send_or_edit_message
import time

print("🚀 ZinBot démarré")

last_post = 0
last_price = None

while True:
    try:
        data = get_price()

        if data:
            current_time = time.time()

            # Envoi uniquement si le prix a changé
            if last_price != data["price"]:
                last_price = data["price"]

                if current_time - last_post >= POST_INTERVAL:

                    message = f"""
🪙 <b>ZING TOKEN (ZTC)</b>

💵 <b>Prix USD :</b> ${data['price']}
🟣 <b>Prix SOL :</b> {data['priceSol']} SOL

📈 <b>Variation 24h :</b> {data['change24h']}

💎 <b>Market Cap :</b> ${data['marketcap']}
💧 <b>Liquidité :</b> ${data['liquidity']}
📊 <b>Volume 24h :</b> ${data['volume24h']}

🟢 <b>Achats :</b> {data['buys24h']}
🔴 <b>Ventes :</b> {data['sells24h']}

🕒 <b>Mise à jour :</b> {time.strftime("%H:%M UTC", time.gmtime())}

━━━━━━━━━━━━━━

🌐 Site :
https://zingbefinance.com

✈️ Telegram :
https://t.me/Zingbefinanc

❌ X :
https://x.com/GogbeZingbe

🔗 DexScreener :
{data['pair']}
"""

                    send_or_edit_message(message)
                    last_post = current_time
                    print("✅ Message Telegram mis à jour")

                else:
                    print("⏳ Prix changé mais attente du prochain intervalle")

            else:
                print("😴 Aucun changement de prix")

        else:
            print("❌ Aucune paire trouvée")

    except Exception as e:
        print("Erreur :", e)

    time.sleep(CHECK_INTERVAL)         
