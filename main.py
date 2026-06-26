from config import CHECK_INTERVAL, POST_INTERVAL
from price import get_price
import time
print("🚀 ZinBot démarré")
last_post = 0
from config import CHECK_INTERVAL, POST_INTERVAL
last_post = 0
from price import get_price
import time

print("🚀 ZinBot démarré")

while True:
    try:
        data = get_price()

        if data:
            print("Prix :", data["price"])
            print("Market Cap :", data["marketcap"])
            print("Liquidité :", data["liquidity"])
            print("Volume 24h :", data["volume24h"])
            print("------------------------")
        else:
            print("Le token n'a pas encore de paire active.")

    except Exception as e:
        print("Erreur :", e)

    time.sleep(CHECK_INTERVAL)
