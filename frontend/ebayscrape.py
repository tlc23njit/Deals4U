import requests as r
from bs4 import BeautifulSoup as bs
#URL = "https://realpython.github.io/fake-jobs/"
websites = ['https://www.ebay.com/deals']
j = 0
d={}
nb=False
for i in websites:
    page = r.get(i)
    #print(page.text)
    soup = bs(page.content, "html.parser")
    #results = soup.find_all(itemprop="price")
    results = soup.find_all("div", class_ = "dne-itemtile dne-itemtile-medium")
    results += soup.find_all("div", class_ = "dne-itemtile dne-itemtile-large")
    print(len(soup.find_all("div", class_ ="dne-itemtile-detail")))
    for i in range(len(results)):
        results[i]=results[i].prettify()
        d[i]=[]
        n=""
        for j in results[i].split():
            if j[0:5] == "href=":
                d[i].append(j[6:-1])
            if j[0:5] == "title":
                nb = True
            if nb:
                if j[-2:]=='">':
                    nb = False
                    d[i].append(n[7:-1])
                n+=j+" "
#for i in d:
    #print(d[i])
#print(results[0].split())
#print(d[0])
print(len(d))
print(len(results))
print(d[0])