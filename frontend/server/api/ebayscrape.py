import requests as r
from bs4 import BeautifulSoup as bs
#URL = "https://realpython.github.io/fake-jobs/"
def scrapeEbay():
    websites = ['https://www.ebay.com/deals']
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    headers = {'User-Agent': user_agent}
    j = 0
    d={}
    nb=False
    wb=True
    for a in websites:
        page = r.get(a, headers=headers)
        soup = bs(page.content, "html.parser")
        results = soup.find_all("div", class_ = "dne-itemtile dne-itemtile-medium")
        results += soup.find_all("div", class_ = "dne-itemtile dne-itemtile-large")
        #print(results[0].prettify().split())
        for i in range(len(results)):
            results[i]=results[i].prettify()
            d[i]={}
            n=""
            k=results[i].split()
            ub = True
            ib = True
            db = True
            d[i]["website"]="ebay"
            d[i]["href"]=None
            d[i]["img_url"]=None
            d[i]["title"]=None
            d[i]['regular_price']=None
            d[i]['sale_price']=None
            d[i]['category']=None
            for j in range(len(k)):
                if k[j][0:5] == "href=" and ub:
                    ub = False
                    d[i]["href"]=k[j][6:-1]
                if k[j][0:5] == "title":
                    nb = True
                if nb:
                    n+=k[j]+" "
                    if k[j][-2:]=='">' or k[j][-2:]=="'>":
                        nb = False
                        d[i]["title"]=n[7:-3]
                if k[j][0:3]=="src" and ib:
                    d[i]["img_url"]=(k[j][4:-3])
                    ib = False
                if k[j][0:15]=="data-config-src" and ib:
                    d[i]["img_url"]=k[j][17:-1]
                    ib = False
                if k[j]=='itemprop="price">':
                    d[i]["sale_price"]=(k[j+1])
                if k[j]=='Previous' and db:
                    d[i]["regular_price"]=k[j+2]
                    db=False
                if k[j]=='class=evo-strikethrough-price">' and db:
                    d[i]["regular_price"]=k[j+1]
                    db=False

    l=[]
    for x in range(len(d)):
        l.append(d[x])
    return l
l=scrapeEbay()
print(len(l))
print(l[104])