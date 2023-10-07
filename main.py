import sys
import sqlite3
import os
from xlsxwriter.workbook import Workbook
import pandas as pd

sys.path.append("./views")

from PyQt5 import *
from PyQt5.QtWidgets import *
from main_page import *
from PyQt5.QtCore import *

mainApp = QApplication(sys.argv)
MainWindow = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

if os.listdir()[0] != "data":
    os.mkdir("data")

MainWindow.setWindowIcon(QtGui.QIcon("./icon.ico"))
MainWindow.setWindowTitle("Stock Management")

connection = sqlite3.connect("data/products.db")
cursor = connection.cursor()
cursor.execute(
    """CREATE TABLE IF NOT EXISTS stock (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,productName TEXT NOT NULL, productType TEXT NOT NULL, quantity INTEGER NOT NULL,quantityPrice INTEGER,mountingType TEXT, description TEXT)"""
)
connection.commit()

MainWindow.show()


def addProduct():
    question = QMessageBox.question(
        MainWindow,
        "Update Record",
        "Are you sure you want to add the product?",
        QMessageBox.Yes | QMessageBox.No,
    )
    try:
        if question == QMessageBox.Yes:
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
                    stock(productName,productType,quantity,
                    quantityPrice,mountingType,description)\
                    VALUES (?,?,?,?,?,?)""",
                    (
                        productName.text().capitalize(),
                        productType.text().capitalize(),
                        quantity.text().capitalize(),
                        quantityPrice.text().capitalize(),
                        mountingType.currentText(),
                        description.toPlainText(),
                    ),
                )
                connection.commit()
                ui.statusbar.showMessage("Saved successfully", 3000)
                productListing()
            else:
                ui.statusbar.showMessage(
                    "Product name, Product Type or Quantity cannot be left blank", 3000
                )
        else:
            ui.statusbar.showMessage("Product addition canceled", 3000)
    except Exception as error:
        ui.statusbar.showMessage("This error was encountered: " + str(error), 3000)


def productListing():
    try:
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
                    rowIndexes,
                    columnIndexes,
                    QtWidgets.QTableWidgetItem(str(columnValue)),
                )

        productName.clear(),
        productType.clear(),
        quantity.clear(),
        quantityPrice.clear(),
        mountingType.setCurrentIndex(-1),
        description.clear()

    except Exception as error:
        ui.statusbar.showMessage("This error was encountered: " + str(error), 3000)


productListing()


def bringRecords():
    try:
        selectedProduct = ui.ProductTable.selectedItems()

        ui.ProductName.setText(selectedProduct[1].text())
        ui.ProductType.setText(selectedProduct[2].text())
        ui.ProductQuantity.setText(selectedProduct[3].text())
        ui.ProductQuantityPrice.setText(selectedProduct[4].text())
        ui.ProductMountingType.setCurrentText(selectedProduct[5].text())
        ui.ProductDescription.setPlainText((selectedProduct[6].text()))

    except Exception as error:
        ui.statusbar.showMessage("This error was encountered: " + str(error), 3000)


def productUpdate():
    question = QMessageBox.question(
        MainWindow,
        "Update Record",
        "Are you sure you want to update the record?",
        QMessageBox.Yes | QMessageBox.No,
    )
    if question == QMessageBox.Yes:
        try:
            selectedProduct = ui.ProductTable.selectedItems()
            id = int(selectedProduct[0].text())

            cursor.execute(
                """UPDATE stock SET\
                productName=?,productType=?,quantity=?,
                quantityPrice=?,mountingType=?,description=? WHERE id=?""",
                (
                    ui.ProductName.text().capitalize(),
                    ui.ProductType.text().capitalize(),
                    ui.ProductQuantity.text().capitalize(),
                    ui.ProductQuantityPrice.text().capitalize(),
                    ui.ProductMountingType.currentText(),
                    ui.ProductDescription.toPlainText(),
                    id,
                ),
            )

            connection.commit()
            productListing()
            ui.statusbar.showMessage(
                "Registration update process was completed successfully...", 3000
            )

        except Exception as error:
            ui.statusbar.showMessage("This error was encountered: " + str(error), 3000)

    else:
        ui.statusbar.showMessage("Registration Update process canceled...", 3000)


def searhProduct():
    try:
        if len(ui.ProductName.text().capitalize()) > 0:
            searched = cursor.execute(
                """SELECT * FROM stock WHERE productName LIKE '%{}%'""".format(
                    ui.ProductName.text().capitalize(),
                )
            )
        elif len(ui.ProductType.text().capitalize()) > 0:
            searched = cursor.execute(
                """SELECT * FROM stock WHERE productType LIKE '%{}%'""".format(
                    ui.ProductType.text().capitalize(),
                )
            )
        elif len(ui.ProductQuantity.text()) > 0:
            searched = cursor.execute(
                """SELECT * FROM stock WHERE quantity LIKE '%{}%'""".format(
                    ui.ProductQuantity.text(),
                )
            )
        elif len(ui.ProductMountingType.currentText()) > 0:
            searched = cursor.execute(
                """SELECT * FROM stock WHERE mountingType LIKE '%{}%'""".format(
                    ui.ProductMountingType.currentText(),
                )
            )
        else:
            searched = cursor.execute("""SELECT * FROM stock""")
            ui.statusbar.showMessage(
                "The product you were looking for was not found...", 3000
            )

        ui.ProductTable.clear()
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
        ui.ProductName.clear(),
        ui.ProductType.clear(),
        ui.ProductQuantity.clear(),
        ui.ProductQuantityPrice.clear(),
        ui.ProductMountingType.setCurrentIndex(-1),
        ui.ProductDescription.clear(),

        ui.ProductTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        for rowIndexes, rowValue in enumerate(searched):
            for columnIndexes, columnValue in enumerate(rowValue):
                ui.ProductTable.setItem(
                    rowIndexes,
                    columnIndexes,
                    QTableWidgetItem(str(columnValue)),
                )

    except Exception as error:
        ui.statusbar.showMessage("This error was encountered: " + str(error), 3000)


def removeProduct():
    question = QMessageBox.question(
        MainWindow,
        "Delete Record",
        "Are you sure you want to delete the record?",
        QMessageBox.Yes | QMessageBox.No,
    )
    if question == QMessageBox.Yes:
        selected = ui.ProductTable.selectedItems()
        productId = int(selected[0].text())
        try:
            cursor.execute("DELETE FROM stock WHERE id='%s'" % (productId))
            connection.commit()
            productListing()
            ui.statusbar.showMessage("Registration deletion was successful...", 10000)
            pass
        except Exception as error:
            ui.statusbar.showMessage("This error was encountered: " + str(error), 3000)

    else:
        ui.statusbar.showMessage("Registration Delete process canceled...", 3000)


def exportDatabase():
    fname, _ = QFileDialog.getSaveFileName(
        None, "Export File", "", "All Files (*);;xlsx Files (*.xlsx)"
    )
    if fname:
        try:
            headers = [
                "id",
                "productName",
                "productType",
                "quantity",
                "quantityPrice",
                "mountingType",
                "description",
            ]
            workBook = Workbook(fname)
            worksheet = workBook.add_worksheet()

            for indexes, values in enumerate(headers):
                worksheet.write(0, indexes, values)

            data = cursor.execute("SELECT * FROM stock")
            for rowIndexes, rowValues in enumerate(data):
                for columnIndexes, columnValues in enumerate(rowValues):
                    worksheet.write(rowIndexes + 1, columnIndexes, columnValues)
            workBook.close()
            ui.statusbar.showMessage(
                "Data from the database was successfully transferred to Excel", 3000
            )
        except Exception as error:
            ui.statusbar.showMessage("This error was encountered: " + str(error), 3000)


def importDatabase():
    fname, _ = QFileDialog.getOpenFileName(
        None, "Import File", "", "All Files (*);;xlsx Files (*.xlsx)"
    )

    if fname:
        try:
            data = pd.ExcelFile(fname)

            for sheet in data.sheet_names:
                df = pd.read_excel(fname)
                df.to_sql("stock", connection, index=False, if_exists="replace")
            productListing()

        except Exception as error:
            ui.statusbar.showMessage("This error was encountered: " + str(error), 3000)


ui.ProductAdd.clicked.connect(addProduct)

ui.ProductTable.itemSelectionChanged.connect(bringRecords)

ui.ProductUpdate.clicked.connect(productUpdate)

ui.ProductSearch.clicked.connect(searhProduct)

ui.ProductList.clicked.connect(productListing)

ui.ProductDelete.clicked.connect(removeProduct)

ui.actionExport_CSV.triggered.connect(exportDatabase)

ui.actionImport_csv.triggered.connect(importDatabase)

sys.exit(mainApp.exec_())
