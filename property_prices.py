from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://appbrewery.github.io/Zillow-Clone/")
web_site = response.text

soup = BeautifulSoup(web_site, "html.parser")

#Address of the Property.
Address = []
address = soup.find_all("address", {"data-test": "property-card-addr"})
for tag  in address:
    Address.append(tag.text.strip())
#Price of property.
prices = []
price = soup.find_all(class_="PropertyCardWrapper__StyledPriceLine")
for pricez in price:
    prices.append(pricez.text.strip())
#Link of the property.
img_src_property = []
link_of_property = soup.find_all('source')
for img_src_propertz in link_of_property:
    img_src_property.append(img_src_propertz)





