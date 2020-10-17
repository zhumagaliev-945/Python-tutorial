import requests
from bs4 import BeautifulSoup
import json

URL = 'https://auto.ria.com/newauto/marka-jeep/'
HEADERS = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0', 'accept': '*/*'}
HOST = 'https://auto.ria.com'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    card = soup.find_all('div', class_='proposition')
    cars = []

    for item in card:
        title = item.find('div', class_='proposition_title')
        h3 = title.find('h3')
        link = h3.find('a')
        cars.append({
            'title': h3.get_text(strip=True),
            'link': HOST + link.get('href'),
            'price': item.find('span', class_='green').get_text(strip=True)
        })
    print(json.dumps(cars, indent=2))
    # print(len(cars))


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        return "ERROR"
parse()
