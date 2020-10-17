import requests
from bs4 import BeautifulSoup
import json



URL = 'https://cointech.kz/miners'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0',
    'accept': '*/*'
}



def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    card = soup.find_all('div', class_='t776__col')
    miners = []

    for item in card:
        div = item.find('div', class_='t776__title').find_next('div')
        title = div.find('strong').get_text()
        miners.append({
            'title': title,
            'price': item.find('div', class_='t776__price-value').get_text()

        })
    print(json.dumps(miners, indent=2))
    # print(len(cars))


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        return "ERROR"
parse()

