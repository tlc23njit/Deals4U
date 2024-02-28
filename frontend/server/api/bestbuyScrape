import requests
from bs4 import BeautifulSoup
def bbScrape():
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    headers = {'User-Agent': user_agent}
    URL = "https://www.bestbuy.com/site/outlet-refurbished-clearance/clearance-electronics/pcmcat748300666044.c?id=pcmcat748300666044"
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.text, "html.parser")
    results = soup.find(id="main-results")
    job_elements = results.find_all("li", class_="sku-item")

    bbProducts = []

    for job_element in job_elements:
        name_element = job_element.find("h4", class_="sku-title")
        sale_element = job_element.find("div", class_="priceView-hero-price priceView-customer-price")
        link_url = job_element.find_all("a")[0]["href"]
        img_element = job_element.find_all("img")[0]["srcset"]
        price_element = job_element.find("div", class_="pricing-price__regular-price sr-only")
        if name_element and price_element and link_url and img_element and sale_element:
            products = {}
            name_element = name_element.text.strip()
            #print(name_element)
            products['title'] = name_element
            #print("")
            sale_element = sale_element.text.strip().split('$')[2].replace(',','')
            sale_element = float(sale_element)
            #print(sale_element)
            products['sale_price'] = sale_element
            #print("")
            price_element = float(price_element.text.strip().split('$')[1].replace(',',''))
            #print(price_element)
            products['regular_price'] = price_element
            #print("")
            link_url = "https://www.bestbuy.com" + link_url
            #print(link_url)
            products['href'] = link_url
            #print ("")
            img_element = img_element.split(';')[0]
            #print(img_element)
            products['image_url'] = img_element
            #print("")
            bbProducts.append(products)
    return bbProducts
