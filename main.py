# Tutorial in https://www.dataquest.io/blog/web-scraping-tutorial-python/


import requests
from bs4 import BeautifulSoup


page = requests.get("http://dataquestio.github.io/web-scraping-pages/" +
                    "ids_and_classes.html")

if page.status_code == 200:
    print("Page status code: %s Download correct" % page.status_code)
else:
    print("Page status code: %s Error downloading" % page.status_code)

# print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())


# Finding all instances of a tag at once
print("Find all 'p'")
print(soup.find_all('p', class_="outer-text"))

soup.find_all('p')[0].get_text()
