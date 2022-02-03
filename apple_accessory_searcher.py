import requests
from requests import exceptions
from bs4 import BeautifulSoup
from urllib.error import HTTPError


def get_search_results(product: str):
    try:
        # Store desired product, format URL
        URL = "https://www.apple.com/us/search/{0}?src=alp"
        product = product.replace(" ", "-")
        URL = URL.format(product)

        # Request page and instantiate bs4 object
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")

        # search for all product results
        product_results = soup.find_all('div', class_="rf-producttile-info")

        # store product data, return dictionary if results are present
        all_products = []
        if len(product_results) > 0:
            for p in product_results:
                product_name = p.find('h2', class_="rf-producttile-name").text.strip()
                product_price = p.find('span', class_="rf-producttile-pricecurrent").text.strip()
                all_products.append({
                    "name": product_name,
                    "price": product_price,
                })
            return all_products
    except (HTTPError, requests.exceptions.RequestException, ValueError):
        return None


if __name__ == "__main__":
    product = input("Enter desired product name: ")
    results = get_search_results(product)
    if results:
        print(f'Found {len(results)} result(s) for "{product}"')
        for res in results:
            print(f'{res["name"]}: {res["price"]}')
    else:
        print(f'No product "{product}" found')