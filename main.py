# Tutorial in https://www.dataquest.io/blog/web-scraping-tutorial-python/


import requests
from bs4 import BeautifulSoup


page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")

if page.status_code == 200:
    print("Page status code: %s Download correct" % page.status_code)
else:
    print("Page status code: %s Error downloading" % page.status_code)

# print(page.content)

soup = BeautifulSoup(page.conteng, 'html.parser')

# print(soup.prettify())

print('Elements types:')
print([type(item) for item in list(soup.childre)])

html = list(soup.children)[2]
body = list(html.children)[3]
p = list(body.children)[1]

print(p.get_text())
