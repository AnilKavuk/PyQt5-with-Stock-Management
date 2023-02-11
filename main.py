# ---------------------Kütühaphane----------------------#
# ------------------------------------------------------#
import sys

sys.path.append("./pages")

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
penMainWindow = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(penMainWindow)

penMainWindow.setWindowIcon(QtGui.QIcon("./icon.ico"))
penMainWindow.setWindowTitle("Stock Management")


penMainWindow.show()

# ---------------------Main oluştur----------------------#


# ---------------------sinyal slot----------------------#

# ---------------------sinyal slot----------------------#


sys.exit(mainApp.exec_())
