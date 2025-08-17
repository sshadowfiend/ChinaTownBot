import requests
from bs4 import BeautifulSoup


url = 'https://www.google.com/search?client=opera-gx&q=курс+юаня+к+рублю&sourceid=opera&ie=UTF-8&oe=UTF-8'
headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0'}


def check_rate() -> float:
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    data = soup.find('span', class_='DFlfde SwHCTb')
    exchange_rate = float(data.text.replace(',', '.'))
    return exchange_rate











