import requests
from bs4 import BeautifulSoup
link = 'https://ru.wordpress.org/plugins/'


def get_html(url):
    response = requests.get(url)
    return response.text


def split(string):
    r = string.split()
    return r


def data(html):
    soup = BeautifulSoup(html, 'lxml')
    sections = soup.find_all('section', class_='plugin-section')[1]
    cards = sections.find_all('article', class_='plugin-card')
    info_cards  = []
    for item in cards:
        info_cards.append({
            'title': item.find('h3', class_='entry-title').find('a').text,
            'vote': item.find('span', class_='rating-count').find('a').get_text(),
            'author': item.find('span', class_='plugin-author').text,
            'href': item.find('h3', class_='entry-title').find('a')
        })
    print(info_cards)


def parser():
    print(data(get_html(link)))


parser()
