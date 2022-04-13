# MLDataCollection
This repository contains some sample Python scripts used to 
extract data from websites and API's. The following are brief descriptions of 
each project, and I will try to add new ones periodically.

**Note**: These scripts were created **strictly** for educational purposes and may 
stop functioning if these websites change their HTML code. If that happens
I'll try to update them accordingly.

---
### Wikipedia Citation Scraper
    Input: URL of desired Wikipedia article

    Output: A file named "(article name) Citations.txt" that contains
    that pages citations. If no citations were found, the file does not 
    get created. Any errors are printed to console. 

---
### Apple Online Store Product Search
    Input: Product name that you would like to search.

    Output: Prints all search results to console as follows:
    "Product Name" - "Product Price"
    Due to page length limitations, this script will only show
    the first 30 items in the search if results > 30 (items on the first page).
    
    Example:
    >>> Enter desired product name: magsafe duo charger
    >>> Found 1 result(s) for "magsafe duo charger"
    >>> Magsafe Duo Charger: $129
---
### Heart Disease Key Indicators Analysis Tutorial
    A simple Jupyter Notebook that helps to understand Pandas
    and straight-forward analysis of a dataset shared to Kaggle.
