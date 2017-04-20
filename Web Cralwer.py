import bs4 as bs
from urllib import request

def get_urls(file):
    f = open(file,"r")
    urls = []
    for line in f.readlines():
        urls.append(line)
    return urls

def enter_urls(file,urls):
    f = open(file,'w')
    for url in urls:
        f.write(url+'\n')
    f.close()

def make_unique(arr):
    arr2 = []
    for i in arr:
        if i not in arr2:
            arr2.append(i)
    return arr2
    
fname = 'urls.csv'
urls = get_urls(fname)

i = 0
while True:
    try:
        html = request.urlopen(urls[i]).read()
        soup = bs.BeautifulSoup(html,'html.parser')
        links = soup.find_all('a')
        urls_new = []
        for link in links:
            href = link['href']
            if href.find('http') == -1:
                urls_new.append(urls[i].replace('\n','')+href[1:len(href)])
        for url in urls_new:
            urls.append(url)
        i += 1
    except:
        break
urls = make_unique(urls)

enter_urls('result.csv',urls)
