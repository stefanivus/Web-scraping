#The user inputs a youtube channel name, the program outputs the number of views the channels most popular video has
from urllib import request
import bs4 as bs

while(True):
    user = input("Youtube channel name: ")
    url = "https://www.youtube.com/user/"+ user +"/videos?sort=p&view=0&flow=grid"
    html = request.urlopen(url).read()
    soup = bs.BeautifulSoup(html,'lxml')
    for p in soup.find_all('ul','yt-lockup-meta-info'):
        views = p.text
        break
    i = 1
    s = "k"
    while s[len(s)-1] != " ":
        s = views[0:i]
        i += 1
    print(s)
