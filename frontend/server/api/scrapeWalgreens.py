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
print(soup)

# Find the <ul> element with class 'list__inline list__3-column content'
product_list = soup.find('ul', id_="at_ul_1253965")
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

# Print the extracted product information
#for product in walgreensProducts:
    print("Title:", product['title'])
    print("Image URL:", product['image_url'])
    print("Href:", product['href'])
    print("Sale Price:", product['sale_price'])
    print()
