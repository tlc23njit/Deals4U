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
        for i in range(len(results)):
            d={}
            results[i]=results[i].prettify()
            k=results[i].split('"')
            d["website"]="Dell"
            d["href"]=''
            d["image_url"]=''
            d["title"]=''
            d['regular_price']=''
            d['sale_price']=''
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
                    d['image_url'] = k[j+2]
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
    return l
