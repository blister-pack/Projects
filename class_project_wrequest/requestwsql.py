import sqlite3
from request import fetch_product_data
from datetime import datetime
import random

connection = sqlite3.connect("products.db")
cursor = connection.cursor()


# BP--------------------------------------------------------------------------
def create_table():
    query = (
        "CREATE TABLE IF NOT EXISTS products("
        "title VARCHAR(30) PRIMARY KEY,"
        "category VARCHAR(30),"
        "price REAL,"
        "description TEXT,"
        "date DATE)"
    )
    cursor.execute(query)


def drop_table():
    query = "DROP TABLE products"
    cursor.execute(query)


def fake_date():
    randyear = random.randint(1990, 2023)
    randmonth = random.randint(1, 12)
    if randmonth in [1, 3, 5.7, 8, 10, 12]:
        randday = random.randint(1, 31)
    elif randmonth == 2:
        randday = random.randint(1, 28)
    else:
        randday = random.randint(1, 30)

    ledate = datetime(year=randyear, month=randmonth, day=randday)
    return ledate.strftime("%Y-%m-%d")


def insert_products(num_of_products):
    for num in range(1, num_of_products + 1):
        rand_date = fake_date()
        item = fetch_product_data(num)
        title = item[0]
        category = item[1]
        price = item[2]
        description = item[3]

        query = (
            f"INSERT INTO products(title, category, price, description, date)"
            f"VALUES(?, ?, ?, ?, ?)"
        )

        cursor.execute(query, (title, category, price, description, rand_date))
        # when it's done like this it prevents sql injection



# BP--------------------------------------------------------------------------
if __name__ == "__main__":
    create_table()
    # drop_table()
    insert_products(10)

connection.commit()
connection.close()
