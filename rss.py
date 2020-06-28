import bs4 as bs
import feedgen
import requests

url="https://holod.media"
r = requests.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}, timeout=15)
a=r.content.decode("utf-8") 
soup = bs.BeautifulSoup(a,'lxml')

tab=[]

for row in soup.find_all('a',attrs={"class" : "t404__link"}):
    tab.append([str(row.get('href')),url+str(row.get('href'))])
        

from feedgen.feed import FeedGenerator
fg = FeedGenerator()
fg.title('HOLOD')
fg.link( href='http://192.168.1.25', rel='alternate' )
fg.id('http://192.168.1.25')
fg.subtitle('HOLOD')

for entry in tab:
    fe = fg.add_entry()
    fe.id(str(entry[1]))
    fe.title(str(entry[0]))
    fe.link(href=str(entry[1]))

fg.rss_file('a.xml')
