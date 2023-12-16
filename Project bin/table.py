import sqlite3
import requests

api_url = "https://api.binance.com/api/v3/klines?interval=1d&limit=1000&startTime=1695104800000&endTime=1696204800000&symbol=BTCUSDT"

def create_table():
    try:
        with sqlite3.connect('binance2.sql') as conn:             #когда выполнение выходит из блока with, соединение закрывается.cоздание соединения с базой данных
            cur = conn.cursor()                                  #cоздание объекта курсора. позволяет выполнять SQL-запросы
            cur.execute('CREATE TABLE IF NOT EXISTS kline_data (Time FLOAT, Open FLOAT, High FLOAT, Low FLOAT, Close FLOAT, Volume FLOAT)')       # execute принимает SQL-запрос в качестве аргумента и выполняет этот запрос
            conn.commit()
    except sqlite3.Error as error:
        print(f'SQLite error when create table: {error}')

def insert_data(data):
    try:
        with sqlite3.connect('binance2.sql') as conn:
            cur = conn.cursor()
            cur.execute('INSERT INTO kline_data (Time, Open, High, Low, Close, Volume) VALUES (?, ?, ?, ?, ?, ?)', data)   # записывает в data по одной строке
            conn.commit()
    except sqlite3.Error as error:
        print(f'Error inserting data: {error}')

def clear_table():
    try:
        with sqlite3.connect('binance2.sql') as conn:
            cur = conn.cursor()
            cur.execute('DELETE FROM kline_data')        # SQL-запрос для очистки таблицы
            conn.commit()
    except sqlite3.Error as error:
        print(f'Error clear data: {error}')

def find_difference():
    try:
        with sqlite3.connect('binance2.sql') as conn:
            cur = conn.cursor()
            cur.execute('SELECT MAX(High), MAX(Low) FROM kline_data')         #('28580.00000000', '27281.44000000')
            result = cur.fetchone()                      #почему fetchall ?
            print(result)
            max_high, max_low = result
            if max_high > max_low:
                difference = float(max_high) - float(max_low)
                return f'Maximum High value(by using SQL): {max_high}\nMaximum Low value(by using SQL): {max_low}\nDifference(by using SQL):{difference}'
            else:
                print("Error: Max High should be greater than Max Low.")
    except sqlite3.Error as error:
        print(f'Error finding max values: {error}')
###################################################################################################

def calculate_price_difference(data):
    def extract_high(table):
        return float(table[2])

    def extract_low(table):
        return float(table[3])

    print(f'list in: {data}')

    high_values = list(map(extract_high, data))                 #функция, которую нужно применить к каждому элементу, последовательность (список, кортеж, строка)
    low_values = list(map(extract_low, data))
    print(f'list out: {high_values}')

    # def get_max_values(values):
    #     return max(values)
    #
    # max_high = get_max_values(high_values)
    # max_low = get_max_values(low_values)


    def get_max_values(numbers):
        def num_max(x):
            return x == max(numbers)

        max_numbers = filter(num_max, numbers)
        return float(next(max_numbers))                  #что такое next ?

    # def get_max_values(numbers):
    #     def is_not_none(x):         #функция- фильтр
    #         return x is not None
    #
    #     not_none_numbers = filter(is_not_none, numbers)     #функция- фильтр, объект
    #
    #     return max(not_none_numbers)

    max_high = get_max_values(high_values)
    max_low = get_max_values(low_values)

    if max_high > max_low:
        difference = max_high - max_low
        return f'Maximum High value(by using map and filter): {max_high}\nMaximum Low value(by using map and filter): {max_low}\nDifference(by using map and filter):{difference}'
    else:
        return f'Maximum Low value should be greater than Max'

###################################################################################################
def get_api_data(api_url):
    response = requests.get(api_url)                # ответ от сервера после отправки GET-запроса по указанному URL
    if response.status_code == 200:
        return response.json()                      #функция возвращает данные в формате JSON из ответа
    else:
        print(f"Error working with API: {response.status_code}")

user_data_list = get_api_data(api_url)

if user_data_list:                     #проверяет не пуст ли список. Если не пуст условие считается истинным

    clear_table()

    create_table()

    for user_input in user_data_list:                           #цикл выполняет итерацию по элементам user_data_list,для каждого элемента выполнится следующий блок кода!
        data = [(user_input[i]) for i in range(0, 6)]           #для каждого user_input (один элемент из API данных) создается список data
        insert_data(data)

    print(find_difference())

    price_difference = calculate_price_difference(user_data_list)
    print(price_difference)
else:
    print("No data received from API.")
