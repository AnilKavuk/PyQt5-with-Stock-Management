# ---------------------Library--------------------------------------#
# ------------------------------------------------------------------#
import sys
import sqlite3

sys.path.append("./views")

from PyQt5 import *
from PyQt5.QtWidgets import *
from main_page import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

# ---------------------Library--------------------------------------#
# ------------------------------------------------------------------#


# ---------------------Main Create----------------------------------#
# ------------------------------------------------------------------#

mainApp = QApplication(sys.argv)
MainWindow = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

MainWindow.setWindowIcon(QtGui.QIcon("./icon.ico"))
MainWindow.setWindowTitle("Stock Management")

connection = sqlite3.connect("./database/products.db")
cursor = connection.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS stock ( id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,productName TEXT NOT NULL, productType TEXT NOT NULL, quantity INTEGER NOT NULL,quantityPrice INTEGER,mountingType TEXT, description TEXT)"
)
connection.commit()

MainWindow.show()

# ---------------------Main Create----------------------------------#


def addProduct():
    productName = ui.ProductName
    productType = ui.ProductType
    quantity = ui.ProductQuantity
    quantityPrice = ui.ProductQuantityPrice
    mountingType = ui.ProductMountingType
    description = ui.ProductDescription

    if (
        len(productName.text()) > 0
        and len(productType.text()) > 0
        and len(quantity.text()) > 0
    ):
        cursor.execute(
            """INSERT INTO \
            stock(productName,productType,quantity,quantityPrice,mountingType,description)\
            VALUES (?,?,?,?,?,?)""",
            (
                productName.text(),
                productType.text(),
                quantity.text(),
                quantityPrice.text(),
                mountingType.currentText(),
                description.toPlainText(),
            ),
        )
        connection.commit()
        productListing()
    else:
        ui.statusbar.showMessage(
            "Product name, Product Type ya da Quantity boş bırakılamaz", 3000
        )


def productListing():
    query = f"SELECT COUNT(*) FROM stock"
    cursor.execute(query)
    result = cursor.fetchone()
    row_count = result[0]
    ui.ProductTable.clear()
    query = cursor.execute("SELECT * FROM stock")
    ui.ProductTable.setRowCount(row_count)
    productName = ui.ProductName
    productType = ui.ProductType
    quantity = ui.ProductQuantity
    quantityPrice = ui.ProductQuantityPrice
    mountingType = ui.ProductMountingType
    description = ui.ProductDescription
    ui.ProductTable.setHorizontalHeaderLabels(
        (
            "No",
            "Product Name",
            "Product Type",
            "Quantity",
            "Quantity Price",
            "Mounting Type",
            "Description",
        )
    )
    ui.ProductTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    for rowIndexes, rowValue in enumerate(query):
        for columnIndexes, columnValue in enumerate(rowValue):
            ui.ProductTable.setItem(
                rowIndexes, columnIndexes, QtWidgets.QTableWidgetItem(str(columnValue))
            )

    productName.clear(),
    productType.clear(),
    quantity.clear(),
    quantityPrice.clear(),
    mountingType.setCurrentIndex(0),
    description.clear()


productListing()
# ---------------------signal slot----------------------------------#
ui.ProductAdd.clicked.connect(addProduct)
# ---------------------signal slot----------------------------------#


sys.exit(mainApp.exec_())
