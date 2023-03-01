import requests
from bs4 import BeautifulSoup as bs
import time
from multiprocessing import Pool

def get_soup(sku = None):

    url = f'https://www.leroymerlin.pl/szukaj.html?q={sku}&sprawdz=true'
    response = requests.get(url)
    soup = bs(response.text, 'lxml')
    return soup


def get_price(sku):
    soup = get_soup(sku)
    if soup:
        try:
            sale_price = soup.find('div', class_='product-right-data').find('span', class_='product-price').get('data-price')
            return(sku,sale_price)
        except:
            
            return(sku,0)
            

def get_all_price(skuls):
    resolt = []
    if skuls:
        seconds = time.time()
        # for sku in skuls.split(';'):
        #     resolt.append((sku, ' - ', get_price(sku)))
        # print(time.time() - seconds)

        with Pool(10) as p:
            prise = p.map(get_price, skuls.split(";"))
        
        for i in prise:
            print(i[0], " - ", i[1])
    
        print(time.time() - seconds)
if __name__ == '__main__':

    get_all_price(";")