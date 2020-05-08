import requests
from bs4 import BeautifulSoup
import pandas


base_website = 'https://www.century21uk.com'
page_url = 'https://www.century21uk.com/property-search/?location=London&lat=51.5073509&lng=-0.1277583&type&min=0&rooms=0&radius=5.1&added=any&max=0&maxrooms=0&agentID&ownership=resale&cpage='

r = requests.get(page_url)
c = r.content
soup = BeautifulSoup(c, 'html.parser')
page_number = int(soup.find_all("a", {'class': 'page-numbers'})[-1].text)


props = []
for page in range(1, page_number+1):
    r = requests.get(page_url+str(page))
    c = r.content
    soup = BeautifulSoup(c, 'html.parser')
    properties = soup.find_all("div", {'class': 'property-tile'})

    for prop in properties:
        d = {}
        d['Address'] = prop.find('h4', {'class': 'title'}).text.lstrip()
        d['Price'] = prop.find('b').text
        d['Beds'] = prop.find_all('li')[0].text.lstrip()
        d['Baths'] = prop.find_all('li')[1].text.lstrip()
        d['Receptions'] = prop.find_all('li')[2].text.lstrip()
        d['URL'] = base_website + prop.find('a').get('href')
        props.append(d)

data = pandas.DataFrame(props)
data.to_csv('properties.csv', index=False)
