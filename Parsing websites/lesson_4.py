import requests
from bs4 import BeautifulSoup
import csv
def get_html(url):
    r = requests.get(url)
    if r.ok:
        return r.text
    print(r.status_code)


def save_file(data):
    with open('coin_market_cam', 'a') as file:
        writer = csv.writer(file)
        writer.writerow((data['name'], data['price']))


def content(html):
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find('table', class_='cmc-table cmc-table___11lFC cmc-table-homepage___2_guh').find('tbody')
    trs = table.find_all('tr')
    for tr in trs:
        tds = tr.find_all('td')
        try:
            name = tds[2].find('p', class_='Text-sc-1eb5slv-0 iTmTiC').text
        except:
            continue
        try:
            price = tds[3].find('a', class_='cmc-link').text.replace('$', '')
        except:
            continue
        data = {
            'name': name,
            'price': price
        }
        save_file(data)

def parse():
    link = 'https://coinmarketcap.com/{}/'
    for i in range(1, 40):
        content(get_html(link.format(i)))

parse()
