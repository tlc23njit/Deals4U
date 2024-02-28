import requests
from bs4 import BeautifulSoup

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

for product in hmProducts:
    print(product['title'])
    print(product['image_url'])
    print(product['href'])
    print(product['sale_price'])
    print(product['regular_price'])

    print()
