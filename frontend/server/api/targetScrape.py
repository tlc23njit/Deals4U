import requests
from bs4 import BeautifulSoup

custom_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
    'Accept-Language': 'da, en-gb, en',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Referer': 'https://www.google.com/'
}

URL = "https://www.target.com/c/clearance/-/N-5q0ga?moveTo=product-list-grid"
baseUrl = "https://www.target.com"
page = requests.get(URL, headers= custom_headers)
soup = BeautifulSoup(page.text, "html.parser")

item_element_list = soup.find_all("div", class_="styles__StyledCardWrapper-sc-z8946b-0 kYOLFQ h-padding-a-tight")
#print(item_element_list)

for item_element in item_element_list:
    list_span = item_element.find("div", class_="h-text-red h-text-md", string="Clearance")

    if list_span:
        itemSoup = BeautifulSoup(str(item_element), "html.parser")
        
        price_span = itemSoup.find('span', class_='h-text-red')
        price_text = price_span.span.text

        print("Extracted Price:", price_text)
        print("\n")
