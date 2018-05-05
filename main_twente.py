# tutorial on
# https://realpython.com/python-web-scraping-practical-introduction/

from bs4 import BeautifulSoup
from aux_func.simple_get import simple_get
import dryscrape

page_address = "https://webapps.utwente.nl/reservationscalendar/"

session = dryscrape.Session()
session.visit(page_address)
response = session.body()
soup = BeautifulSoup(response, 'html.parser')
spans = soup.find('span')
print(spans)


"""raw_page_content = simple_get(page_address)

parser = 'html.parser'
parser = 'lxml'
html_content = BeautifulSoup(raw_page_content, parser)

divs = html_content.find_all('span')
print(divs)"""
