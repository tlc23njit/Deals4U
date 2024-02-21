import os
from dotenv import load_dotenv
import mysql.connector
import sys


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


def updateDB(product_id_to_remove, new_product_data):
    mydb = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    cursor = mydb.cursor()

    try:
        # Remove the existing product
        remove_product_query = "DELETE FROM Products WHERE Product_ID = %s"
        cursor.execute(remove_product_query, (product_id_to_remove,))

        # Insert the new product
        insert_product_query = "INSERT INTO Products (Product_ID, Product_Name, WebsiteUrl, Image, Discount_Price, Full_Price, Category) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(insert_product_query, new_product_data)

        # Commit the changes
        mydb.commit()

        print("Database updated successfully.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        cursor.close()
        mydb.close()

# Assuming script is run like: python script.py 1 "New Product" "https://newproduct.com" "new_image.jpg" "19.99" "29.99" "Electronics"
if len(sys.argv) != 8:
    print("Usage: python script.py <Product_ID to remove> <Product_Name> <WebsiteUrl> <Image> <Discount_Price> <Full_Price> <Category>")
    sys.exit(1)

product_id_to_remove = int(sys.argv[1])
new_product_data = tuple(sys.argv[2:])

updateDB(product_id_to_remove, new_product_data)


