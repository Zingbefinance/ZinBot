import sqlite3

conn = sqlite3.connect("zingbot.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS settings(
    id INTEGER PRIMARY KEY,
    message_id INTEGER
)
""")

conn.commit()


def get_message_id():
    cursor.execute("SELECT message_id FROM settings WHERE id=1")
    row = cursor.fetchone()

    if row:
        return row[0]

    return None


def save_message_id(message_id):
    cursor.execute(
        "INSERT OR REPLACE INTO settings(id,message_id) VALUES(1,?)",
        (message_id,)
    )
    conn.commit()
