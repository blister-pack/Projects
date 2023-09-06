import sqlite3
from faker import Faker
import secrets
from random import randint
import string

connection = sqlite3.connect("products.db")
cursor = connection.cursor()
f = Faker()
Faker.seed(4)
# BP ------------------------------------------------------------------------


def create_user_table():
    query = (
        "CREATE TABLE IF NOT EXISTS users("
        "id INTEGER PRIMARY KEY AUTOINCREMENT,"
        "user_name VARCHAR(30),"
        "first_name VARCHAR(30),"
        "last_name VARCHAR(30),"
        "address VARCHAR(50),"
        "password VARCHAR(50))"
    )
    cursor.execute(query)


def generate_pw(length=(randint(8, 20))):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(characters) for _ in range(length))
    return password


def create_users(user_num):
    query = (
        "INSERT INTO users(user_name, first_name, last_name, address, password)"
        "VALUES(?, ?, ?, ?, ?)"
    )

    for _ in range(user_num):
        username = f.user_name()
        firstname = f.first_name()
        lastname = f.last_name()
        address = f.address()
        pw_random = generate_pw()

        cursor.execute(query, (username, firstname, lastname, address, pw_random))


# BP ------------------------------------------------------------------------
if __name__ == "__main__":
    create_user_table()
    create_users(5)

connection.commit()
connection.close()
