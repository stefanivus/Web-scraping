#For a youtube search query , prints out the titles of all related videos to each of the videos on the first result page of the search query
from urllib import request
import re
import bs4 as bs
def findall(sub, string):
    i = string.find(sub)
    while i != -1:
        yield i
        i = string.find(sub, i+1)
        
while(True):
    keyword = input("Enter search query: ")
    url = "https://www.youtube.com/results?search_query=" + keyword
    regex = "<li>(.+?)</li>"
    pattern = re.compile(regex)
    try:
        a = request.urlopen(url)
        html = a.read()
        data = re.findall(pattern,str(html))
        links = []
        for a in data:
            indexes = findall('href="/watch?v=',a)
            for i in indexes:
                links.append("https://www.youtube.com/watch?v="+a[i+15:i+26])
        comments = []
        for link in links:
            html = request.urlopen(link).read()
            soup = bs.BeautifulSoup(html,'lxml')
            for title in soup.find_all('span','title'):
                print(title.text)
    except:
        print("An unexpected error occured")

           

        
