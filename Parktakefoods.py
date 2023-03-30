import pandas as pd
import requests as r
from bs4 import BeautifulSoup as bs

main_url = 'https://partakefoods.com/collections/all'

res = r.get(main_url)
# print(res.status_code)

soup = bs(res.text, 'html.parser')
# print(soup)

products = soup.find_all('div', {'class': 'card-information__wrapper'})

product_list = []

for product in products:
    product_name = product.find('h3').text
    product_names = product_name.replace('\n',"")
    product_price = product.find('span', {'class': 'price-item price-item--regular'}).text
    products_price = product_price.replace('$',"").replace('From',"").strip()
    # review_count = product.find('div', {'class': 'bv_averageRating_component_container'}).text

    prodduct_data = {
        'Product_Name': product_names,
        'Product_Price': products_price
    }

    product_list.append(prodduct_data)

df = pd.DataFrame(product_list)
df.to_csv('Product_information.csv', index=False)