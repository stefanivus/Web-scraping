import bs4 as bs
from urllib import request

def get_urls(file):
    f = open(file,"r")
    urls = []
    for line in f.readlines():
        urls.append(line)
    return urls

file = "websites.txt"
urls = get_urls(file)
for url in urls:
    html = request.urlopen(url).read()
    soup = bs.BeautifulSoup(html,'lxml')
    sources = soup.findAll('meta',{"name":"description"})
    title = soup.find('title')
    for source in sources:
        print("Title: " + title.text)
        print("Description: " + source['content']+"\n")

a = input()




