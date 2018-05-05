# tutorial on https://realpython.com/python-web-scraping-practical-introduction/

from bs4 import BeautifulSoup

from aux_func.simple_get import simple_get


page_address = "https://webapps.utwente.nl/reservationscalendar/"
page_content = simple_get(page_address)


# Possible parsers
# soup = BeautifulSoup(page.content, 'lxml')
# soup = BeautifulSoup(page.content, 'lxml-xml')
page_content = BeautifulSoup(page.content, 'html.parser')
# soup = BeautifulSoup(page.content, 'html5lib')

# print(soup.prettify())

# k_header = soup.find_all('div')
# subclass = soup.find_all(class_="k-state-default k-nav-current")
# print(soup.find_all('div', class_="k-reset k-scheduler-navigation"))
# print(soup.find_all('li', class_="k-state-default k-nav-current"))
# print(soup.find_all('body div'))
print(page_content.find(class_="k-lg-date-format"))

# print(soup.find_all('li')[0].get_text())
# print(len(k_header))
# print(k_header)
# print(subclass)
