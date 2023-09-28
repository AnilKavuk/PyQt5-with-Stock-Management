import sqlite3

connection = sqlite3.connect("./database/products.db")
cursor = connection.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS stock (productName TEXT, productType TEXT, quantity INTEGER,quantityPrice INTEGER,mountingType TEXT, description TEXT)"
)


def AddProduct():
    pass
