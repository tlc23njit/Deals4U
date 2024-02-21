import requests as r
from bs4 import BeautifulSoup as bs
#URL = "https://realpython.github.io/fake-jobs/"
websites = ['https://www.ebay.com/deals']
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
headers = {'User-Agent': user_agent}
j = 0
d={}
nb=False
wb=True
for i in websites:
    page = r.get(i, headers=headers)
    soup = bs(page.content, "html.parser")
    results = soup.find_all("div", class_ = "dne-itemtile dne-itemtile-medium")
    results += soup.find_all("div", class_ = "dne-itemtile dne-itemtile-large")
    for i in range(len(results)):
        results[i]=results[i].prettify()
        d[i]={}
        n=""
        k=results[i].split()
        ub = True
        ib = True
        for j in range(len(k)):
            if wb:
                d[i]["website"]="ebay"
                wb=False
            if k[j][0:5] == "href=" and ub:
                ub = False
                d[i]["url"]=k[j][6:-1]
            if k[j][0:5] == "title":
                nb = True
            if nb:
                n+=k[j]+" "
                if k[j][-2:]=='">' or k[j][-2:]=="'>":
                    nb = False
                    d[i]["name"]=n[7:-3]
            if k[j][0:15]=="data-config-src" and ib:
                d[i]["img"]=k[j][17:-1]
                ib = False
            if k[j][0:3]=="src" and ib:
                d[i]["img"]=(k[j][4:-3])
                ib = False
            if k[j]=='itemprop="price">':
                d[i]["price"]=(k[j+1])
            if k[j]=="off":
                d[i]["discount"]=k[j-1]
#for i in d:
    #print(d[i])
#print(results[0].split())
#print(d[0])
#print(len(d))
#print(len(results))
print(d[0])
#print(d[1])
print(results[0].split())
#print(d[len(d)-1])