import bs4 as bs
from urllib import request


def export_data(file,data):
    header = "URL,TITLE,LOCATION,DISTANCE,BUYS,NORMAL PRICE,DISCOUNT PRICE\n"
    f = open(file,'w')
    f.write(header)
    for entry in data:
        try:
            f.write(entry)
        except:
            continue
    f.close()
    
urls = ['https://www.groupon.com/']
items = []

i = 0
while True:
    try:
        html = request.urlopen(urls[i]).read()
        soup = bs.BeautifulSoup(html,'html.parser')
        links = soup.find_all('a')
        urls_new = []
        for link in links:
            try:
                href = link['href']
                if href.find('https://www.groupon.com') != -1:
                    urls_new.append(href)
                elif href.find('http') == -1 and href[0:1] == '/':
                    urls_new.append(urls[i]+href[1:len(href)])
            except:
                None
        for url in urls_new:
            if url not in urls:
                urls.append(url)
        try:
            containers = soup.findAll('div',{'class':'cui-udc-details c-txt-gray-dk'})
            for container in containers:
                try:
                    title = container.div.text.replace(",",";")
                except:
                    title = ""
                try:
                    location = container.span.text.replace(",",";")
                except:
                    location = ""
                try:
                    location_distance = container.findAll('span',{'class':'cui-location-distance '})
                    location_distance = location_distance[0].text.replace(",",";")
                except:
                    location_distance = ""
                try:
                    buys = container.findAll('div',{'class':'cui-quantity-bought c-txt-gray-dk'})
                    buys = buys[0].text.replace(",",";")
                except:
                    buys = ""
                try:
                    original_price = container.s.text.replace(",",";")
                except:
                    original_price = ""
                try:
                    discount_price = container.findAll('span',{'class':'cui-price-discount c-txt-price '})
                    discount_price = discount_price[0].text.replace(",",";")
                except:
                    discount_price = ""
                data = urls[i] + "," + title.strip() + "," + location.strip()  + "," + location_distance.strip() + "," + buys.strip() + "," + original_price.strip() + "," + discount_price.strip() + "\n"
                if data not in items:
                    items.append(data)
        except:
            None
        i += 1
    except:
        break

export_data("data.csv",items)
    
