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
        
        # Commit the changes
        mydb.commit()

        print("Database updated successfully.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        cursor.close()
        mydb.close()

<<<<<<< HEAD
# Assuming script is run like: python script.py 1 "New Product" "https://newproduct.com" "new_image.jpg" "19.99" "29.99" "Electronics"
if len(sys.argv) != 8:
    print("Usage: python script.py <Product_ID to remove> <Product_Name> <WebsiteUrl> <Image> <Discount_Price> <Full_Price> <Category>")
    sys.exit(1)

product_id_to_remove = int(sys.argv[1])
new_product_data = tuple(sys.argv[2:])

<<<<<<< HEAD
updateDB(product_id_to_remove, new_product_data)
=======
updateDB(product_id_to_remove, new_product_data)
=======
updateDB()



>>>>>>> 69e2e6c6584d05fe751c6cbaa53549d4dfbd3809


>>>>>>> a7a24d80758a4bae5f8482c8c056a3050de1c4ae
