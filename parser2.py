import requests
from bs4 import BeautifulSoup



URL = 'https://cointech.kz/miners'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0',
    'accept': '*/*'
}



def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def parser2():
    html = get_html(URL)
    if html.status_code == 200:
        print(html.text)
    else:
        print("ERROR")
parser2()

