import sqlite3
from unittest import result

connection = sqlite3.connect("products.db")
cursor = connection.cursor()


# BP----------------------------------------------------------------------------------
def display_items():
    query = "SELECT * FROM products"
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)


def cli():
    quitter = False
    while quitter == False:
        answer = input("Would you like to see the stock or exit? ")
        if answer == "stock":
            display_items()
        else:
            quitter = True
            print("Goodbye!")


# BP----------------------------------------------------------------------------------
if __name__ == "__main__":
    cli()

connection.commit()
connection.close()
