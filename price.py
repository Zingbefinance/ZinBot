import requests

MINT_ADDRESS = "4zihBzwHLx9z7aNmXam181iUd285xbqJNN57M5LhoHpu"

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
        "price": pair["priceUsd"],
        "marketcap": pair.get("marketCap", "0"),
        "liquidity": pair["liquidity"]["usd"],
        "volume24h": pair["volume"]["h24"],
        "pair": pair["url"]
    }


if __name__ == "__main__":

    print(get_price())
