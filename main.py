import requests
import selectorlib
import os
import time
import sqlite3

if not os.path.exists("data.db"):
    with open("data.db", 'w') as file:
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE temperature (date TEXT, temperature REAL)")
else:
    connection = sqlite3.connect("data.db") 

URL = "https://programmer100.pythonanywhere.com/"


def get_html(url):
    response = requests.get(url)
    return response.text


def scrape(data):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    content = extractor.extract(data)['temp']
    return content
    

def write(date, temperature):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO temperature VALUES (?,?)", (date, temperature))
    connection.commit()

if __name__ == "__main__":
    while True:
        html = get_html(URL)
        temperature = scrape(html)
        date = time.strftime('%Y-%m-%d-%H-%M-%S')
        write(date, temperature)
        time.sleep(5)