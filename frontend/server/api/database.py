import requests 
import os
from dotenv import load_dotenv
import mysql.connector
from bs4 import BeautifulSoup


def scrapeHM():
    url = "http://www2.hm.com/en_us/sale/men/view-all.html"
    base_url = "http://www2.hm.com"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15",
    }
    hmProducts = []
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the <ul> element with class 'products-listing small'
    product_list = soup.find('ul', class_='products-listing small')

    # Find all <li> elements with class 'product-item' within the product_list
    product_items = product_list.find_all('li', class_='product-item')


    # Iterate over each product item and extract the desired information
    for product_item in product_items:
        products = {}
        title = product_item.find('a', class_='link').text.strip()
        image_tag = product_item.find('img')
        # Extract the image URL from the 'data-src' attribute
        image_url = "https:" + image_tag.get('data-src', 'Image URL not found')
        href = base_url + product_item.find('a', class_='link')['href']
        try:
            sale_price = product_item.find('span', class_='price sale').text.strip()
        except AttributeError:
            sale_price = ''
        regular_price = product_item.find('span', class_='price regular').text.strip()

        products['title'] = title
        products['image_url'] = image_url
        products['href'] = href
        products['sale_price'] = sale_price
        products['regular_price'] = regular_price

        hmProducts.append(products)
    
    return hmProducts 
def scrapeWalgreens(): 
    import requests
    from bs4 import BeautifulSoup

    # URL of the Walgreens online deals page
    url = "https://www.walgreens.com/topic/promotion/walgreens-online-deals.jsp?ban=dl_dlsp_MegaMenu_DMI_TopDeals"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15",
    }

    # Send a GET request to the URL
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the <ul> element with class 'list__inline list__3-column content'
    product_list = soup.find('ul', class_="list__inline list__3-column content")

    # Initialize an empty list to store the product dictionaries
    walgreensProducts = []

    # Check if product_list is found
    if product_list:
        # Find all <li> elements within the product_list
        product_items = product_list.find_all('li')

        # Iterate over each product item and extract the desired information
        for product_item in product_items:
            try:
                product = {}
                title_div = product_item.find('div', class_='font__sixteen')
                if title_div:
                    title = title_div.text.strip()

                    # Remove "select" from the beginning of the title if it exists
                    if title.startswith('select '):
                        title = title[len('select '):]

                    # Remove asterisk (*) from the end of the title
                    title = title.rstrip('*')

                    image_tag = product_item.find('img')
                    image_url = image_tag['src'] if image_tag else 'Image URL not found'
                    href_tag = product_item.find('a', class_='card__topic')
                    href = href_tag['href'] if href_tag else 'URL not found'
                    sale_price_tag = product_item.find('strong')
                    sale_price = sale_price_tag.text.strip() if sale_price_tag else 'Price not found'

                    # Store the extracted information in the product dictionary
                    product['title'] = title
                    product['image_url'] = image_url
                    product['href'] = href
                    product['sale_price'] = sale_price

                    # Add the product dictionary to the list
                    walgreensProducts.append(product)
            except Exception as e:
                print(f"An error occurred: {e}")
    else:
        print("Product list not found.")

    return walgreensProducts
