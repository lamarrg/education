"""
Use requests and BeautifulSoup to pull headlines from a news site.
"""
import requests
from bs4 import BeautifulSoup

# url to call
url = "https://www.npr.org/sections/news/"

# returns contents of page
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

# finds headlines as laid out on this page
headlines = soup.find_all("h2", class_="title")

# prints first 5 headlines
for i in range(0, 5):
    print(headlines[i].text.strip())

# specifically found a simple website to demonstrate the concept. One time I built a scraper to check when Hamilton tickets went on sale. The page would not allow a Beautifulsoup scrape, so I used a terminal curl statement to pull the contents of the page and checked the html after it was saved to a file. 
