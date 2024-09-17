import requests
import selectorlib
import os
import time

if not os.path.exists("data.txt"):
    with open("data.txt", 'w') as file:
        file.write("date,temperature" + '\n')

URL = "https://programmer100.pythonanywhere.com/"


def get_html(url):
    response = requests.get(url)
    return response.text


def scrape(data):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    content = extractor.extract(data)['temp']
    return content
    

if __name__ == "__main__":
    while True:
        html = get_html(URL)
        temperature = scrape(html)
        data = f"{time.strftime('%Y-%m-%d-%H-%M-%S')},{temperature}\n"
        with open("data.txt", "a") as file:
            file.write(data)
        time.sleep(5)