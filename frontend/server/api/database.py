import os
from dotenv import load_dotenv
import mysql.connector

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


