import requests
from requests import exceptions
from bs4 import BeautifulSoup
from urllib.error import HTTPError

if __name__ == "__main__":
    #Store product name and search
    product_split = input("Enter desired product name: ").split(" ")
    URL = "https://www.walmart.com/search?q="
    for i in product_split:
        URL += i + "+"

    #Request page and store BeautifulSoup object with html parser
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    #Find all products
