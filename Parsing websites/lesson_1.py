import requests
from bs4 import BeautifulSoup
import csv
URL = 'https://coinmarketcap.com/'
LINK = 'https://coinmarketcap.com'


def get_html(url):
    r = requests.get(url)
    return r.text


def save(data):
    with open('data_table.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow((data['name'],
                         data['symbol'],
                         data['link'],
                         data['price']))


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find('tbody').find_all('tr')
    del trs[10]
    for tr in trs:
        tds = tr.find_all('td')
        name = tds[2].find('p', class_='Text-sc-1eb5slv-0').text
        symbol = tds[2].find('p', class_='Text-sc-1eb5slv-0 eweNDy coin-item-symbol').text
        link = LINK + tds[2].find('a', class_='cmc-link').get('href')
        price = tds[3].find('a').text
        data = {
            'name': name,
            'symbol': symbol,
            'link': link,
            'price': price
        }
        save(data)


def parse():
    print(get_data(get_html(URL)))


parse()
