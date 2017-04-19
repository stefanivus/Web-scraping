import bs4 as bs
from urllib import request as rq

url = "https://www.groupon.com/browse/chicago?category=beauty-and-spas"
fname = "data.csv"
data_types = "title, location, location_distance, buys, original_price, discount_price\n"
f = open(fname,"w")
f.write(data_types)
html = rq.urlopen(url).read()
soup = bs.BeautifulSoup(html,'html.parser')
containers = soup.findAll('div',{'class':'cui-udc-details c-txt-gray-dk'})
for container in containers:
    title = container.div.text
    location = container.span.text
    location_distance = container.findAll('span',{'class':'cui-location-distance '})
    location_distance = location_distance[0].text
    buys = container.findAll('div',{'class':'cui-quantity-bought c-txt-gray-dk'})
    buys = buys[0].text
    original_price = container.s.text
    discount_price = container.findAll('span',{'class':'cui-price-discount c-txt-price '})
    discount_price = discount_price[0].text
    data = title.strip() + "," + location.strip()  + "," + location_distance.strip() + "," + buys.strip() + "," + original_price.strip() + "," + discount_price.strip() + "\n"
    f.write(data)
f.close()

