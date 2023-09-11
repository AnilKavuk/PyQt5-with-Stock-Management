# ---------------------Kütühaphane----------------------#
# ------------------------------------------------------#
import sys

sys.path.append("./views")
sys.path.append("./controller")

import sqlite3
from PyQt5 import *
from PyQt5.QtWidgets import *
from main_page import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *


# ---------------------Kütühaphane----------------------#
# ------------------------------------------------------#


# ---------------------Main oluştur----------------------#
# ----------------------------------------------------------------#

mainApp = QApplication(sys.argv)
MainWindow = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

MainWindow.setWindowIcon(QtGui.QIcon("./icon.ico"))
MainWindow.setWindowTitle("Stock Management")


MainWindow.show()

# ---------------------Main oluştur----------------------#


# ---------------------sinyal slot----------------------#

# ---------------------sinyal slot----------------------#


sys.exit(mainApp.exec_())
