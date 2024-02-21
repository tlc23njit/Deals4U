import requests as r
from bs4 import BeautifulSoup as bs
websites = ['https://www.kohls.com/catalog.jsp?CN=Assortment:Must%20Have%20Price%20and%20on%20Sale&BL=y&cc=salemusthave-TN1.0-S-SaleMusthave']
j = 0
d={}
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
headers = {'User-Agent': user_agent}
k=[]
for i in websites:
    page = r.get(i, headers=headers)
    soup = bs(page.content, "html.parser")
    results=soup.find_all("li", class_="products_grid coupon_eligible")
    for i in range(len(results)):
        results[i]=results[i].prettify()
        d[i]={}
        n=""
        k=results[i].split()
        nb=False
        nb2 = True
        ub=True
        ib=True
        pb=True
        db=True
        d[i]["website"]="Kohls"
        d[i]["url"]=''
        d[i]["img"]=''
        d[i]["title"]=''
        d[i]['price']=''
        d[i]['discount']=''
        for j in range(len(k)):
            if k[j][0:5] == "href=" and ub:
                ub = False
                d[i]["url"]="kohls.com"+k[j][6:-1]
            if k[j][0:5] == "title" and nb2:
                nb2 = False
                nb = True
            if nb:
                n+=k[j]+" "
                if '>' in k[j]:
                    nb = False
                    d[i]["title"] = n[7:-18]
            if k[j][0:7]=="srcset=" and ib:
                d[i]["img"] = k[j][8:]
                ib=False
            if k[j] == 'red_color">' and pb:
                pb=False
                d[i]["price"] = k[j+1]
            if k[j] == 'class="prod_price_amount">' and db:
                pb=False
                d[i]["price"] = k[j+1]
            if k[j] == 'class="prod_price_original">' and db:
                db=False
                if k[j+1] == '</div>':
                    d[i]["discount"] = "N/A"
                else:
                    d[i]["discount"] = k[j+1]
                
#print(k)
#print(results)
#print("test")
#print(soup.prettify())

for i in d:
    #if d[i]["price"] =='':
    #print(i,": ", results[i].split())
    print(i,": ", d[i])

#print(len(d))
#print(results[6].split())
#print(d[44])
#print(results[7].split())
#print(k)
#print(d[2])