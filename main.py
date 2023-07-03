import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
url="https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
page=urlopen(url)
html_code = page.read().decode('utf-8')
soup=BeautifulSoup(html_code,'html.parser')
models=soup.find_all('a',class_='title')
prices=soup.find_all('h4',class_='pull-right price')
konfs=soup.find_all('p',class_='description')
with open('laptops.csv','w', encoding='utf-8') as file:
    file.write(f'Модель;Описание;Цена\n')
    for m, d, p in zip(models, konfs, prices):
        file.write(f"{m['title']};{d.get_text()};{p.get_text()}\n")