import requests
from bs4 import BeautifulSoup

r = requests.get(
    'https://www.century21uk.com/property-search/?location=London&lat=51.5073509&lng=-0.1277583&type=&min=0&rooms=0&radius=5.1&added=any&max=0&maxrooms=0&agentID=&ownership=resale')

base_website = 'https://www.century21uk.com'

c = r.content

soup = BeautifulSoup(c, 'html.parser')

properties = soup.find_all("div", {'class': 'property-tile'})

first = properties[0].find("b").text

for prop in properties:
    print(prop.find('h4', {'class': 'title'}).text.lstrip())
    print(prop.find('b').text)
    print(prop.find_all('li')[0].text.lstrip() + " Bedrooms")
    print(prop.find_all('li')[1].text.lstrip() + " Bathrooms")
    print(prop.find_all('li')[2].text.lstrip() + " Receptions")
    print(base_website + prop.find('a').get('href'))