def scrapeAmazon():
    custom_headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
        'Accept-Language': 'da, en-gb, en',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Referer': 'https://www.google.com/'
    }

    amazonProducts = []

    URL = "https://www.amazon.com/s?k=deals&crid=3TY4WIKT6FJYD&sprefix=deals%2Caps%2C78&ref=nb_sb_noss_1"
    baseUrl = "https://www.amazon.com"
    page = requests.get(URL, headers= custom_headers)
    soup = BeautifulSoup(page.text, "html.parser")

    item_element_list = soup.find_all("div", class_="sg-col-inner")

    for item_element in item_element_list:
        list_span = item_element.find("span", class_="a-size-base a-color-secondary", string="List: ")
        typical_span = item_element.find("span", class_="a-size-base a-color-secondary", string="Typical: ")

        if list_span or typical_span:
            price_element = item_element.find_previous("a", class_="a-link-normal s-no-hover s-underline-text s-underline-link-text s-link-style a-text-normal")
            name_element = item_element.find_previous("span", class_="a-size-base-plus a-color-base a-text-normal")
            img_element = item_element.find_previous("div", class_="a-section aok-relative s-image-tall-aspect")
            href_element = item_element.find_previous("a", class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")
            sale_element = item_element.find_previous("span", class_="a-price a-text-price")

            if price_element and name_element:
                priceSoup = BeautifulSoup(str(price_element), 'html.parser')
                priceStrip = priceSoup.select_one("a.a-link-normal span.a-price")
                holdPrice = priceStrip.text.strip()
                holdSale = sale_element.text.strip()
                imgSoup = BeautifulSoup(str(img_element), 'html.parser')
                holdImg = imgSoup.find('img')['src']
                hrefSoup = BeautifulSoup(str(href_element), 'html.parser')
                holdHref = hrefSoup.find('a')

                products = {}


                if (float(holdPrice[1:int(len(holdPrice)/2)]) > float(holdSale[1:int(len(holdSale)/2)])):
                    continue

                '''
                print("Price:", holdPrice[1:int(len(holdPrice)/2)])
                print("Name:", name_element.text.strip())
                print("href: ", baseUrl + holdHref.get('href'))
                print("Img:", holdImg)
                print("Sale: ", holdSale[1:int(len(holdSale)/2)])

                print("\n")
                '''
                products['title'] = name_element.text.strip()
                products['image_url'] = holdImg
                products['href'] = baseUrl + holdHref.get('href')
                products['sale_price'] = holdPrice[1:int(len(holdPrice)/2)]
                products['regular_price'] = holdSale[1:int(len(holdSale)/2)]

                amazonProducts.append(products)

    return amazonProducts
def scrapeEbay():
    websites = ['https://www.ebay.com/deals']
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    headers = {'User-Agent': user_agent}
    j = 0
    d={}
    nb=False
    wb=True
    for a in websites:
        page = requests.get(a, headers=headers)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find_all("div", class_ = "dne-itemtile dne-itemtile-medium")
        results += soup.find_all("div", class_ = "dne-itemtile dne-itemtile-large")
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
                if k[j][0:15]=="data-config-src" and ib:
                    d[i]["img_url"]=k[j][17:-1]
                    ib = False
                if k[j][0:3]=="src" and ib:
                    d[i]["image_url"]=(k[j][4:-3])
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
def scrapeDell():
    websites = ['https://www.dell.com/en-us/shop/deals']
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    headers = {'User-Agent': user_agent}
    l = []
    for a in websites:
        page = requests.get(a, headers=headers)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find_all("article")
        for i in range(len(results)):
            d={}
            results[i]=results[i].prettify()
            k=results[i].split('"')
            d[i]["website"]="Dell"
            d[i]["href"]=None
            d[i]["img_url"]=None
            d[i]["title"]=None
            d[i]['regular_price']=None
            d[i]['sale_price']=None
            d[i]['category']='Technology'
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
    for i in range(len(l)-1,0,-1):
        if l[i]['title']==None:
            del l[i]
        else:
            break
    return l

load_dotenv()

host = os.environ.get("DB_HOST")
user = os.environ.get("DB_USER")
password = os.environ.get("DB_PASSWORD")
database = os.environ.get("DB_DATABASE")


mydb = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)
cursor = mydb.cursor()


def updateDB():
    mydb = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    cursor = mydb.cursor()

    try:
        # Remove the existing product
        remove_product_query = "DELETE FROM Products "
        cursor.execute(remove_product_query)
        count = 0

        # Insert the new product
        insert_product_query = "INSERT INTO Products (Product_ID, Product_Name, WebsiteUrl, Image, Discount_Price, Full_Price, Category) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        hmList = scrapeHM()
        for product in hmList:
            count += 1
            cursor.execute(insert_product_query, (count, product['title'], product['href'], product['image_url'], product['sale_price'], product['regular_price'], "Clothing"))
        
        walgreensList = scrapeWalgreens()
        for product in walgreensList:
            count += 1
            cursor.execute(insert_product_query, (count, product['title'], product['href'], product['image_url'], product['sale_price'], None, "Convinience"))
        
        amazonList = scrapeAmazon()
        for product in amazonList:
            count += 1
            cursor.execute(insert_product_query, (count, product['title'], product['href'], product['image_url'], product['sale_price'], product['regular_price'], "Sorted"))

        ebayList = scrapeEbay()
        for product in ebayList:
            count += 1
            cursor.execute(insert_product_query, (count, product['title'], product['href'], product['image_url'], product['sale_price'], None, "Sorted"))

        dellList = scrapeDell()
        for product in dellList:
            count += 1
            cursor.execute(insert_product_query, (count, product['title'], product['href'], product['image_url'], product['sale_price'], product['regular_price'],product['category']))

        # Commit the changes
        mydb.commit()

        print("Database updated successfully.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        cursor.close()
        mydb.close()

updateDB()