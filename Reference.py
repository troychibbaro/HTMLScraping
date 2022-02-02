import requests
from requests import exceptions
from bs4 import BeautifulSoup
from urllib.error import HTTPError

if __name__ == "__main__":
    try:
        #requests and stores page content
        url = "https://realpython.github.io/fake-jobs/"
        page = requests.get(url)

        #Holds BS object, parses the html text stored from page request
        soup = BeautifulSoup(page.content, "html.parser")

        #returns result set of search
        results = soup.find(id="ResultsContainer")

        #Find all jobs
        job_elements = results.find_all("div", class_="card-content")

        #Get job titles
        titles = []
        for job in job_elements:
            titles.append(job.find("h2", class_="title").text)
        print(titles)

        #Find all python related jobs by giving a lambda to as an argument
        #Returns result set containing PageElements fitting criteria
        pyjobs = results.find_all("h2", string=lambda text: "python" in text.lower())
        print("Pyjobs:")
        for job in pyjobs:
            print(job.text)
    except (HTTPError, exceptions.RequestException, ValueError):
        if HTTPError:
            print("Issue retrieving page, try another URL")
        elif exceptions.RequestException:
            print(f'Invalid URL: {URL}')