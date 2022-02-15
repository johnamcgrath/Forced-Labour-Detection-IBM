# importing necessary libraries for the webscraping to work
import requests
from bs4 import BeautifulSoup


def main():
    # setting the url to the website for scraping, in this case the first page of the accounting jobs section
    # on locanto.ie
    url = 'https://www.locanto.ie/Accounting-Financing-Banking/644/'

    # setting a user agent for accessing the url, in the event the website
    # tries to block a browser without a user agent as this being done through
    # a python script
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"
    }

    # requesting the data from the url, passing the header that was made
    # r has the source code for this url
    r = requests.get(url, {'headers': headers})

    # use beautiful soup to skim through the source code
    soup = BeautifulSoup(r.text, 'html.parser')

    # sample query. looking for the title of the first job on the page
    print(soup.find_all('div', {'class': 'textHeader'})[0].find('a').text + "\n")

    # loop to print the job titles and initial descriptions of each job on the page
    # counted 24 job links on the first page but there might be more or less on
    # other pages
    i = 0
    while i < 24:
        print(soup.find_all('div', {'class': 'textHeader'})[i].find('a').text)
        print(soup.find_all('div', {'class': 'textDesc gray12'})[i].find('a').text)
        print()
        i += 1


if __name__ == "__main__":
    main()
