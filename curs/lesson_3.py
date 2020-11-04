import requests
from bs4 import BeautifulSoup
import csv
header_link = 'https://supersliv.biz/'


def get_html(url):
    r = requests.get(url)
    return r.text


def save(data):
    with open('supersliv.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((
            data['name'],
            data['url']
        ))


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    ol = soup.find('ol', class_='discussionListItems')
    lis = ol.find_all('li', class_='discussionListItem')
    for li in lis:
        try:
            name = li.find('a', class_='PreviewTooltip').text
            url = header_link + li.find('a', class_='PreviewTooltip').get('href')
        except:
            name = ''
            url =''

        data = {
            'name': name,
            'url': url
        }
        save(data)

def parse():
    link = 'https://supersliv.biz/forums/administrirovanie-i-programmirovanie.34/page-{}'
    for i in range(1, 60):
        url = link.format(str(i))
        html = get_html(url)
        data = get_data(html)
        print(data)

parse()
