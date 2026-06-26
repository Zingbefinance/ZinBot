import os
import json
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

STATE_FILE = "state.json"


def load_state():
    try:
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    except:
        return {"message_id": None, "last_price": None}


def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f)


def send_or_edit_message(message):
    state = load_state()

    if state["message_id"] is None:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": CHAT_ID,
            "text": message,
            "parse_mode": "HTML"
        }

        response = requests.post(url, data=payload)
        data = response.json()

        if data.get("ok"):
            state["message_id"] = data["result"]["message_id"]
            save_state(state)

        return data

    else:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/editMessageText"
        payload = {
            "chat_id": CHAT_ID,
            "message_id": state["message_id"],
            "text": message,
            "parse_mode": "HTML"
        }

        response = requests.post(url, data=payload)
        return response.json()
