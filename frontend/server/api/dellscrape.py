import requests as r
from bs4 import BeautifulSoup as bs
#URL = "https://realpython.github.io/fake-jobs/"
def scrapeDell():
    websites = ['https://www.dell.com/en-us/shop/deals']
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    headers = {'User-Agent': user_agent}
    l = []
    for a in websites:
        page = r.get(a, headers=headers)
        soup = bs(page.content, "html.parser")
        results = soup.find_all("article")
        #print(results[26].prettify().split())
        for i in range(len(results)):
            d={}
            results[i]=results[i].prettify()
            k=results[i].split('"')
            d["website"]="Dell"
            d["href"]=None
            d["img_url"]=None
            d["title"]=None
            d['regular_price']=None
            d['sale_price']=None
            d['category']='Technology'
            tb = True
            ib = True
            pb = True
            ub = True
            ub1 = True
            db = True
            for j in range(len(k)):
                if k[j] == "title" and tb:
                    tb = False
                    d['title'] = k[j+2]
                if k[j] == 'image' and ib:
                    ib = False
                    d['img_url'] = k[j+2]
                if k[j] == 'dellPrice' and pb:
                    pb = False
                    d['sale_price'] = k[j+2]
                if k[j] == 'marketPrice' and db:
                    db = False
                    d["regular_price"] = k[j+2]
                if k[j] == "}' href=" and ub:
                    ub = False
                    d['href'] = "https:"+k[j+1]
            l.append(d)
    print(len(l))
    for i in range(len(l)-1,0,-1):
        if l[i]['title']==None:
            del l[i]
        else:
            break
    print(len(l))
    return l
l=scrapeDell()
#print(len(l))
print(l)