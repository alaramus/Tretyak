import sqlite3
import requests

api_url = "Подставить свой url"

def create_table():
    conn = None
    try:
        conn = sqlite3.connect('binance.sql')
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS user_data (value TEXT, comment TEXT)')
        conn.commit()
    except sqlite3.Error as e:
        error_message = f"SQLite error when creating table: {e}"
        print(error_message)
    finally:
        if conn:
            conn.close()

def insert_data(data):
    conn = None
    try:
        conn = sqlite3.connect('binance.sql')
        cur = conn.cursor()
        cur.execute('INSERT INTO user_data (value, comment) VALUES (?, ?)', data)
        conn.commit()
    except sqlite3.Error as e:
        error_message = f"SQLite error when populating table: {e}"
        print(error_message)
    finally:
        if conn:
            conn.close()

def get_api_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error working with API: {response.status_code}")
        return None

user_data_list = get_api_data(api_url)

if user_data_list:
    comments = ["Kline open time", "Open price", "High price", "Low price", "Close price", "Volume", "Kline Clone time", "Quote asset volume", "Number of trades", "Taker buy base asset volume", "Taker buy quote asset volume", "Unused field, ignore."]

    create_table()

    for user_input in user_data_list:
        for i in range(len(user_input)):
            value = f'"{user_input[i]}"' if isinstance(user_input[i], str) else user_input[i]
            data = value, comments[i]
            insert_data(data)
else:
    print("No data received from API.")
