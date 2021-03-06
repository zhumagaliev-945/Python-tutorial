import requests
from bs4 import BeautifulSoup
import csv
URL = 'https://kolesa.kz/cars/mercedes-benz/s-320/taraz/'
HEADERS = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0',
           'accept': '*/*'}
LINK = 'https://kolesa.kz'
FILE = 'cars.csv'


def get_html(url, parameters=None):
    r = requests.get(url, headers=HEADERS, params=parameters)
    return r


def get_count_pages(html):
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find('div', class_='pager')
    if div:
        more = div.find('ul').find_all('li')
        return int(more[-1].get_text())
    if div is None:
        return 1


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    cards = soup.find_all('div', class_='a-info-side')
    cars = []
    for data in cards:
        cars.append({
            'title': data.find('span', class_='a-el-info-title').get_text(strip=True),
            'link': LINK + data.find('a', class_='ddl_product_link').get('href'),
            'price': data.find('span', class_='price').get_text(strip=True).replace('<span class="curr-sign">', ''),
            'currency': data.find('span', class_='curr-sign').get_text(),
            'city': data.find('div', class_='list-region').get_text(strip=True),



        })
    return cars


def save(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Model', 'Link', 'Price', 'Currency', 'City'])
        for ob in items:
            writer.writerow([ob['title'], ob['link'], ob['price'], ob['currency'], ob['city']])


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        collect = []
        pages = get_count_pages(html.text)
        for number in range(1, pages + 1):
            get_result = get_html(URL, parameters={'page': number})
            output = get_content(get_result.text)
            collect.extend(output)
        save(collect, FILE)
    else:
        print("Error >>> <br> Link is not correct")


parse()
