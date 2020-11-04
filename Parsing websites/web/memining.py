import requests
from bs4 import BeautifulSoup
link = 'https://www.poolin.com/my/9065404/btc/miners?group_id=0&page_size=30&read_token=wowavddEViQIGPBjeMWsHsmrdPov13xbjg7tJFprSKNsw1a1UorPGGhzKbX1fZWM'


def get_html(url):
    r = requests.get(url)
    return r.text


def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find('div', class_='p15')
    some = div.find('table', class_='el-table__header').text
    return some


def parse():
    print(get_data(get_html(link)))


parse()
