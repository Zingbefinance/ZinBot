from config import CHECK_INTERVAL, POST_INTERVAL
from price import get_price
from telegram_sender import send_or_edit_message
import time
from datetime import datetime

print("🚀 ZinBot démarré")

last_post = 0

while True:
    try:
        data = get_price()

        if data:
            current_time = time.time()

            if current_time - last_post >= POST_INTERVAL:

                variation = float(data["change24h"])

                if variation >= 0:
                    tendance = "📈"
                    variation_txt = f"+{variation:.2f}%"
                else:
                    tendance = "📉"
                    variation_txt = f"{variation:.2f}%"

                update_time = datetime.utcnow().strftime("%H:%M UTC")

                message = f"""🪙 <b>ZING TOKEN (ZTC)</b>

💵 <b>Prix USD :</b> ${float(data['price']):.8f}
🟣 <b>Prix SOL :</b> {data['priceSol']} SOL

{tendance} <b>Variation 24h :</b> {variation_txt}

💎 <b>Market Cap :</b> ${float(data['marketcap']):,.2f}
💧 <b>Liquidité :</b> ${float(data['liquidity']):,.2f}
📊 <b>Volume 24h :</b> ${float(data['volume24h']):,.2f}

🟢 <b>Achats :</b> {data['buys24h']}
🔴 <b>Ventes :</b> {data['sells24h']}

🕒 <b>Mise à jour :</b> {update_time}

━━━━━━━━━━━━━━━

🌐 <b>Site :</b>
https://zingbefinance.com

✈️ <b>Telegram :</b>
https://t.me/Zingbefinanc

https://x.com/GogbeZingbe

🔗 <a href="{data['pair']}">DexScreener</a>

🤖 <i>Mise à jour automatique toutes les 30 minutes</i>
"""

                send_or_edit_message(message)
                last_post = current_time
                print("✅ Message Telegram envoyé.")

        else:
            print("Aucune paire trouvée.")

    except Exception as e:
        print("Erreur :", e)

    time.sleep(CHECK_INTERVAL)
