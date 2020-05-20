from urllib.parse import urlunsplit, urlunparse
import webbrowser


def build_link(scheme, agent, path, location, fragment):
    url = urlunsplit((scheme, supplier, path, location_input, fragment))
    return url


x = ('https://', 'www.century21uk.com', '/property-search/',
     'location=London&lat=51.5073509&lng=-0.1277583&type=&min=0&rooms=0&radius=5.1&added=any&max=0&maxrooms=0&agentID=&ownership=resale', '')

scheme = 'https://'

supplier = 'www.century21uk.com'

path = '/property-search/'

location_input = 'location=London&lat=51.5073509&lng=-0.1277583&type=&min=0&rooms=0&radius=5.1&added=any&max=0&maxrooms=0&agentID=&ownership=resale'

fragment = ''

url = urlunsplit((scheme, supplier, path, location_input, fragment))

print(build_link(*x))
