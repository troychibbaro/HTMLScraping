import requests
from requests import exceptions
from bs4 import BeautifulSoup
from urllib.error import HTTPError


if __name__ == "__main__":
    URL = input("Enter desired Wiki page: ")
    try:
        #Store page contents
        page = requests.get(URL)

        #create parser and find all 'cite' class HTML elements as well as article title
        soup = BeautifulSoup(page.content, "html.parser")
        citations = soup.find_all("cite")
        page_title = soup.find(id="firstHeading")

        #Create file only if citations were found
        if len(citations) > 0:
            f = open(f'{page_title.text} Citations.txt', "w")

            #Write citations to file
            for cite in citations:
                f.write(cite.text + "\n")
            f.close()
        else:
            print(f'No citations found in article "{page_title.text}"')

    #Catch runtime exceptions
    except (HTTPError, exceptions.RequestException, ValueError, IOError):
        if HTTPError:
            print(f'Issue retrieving page [{URL}], try another URL')
        elif exceptions.RequestException:
            print(f'Invalid URL: {URL}')
        elif IOError:
            print(IOError)
