import requests
import os

MINT_ADDRESS = os.getenv("MINT_ADDRESS")

def get_price():
    url = f"https://api.dexscreener.com/latest/dex/tokens/{MINT_ADDRESS}"

    r = requests.get(url)

    if r.status_code != 200:
        return None

    data = r.json()

    if "pairs" not in data or len(data["pairs"]) == 0:
        return None

    pair = data["pairs"][0]

    return {
        "price": pair.get("priceUsd", "0"),
        "priceSol": pair.get("priceNative", "0"),
        "marketcap": pair.get("marketCap", 0),
        "liquidity": pair.get("liquidity", {}).get("usd", 0),
        "volume24h": pair.get("volume", {}).get("h24", 0),
        "change24h": pair.get("priceChange", {}).get("h24", 0),
        "buys24h": pair.get("txns", {}).get("h24", {}).get("buys", 0),
        "sells24h": pair.get("txns", {}).get("h24", {}).get("sells", 0),
        "pair": pair.get("url", "")
    }
