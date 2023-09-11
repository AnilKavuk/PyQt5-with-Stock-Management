import sqlite3


def createDb():
    print("db olusturuldu")
    connection = sqlite3.connect("products.db")

    cursor = connection.cursor()

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS stock (productName TEXT, productType TEXT, quantity INTEGER,quantityPrice INTEGER,mountingType TEXT, description TEXT)"
    )
