import requests
from requests import exceptions
from bs4 import BeautifulSoup

if __name__ == "__main__":
    #Store product name and search
    product_split = input("Enter desired product name: ").split(" ")
    URL = "https://www.walmart.com/search?q="
    for i in product_split:
        URL += i + "+"
    print(URL)
    #Request page and store BeautifulSoup object with html parser
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    #Find all products
    results = soup.find_all('span', class_="w_BJ")
    for res in results:
        print(res.text)