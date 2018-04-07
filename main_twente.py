import requests
from bs4 import BeautifulSoup


page = requests.get("https://webapps.utwente.nl/reservationscalendar/")

if page.status_code == 200:
    print("Page status code: %s Download correct" % page.status_code)
else:
    print("Page status code: %s Error downloading" % page.status_code)

# print(page.content)

# soup = BeautifulSoup(page.content, 'ht    ml.parser')
soup = BeautifulSoup(page.content, 'html5lib')

# print(soup.prettify())

k_header = soup.find_all('div')
subclass = soup.find_all('div', class_="k-floatwrap k-header k-scheduler-toolbar")
# print(soup.find_all('div', class_="k-reset k-scheduler-navigation"))

# print(soup.find_all('li')[0].get_text())
print(len(k_header))
print(subclass)
