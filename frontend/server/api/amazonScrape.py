import requests
from bs4 import BeautifulSoup

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

                amazonProducts.apppend(products)

    return amazonProducts

scrapeAmazon()
            
