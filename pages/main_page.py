# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main-page.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1269, 797)
        MainWindow.setMinimumSize(QtCore.QSize(1269, 797))
        MainWindow.setMaximumSize(QtCore.QSize(1269, 797))
        MainWindow.setStyleSheet("QToolTip\n"
"{\n"
"     border: 1px solid black;\n"
"     background-color: #ffa02f;\n"
"     padding: 1px;\n"
"     border-radius: 3px;\n"
"     opacity: 100;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background: #444;\n"
"    border: 1px solid #000;\n"
"    background-color: QLinearGradient(\n"
"        x1:0, y1:0,\n"
"        x2:0, y2:1,\n"
"        stop:1 #212121,\n"
"        stop:0.4 #343434/*,\n"
"        stop:0.2 #343434,\n"
"        stop:0.1 #ffaa00*/\n"
"    );\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #000;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 20px 2px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #404040;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);\n"
"}\n"
"\n"
"QWidget:focus\n"
"{\n"
"    /*border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);*/\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 12px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: #ffaa00;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"\n"
"     border-left-width: 0px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"     image: url(:/down_arrow.png);\n"
"}\n"
"\n"
"QGroupBox:focus\n"
"{\n"
"border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QTextEdit:focus\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"     border: 1px solid #222222;\n"
"     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"     height: 7px;\n"
"     margin: 0px 16px 0 16px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"      width: 7px;\n"
"      margin: 16px 0 16px 0;\n"
"      border: 1px solid #222222;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      height: 14px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);\n"
"      height: 14px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"color: #414141;\n"
"}\n"
"\n"
"QDockWidget::title\n"
"{\n"
"    text-align: center;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button\n"
"{\n"
"    text-align: center;\n"
"    spacing: 1px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover\n"
"{\n"
"    background: #242424;\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed\n"
"{\n"
"    padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #4c4c4c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QToolBar::handle\n"
"{\n"
"     spacing: 3px; /* spacing between items in the tool bar */\n"
"     background: url(:/images/handle.png);\n"
"}\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 2px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QProgressBar\n"
"{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #d7801a;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #444;\n"
"    border-bottom-style: none;\n"
"    background-color: #323232;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-right: -1px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
" margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
"\n"
"\n"
"    border-top-left-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    border-bottom-style: solid;\n"
"    margin-top: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    /*border-top: 2px solid #ffaa00;\n"
"    padding-bottom: 3px;*/\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5, fy: 0.5,\n"
"        radius: 1.0,\n"
"        stop: 0.25 #ffaa00,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    width: 9px;\n"
"    height: 9px;\n"
"}\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover, QCheckBox::indicator:hover\n"
"{\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(:/images/checkbox.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled, QRadioButton::indicator:disabled\n"
"{\n"
"    border: 1px solid #444;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1271, 771))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tabWidget.setObjectName("tabWidget")
        self.resistors = QtWidgets.QWidget()
        self.resistors.setObjectName("resistors")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.resistors)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 480, 1271, 271))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.resistorTable = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resistorTable.sizePolicy().hasHeightForWidth())
        self.resistorTable.setSizePolicy(sizePolicy)
        self.resistorTable.setObjectName("resistorTable")
        self.resistorTable.setColumnCount(6)
        self.resistorTable.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.resistorTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.resistorTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.resistorTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.resistorTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.resistorTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.resistorTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.resistorTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.resistorTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.resistorTable.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.resistorTable.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.resistorTable.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.resistorTable.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.resistorTable.setItem(0, 5, item)
        self.resistorTable.horizontalHeader().setCascadingSectionResizes(False)
        self.resistorTable.horizontalHeader().setStretchLastSection(True)
        self.resistorTable.verticalHeader().setCascadingSectionResizes(False)
        self.resistorTable.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.resistorTable)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.resistors)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 50, 271, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.RproductName = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.RproductName.setObjectName("RproductName")
        self.horizontalLayout.addWidget(self.RproductName)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.resistors)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(340, 50, 271, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.RproductType = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.RproductType.setObjectName("RproductType")
        self.horizontalLayout_2.addWidget(self.RproductType)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.resistors)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(640, 50, 191, 80))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.Rquantity = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.Rquantity.setMouseTracking(False)
        self.Rquantity.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Rquantity.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Rquantity.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Rquantity.setText("")
        self.Rquantity.setFrame(True)
        self.Rquantity.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.Rquantity.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Rquantity.setDragEnabled(False)
        self.Rquantity.setClearButtonEnabled(False)
        self.Rquantity.setObjectName("Rquantity")
        self.horizontalLayout_3.addWidget(self.Rquantity)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.resistors)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(870, 50, 221, 80))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.RquantityPrice = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.RquantityPrice.setMouseTracking(False)
        self.RquantityPrice.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.RquantityPrice.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.RquantityPrice.setInputMethodHints(QtCore.Qt.ImhNone)
        self.RquantityPrice.setText("")
        self.RquantityPrice.setFrame(True)
        self.RquantityPrice.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.RquantityPrice.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.RquantityPrice.setDragEnabled(False)
        self.RquantityPrice.setClearButtonEnabled(False)
        self.RquantityPrice.setObjectName("RquantityPrice")
        self.horizontalLayout_4.addWidget(self.RquantityPrice)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.resistors)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(40, 160, 271, 80))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.RmountingType = QtWidgets.QComboBox(self.horizontalLayoutWidget_5)
        self.RmountingType.setObjectName("RmountingType")
        self.RmountingType.addItem("")
        self.RmountingType.addItem("")
        self.horizontalLayout_6.addWidget(self.RmountingType)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.resistors)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(330, 160, 761, 81))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_16 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_17.addWidget(self.label_16)
        self.Rdescription = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget_6)
        self.Rdescription.setObjectName("Rdescription")
        self.horizontalLayout_17.addWidget(self.Rdescription)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.resistors)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(1100, 50, 160, 411))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.resistorAdd = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.resistorAdd.setObjectName("resistorAdd")
        self.verticalLayout_5.addWidget(self.resistorAdd)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.resistorUpdate = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.resistorUpdate.setObjectName("resistorUpdate")
        self.verticalLayout_5.addWidget(self.resistorUpdate)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.resistorDelete = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.resistorDelete.setObjectName("resistorDelete")
        self.verticalLayout_5.addWidget(self.resistorDelete)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.resistorSearch = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.resistorSearch.setObjectName("resistorSearch")
        self.verticalLayout_5.addWidget(self.resistorSearch)
        spacerItem3 = QtWidgets.QSpacerItem(20, 230, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.tabWidget.addTab(self.resistors, "")
        self.capacitors = QtWidgets.QWidget()
        self.capacitors.setObjectName("capacitors")
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.capacitors)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(40, 160, 271, 80))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_17 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_18.addWidget(self.label_17)
        self.CapmountingType = QtWidgets.QComboBox(self.horizontalLayoutWidget_7)
        self.CapmountingType.setObjectName("CapmountingType")
        self.CapmountingType.addItem("")
        self.CapmountingType.addItem("")
        self.horizontalLayout_18.addWidget(self.CapmountingType)
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(self.capacitors)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(330, 160, 761, 81))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_18 = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_19.addWidget(self.label_18)
        self.Capdescription = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget_8)
        self.Capdescription.setObjectName("Capdescription")
        self.horizontalLayout_19.addWidget(self.Capdescription)
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(self.capacitors)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(340, 50, 271, 80))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_19 = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_20.addWidget(self.label_19)
        self.CapproductType = QtWidgets.QLineEdit(self.horizontalLayoutWidget_9)
        self.CapproductType.setObjectName("CapproductType")
        self.horizontalLayout_20.addWidget(self.CapproductType)
        self.horizontalLayoutWidget_10 = QtWidgets.QWidget(self.capacitors)
        self.horizontalLayoutWidget_10.setGeometry(QtCore.QRect(870, 50, 221, 80))
        self.horizontalLayoutWidget_10.setObjectName("horizontalLayoutWidget_10")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_20 = QtWidgets.QLabel(self.horizontalLayoutWidget_10)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_21.addWidget(self.label_20)
        self.CapquantityPrice = QtWidgets.QLineEdit(self.horizontalLayoutWidget_10)
        self.CapquantityPrice.setMouseTracking(False)
        self.CapquantityPrice.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.CapquantityPrice.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CapquantityPrice.setInputMethodHints(QtCore.Qt.ImhNone)
        self.CapquantityPrice.setText("")
        self.CapquantityPrice.setFrame(True)
        self.CapquantityPrice.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.CapquantityPrice.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.CapquantityPrice.setDragEnabled(False)
        self.CapquantityPrice.setClearButtonEnabled(False)
        self.CapquantityPrice.setObjectName("CapquantityPrice")
        self.horizontalLayout_21.addWidget(self.CapquantityPrice)
        self.horizontalLayoutWidget_11 = QtWidgets.QWidget(self.capacitors)
        self.horizontalLayoutWidget_11.setGeometry(QtCore.QRect(640, 50, 191, 80))
        self.horizontalLayoutWidget_11.setObjectName("horizontalLayoutWidget_11")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_11)
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_21 = QtWidgets.QLabel(self.horizontalLayoutWidget_11)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_22.addWidget(self.label_21)
        self.Capquantity = QtWidgets.QLineEdit(self.horizontalLayoutWidget_11)
        self.Capquantity.setMouseTracking(False)
        self.Capquantity.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Capquantity.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Capquantity.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Capquantity.setText("")
        self.Capquantity.setFrame(True)
        self.Capquantity.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.Capquantity.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Capquantity.setDragEnabled(False)
        self.Capquantity.setClearButtonEnabled(False)
        self.Capquantity.setObjectName("Capquantity")
        self.horizontalLayout_22.addWidget(self.Capquantity)
        self.horizontalLayoutWidget_12 = QtWidgets.QWidget(self.capacitors)
        self.horizontalLayoutWidget_12.setGeometry(QtCore.QRect(40, 50, 271, 80))
        self.horizontalLayoutWidget_12.setObjectName("horizontalLayoutWidget_12")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_12)
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.label_22 = QtWidgets.QLabel(self.horizontalLayoutWidget_12)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_23.addWidget(self.label_22)
        self.CapproductName = QtWidgets.QLineEdit(self.horizontalLayoutWidget_12)
        self.CapproductName.setObjectName("CapproductName")
        self.horizontalLayout_23.addWidget(self.CapproductName)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.capacitors)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 480, 1271, 271))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.capacitorTable = QtWidgets.QTableWidget(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.capacitorTable.sizePolicy().hasHeightForWidth())
        self.capacitorTable.setSizePolicy(sizePolicy)
        self.capacitorTable.setObjectName("capacitorTable")
        self.capacitorTable.setColumnCount(6)
        self.capacitorTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.capacitorTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.capacitorTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.capacitorTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.capacitorTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.capacitorTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.capacitorTable.setHorizontalHeaderItem(5, item)
        self.capacitorTable.horizontalHeader().setCascadingSectionResizes(False)
        self.capacitorTable.horizontalHeader().setStretchLastSection(True)
        self.capacitorTable.verticalHeader().setCascadingSectionResizes(False)
        self.capacitorTable.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_2.addWidget(self.capacitorTable)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.capacitors)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(1100, 50, 160, 411))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.capacitorAdd = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.capacitorAdd.setObjectName("capacitorAdd")
        self.verticalLayout_6.addWidget(self.capacitorAdd)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem4)
        self.capacitorUpdate = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.capacitorUpdate.setObjectName("capacitorUpdate")
        self.verticalLayout_6.addWidget(self.capacitorUpdate)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem5)
        self.capacitorDelete = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.capacitorDelete.setObjectName("capacitorDelete")
        self.verticalLayout_6.addWidget(self.capacitorDelete)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem6)
        self.capacitorSearch = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.capacitorSearch.setObjectName("capacitorSearch")
        self.verticalLayout_6.addWidget(self.capacitorSearch)
        spacerItem7 = QtWidgets.QSpacerItem(20, 230, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem7)
        self.tabWidget.addTab(self.capacitors, "")
        self.coils = QtWidgets.QWidget()
        self.coils.setObjectName("coils")
        self.horizontalLayoutWidget_13 = QtWidgets.QWidget(self.coils)
        self.horizontalLayoutWidget_13.setGeometry(QtCore.QRect(40, 160, 271, 81))
        self.horizontalLayoutWidget_13.setObjectName("horizontalLayoutWidget_13")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_13)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_23 = QtWidgets.QLabel(self.horizontalLayoutWidget_13)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_5.addWidget(self.label_23)
        self.CoilmountingType = QtWidgets.QComboBox(self.horizontalLayoutWidget_13)
        self.CoilmountingType.setObjectName("CoilmountingType")
        self.CoilmountingType.addItem("")
        self.CoilmountingType.addItem("")
        self.horizontalLayout_5.addWidget(self.CoilmountingType)
        self.horizontalLayoutWidget_14 = QtWidgets.QWidget(self.coils)
        self.horizontalLayoutWidget_14.setGeometry(QtCore.QRect(330, 160, 761, 81))
        self.horizontalLayoutWidget_14.setObjectName("horizontalLayoutWidget_14")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_14)
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.label_24 = QtWidgets.QLabel(self.horizontalLayoutWidget_14)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_25.addWidget(self.label_24)
        self.Coildescription = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget_14)
        self.Coildescription.setObjectName("Coildescription")
        self.horizontalLayout_25.addWidget(self.Coildescription)
        self.horizontalLayoutWidget_15 = QtWidgets.QWidget(self.coils)
        self.horizontalLayoutWidget_15.setGeometry(QtCore.QRect(340, 50, 271, 80))
        self.horizontalLayoutWidget_15.setObjectName("horizontalLayoutWidget_15")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_15)
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.label_25 = QtWidgets.QLabel(self.horizontalLayoutWidget_15)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_26.addWidget(self.label_25)
        self.CoilproductType = QtWidgets.QLineEdit(self.horizontalLayoutWidget_15)
        self.CoilproductType.setObjectName("CoilproductType")
        self.horizontalLayout_26.addWidget(self.CoilproductType)
        self.horizontalLayoutWidget_16 = QtWidgets.QWidget(self.coils)
        self.horizontalLayoutWidget_16.setGeometry(QtCore.QRect(870, 50, 221, 80))
        self.horizontalLayoutWidget_16.setObjectName("horizontalLayoutWidget_16")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_16)
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.label_26 = QtWidgets.QLabel(self.horizontalLayoutWidget_16)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_27.addWidget(self.label_26)
        self.CoilquantityPrice = QtWidgets.QLineEdit(self.horizontalLayoutWidget_16)
        self.CoilquantityPrice.setMouseTracking(False)
        self.CoilquantityPrice.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.CoilquantityPrice.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CoilquantityPrice.setInputMethodHints(QtCore.Qt.ImhNone)
        self.CoilquantityPrice.setText("")
        self.CoilquantityPrice.setFrame(True)
        self.CoilquantityPrice.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.CoilquantityPrice.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.CoilquantityPrice.setDragEnabled(False)
        self.CoilquantityPrice.setClearButtonEnabled(False)
        self.CoilquantityPrice.setObjectName("CoilquantityPrice")
        self.horizontalLayout_27.addWidget(self.CoilquantityPrice)
        self.horizontalLayoutWidget_17 = QtWidgets.QWidget(self.coils)
        self.horizontalLayoutWidget_17.setGeometry(QtCore.QRect(640, 50, 191, 80))
        self.horizontalLayoutWidget_17.setObjectName("horizontalLayoutWidget_17")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_17)
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.label_27 = QtWidgets.QLabel(self.horizontalLayoutWidget_17)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_28.addWidget(self.label_27)
        self.Coilquantity = QtWidgets.QLineEdit(self.horizontalLayoutWidget_17)
        self.Coilquantity.setMouseTracking(False)
        self.Coilquantity.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Coilquantity.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Coilquantity.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Coilquantity.setText("")
        self.Coilquantity.setFrame(True)
        self.Coilquantity.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.Coilquantity.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Coilquantity.setDragEnabled(False)
        self.Coilquantity.setClearButtonEnabled(False)
        self.Coilquantity.setObjectName("Coilquantity")
        self.horizontalLayout_28.addWidget(self.Coilquantity)
        self.horizontalLayoutWidget_18 = QtWidgets.QWidget(self.coils)
        self.horizontalLayoutWidget_18.setGeometry(QtCore.QRect(40, 50, 271, 80))
        self.horizontalLayoutWidget_18.setObjectName("horizontalLayoutWidget_18")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_18)
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.label_28 = QtWidgets.QLabel(self.horizontalLayoutWidget_18)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_29.addWidget(self.label_28)
        self.CoilproductName = QtWidgets.QLineEdit(self.horizontalLayoutWidget_18)
        self.CoilproductName.setObjectName("CoilproductName")
        self.horizontalLayout_29.addWidget(self.CoilproductName)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.coils)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 480, 1271, 271))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.coilTable = QtWidgets.QTableWidget(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.coilTable.sizePolicy().hasHeightForWidth())
        self.coilTable.setSizePolicy(sizePolicy)
        self.coilTable.setObjectName("coilTable")
        self.coilTable.setColumnCount(6)
        self.coilTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.coilTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.coilTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.coilTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.coilTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.coilTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.coilTable.setHorizontalHeaderItem(5, item)
        self.coilTable.horizontalHeader().setCascadingSectionResizes(False)
        self.coilTable.horizontalHeader().setStretchLastSection(True)
        self.coilTable.verticalHeader().setCascadingSectionResizes(False)
        self.coilTable.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_3.addWidget(self.coilTable)
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.coils)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(1100, 50, 160, 411))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.coilAdd = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.coilAdd.setObjectName("coilAdd")
        self.verticalLayout_7.addWidget(self.coilAdd)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem8)
        self.coilUpdate = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.coilUpdate.setObjectName("coilUpdate")
        self.verticalLayout_7.addWidget(self.coilUpdate)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem9)
        self.coilDelete = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.coilDelete.setObjectName("coilDelete")
        self.verticalLayout_7.addWidget(self.coilDelete)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem10)
        self.coilSearch = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.coilSearch.setObjectName("coilSearch")
        self.verticalLayout_7.addWidget(self.coilSearch)
        spacerItem11 = QtWidgets.QSpacerItem(20, 230, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem11)
        self.tabWidget.addTab(self.coils, "")
        self.ics = QtWidgets.QWidget()
        self.ics.setObjectName("ics")
        self.horizontalLayoutWidget_19 = QtWidgets.QWidget(self.ics)
        self.horizontalLayoutWidget_19.setGeometry(QtCore.QRect(40, 160, 271, 80))
        self.horizontalLayoutWidget_19.setObjectName("horizontalLayoutWidget_19")
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_19)
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.label_29 = QtWidgets.QLabel(self.horizontalLayoutWidget_19)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_30.addWidget(self.label_29)
        self.ICmountingType = QtWidgets.QComboBox(self.horizontalLayoutWidget_19)
        self.ICmountingType.setObjectName("ICmountingType")
        self.ICmountingType.addItem("")
        self.ICmountingType.addItem("")
        self.horizontalLayout_30.addWidget(self.ICmountingType)
        self.horizontalLayoutWidget_20 = QtWidgets.QWidget(self.ics)
        self.horizontalLayoutWidget_20.setGeometry(QtCore.QRect(330, 160, 761, 81))
        self.horizontalLayoutWidget_20.setObjectName("horizontalLayoutWidget_20")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_20)
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.label_30 = QtWidgets.QLabel(self.horizontalLayoutWidget_20)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_31.addWidget(self.label_30)
        self.ICdescription = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget_20)
        self.ICdescription.setObjectName("ICdescription")
        self.horizontalLayout_31.addWidget(self.ICdescription)
        self.horizontalLayoutWidget_21 = QtWidgets.QWidget(self.ics)
        self.horizontalLayoutWidget_21.setGeometry(QtCore.QRect(340, 50, 271, 80))
        self.horizontalLayoutWidget_21.setObjectName("horizontalLayoutWidget_21")
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_21)
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.label_31 = QtWidgets.QLabel(self.horizontalLayoutWidget_21)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_32.addWidget(self.label_31)
        self.ICproductType = QtWidgets.QLineEdit(self.horizontalLayoutWidget_21)
        self.ICproductType.setObjectName("ICproductType")
        self.horizontalLayout_32.addWidget(self.ICproductType)
        self.horizontalLayoutWidget_22 = QtWidgets.QWidget(self.ics)
        self.horizontalLayoutWidget_22.setGeometry(QtCore.QRect(870, 50, 221, 80))
        self.horizontalLayoutWidget_22.setObjectName("horizontalLayoutWidget_22")
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_22)
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.label_32 = QtWidgets.QLabel(self.horizontalLayoutWidget_22)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.horizontalLayout_33.addWidget(self.label_32)
        self.ICquantityPrice = QtWidgets.QLineEdit(self.horizontalLayoutWidget_22)
        self.ICquantityPrice.setMouseTracking(False)
        self.ICquantityPrice.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.ICquantityPrice.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ICquantityPrice.setInputMethodHints(QtCore.Qt.ImhNone)
        self.ICquantityPrice.setText("")
        self.ICquantityPrice.setFrame(True)
        self.ICquantityPrice.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.ICquantityPrice.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ICquantityPrice.setDragEnabled(False)
        self.ICquantityPrice.setClearButtonEnabled(False)
        self.ICquantityPrice.setObjectName("ICquantityPrice")
        self.horizontalLayout_33.addWidget(self.ICquantityPrice)
        self.horizontalLayoutWidget_23 = QtWidgets.QWidget(self.ics)
        self.horizontalLayoutWidget_23.setGeometry(QtCore.QRect(640, 50, 191, 80))
        self.horizontalLayoutWidget_23.setObjectName("horizontalLayoutWidget_23")
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_23)
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.label_33 = QtWidgets.QLabel(self.horizontalLayoutWidget_23)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.horizontalLayout_34.addWidget(self.label_33)
        self.ICquantity = QtWidgets.QLineEdit(self.horizontalLayoutWidget_23)
        self.ICquantity.setMouseTracking(False)
        self.ICquantity.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.ICquantity.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ICquantity.setInputMethodHints(QtCore.Qt.ImhNone)
        self.ICquantity.setText("")
        self.ICquantity.setFrame(True)
        self.ICquantity.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.ICquantity.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ICquantity.setDragEnabled(False)
        self.ICquantity.setClearButtonEnabled(False)
        self.ICquantity.setObjectName("ICquantity")
        self.horizontalLayout_34.addWidget(self.ICquantity)
        self.horizontalLayoutWidget_24 = QtWidgets.QWidget(self.ics)
        self.horizontalLayoutWidget_24.setGeometry(QtCore.QRect(40, 50, 271, 80))
        self.horizontalLayoutWidget_24.setObjectName("horizontalLayoutWidget_24")
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_24)
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.label_34 = QtWidgets.QLabel(self.horizontalLayoutWidget_24)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.horizontalLayout_35.addWidget(self.label_34)
        self.ICproductName = QtWidgets.QLineEdit(self.horizontalLayoutWidget_24)
        self.ICproductName.setEnabled(True)
        self.ICproductName.setMinimumSize(QtCore.QSize(0, 0))
        self.ICproductName.setObjectName("ICproductName")
        self.horizontalLayout_35.addWidget(self.ICproductName)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.ics)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(0, 480, 1271, 271))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.icTable = QtWidgets.QTableWidget(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icTable.sizePolicy().hasHeightForWidth())
        self.icTable.setSizePolicy(sizePolicy)
        self.icTable.setObjectName("icTable")
        self.icTable.setColumnCount(6)
        self.icTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.icTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.icTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.icTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.icTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.icTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.icTable.setHorizontalHeaderItem(5, item)
        self.icTable.horizontalHeader().setCascadingSectionResizes(False)
        self.icTable.horizontalHeader().setStretchLastSection(True)
        self.icTable.verticalHeader().setCascadingSectionResizes(False)
        self.icTable.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_4.addWidget(self.icTable)
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.ics)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(1100, 50, 160, 411))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.icAdd = QtWidgets.QPushButton(self.verticalLayoutWidget_8)
        self.icAdd.setObjectName("icAdd")
        self.verticalLayout_8.addWidget(self.icAdd)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem12)
        self.icUpdate = QtWidgets.QPushButton(self.verticalLayoutWidget_8)
        self.icUpdate.setObjectName("icUpdate")
        self.verticalLayout_8.addWidget(self.icUpdate)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem13)
        self.icDelete = QtWidgets.QPushButton(self.verticalLayoutWidget_8)
        self.icDelete.setObjectName("icDelete")
        self.verticalLayout_8.addWidget(self.icDelete)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem14)
        self.icSearch = QtWidgets.QPushButton(self.verticalLayoutWidget_8)
        self.icSearch.setObjectName("icSearch")
        self.verticalLayout_8.addWidget(self.icSearch)
        spacerItem15 = QtWidgets.QSpacerItem(20, 230, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem15)
        self.tabWidget.addTab(self.ics, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusbar.sizePolicy().hasHeightForWidth())
        self.statusbar.setSizePolicy(sizePolicy)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.resistorTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "0"))
        item = self.resistorTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Product Name"))
        item = self.resistorTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Product Type"))
        item = self.resistorTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Quantity"))
        item = self.resistorTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Quantity Price"))
        item = self.resistorTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Mounting Type"))
        item = self.resistorTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Description"))
        __sortingEnabled = self.resistorTable.isSortingEnabled()
        self.resistorTable.setSortingEnabled(False)
        item = self.resistorTable.item(0, 0)
        item.setText(_translate("MainWindow", "test"))
        item = self.resistorTable.item(0, 1)
        item.setText(_translate("MainWindow", "test"))
        item = self.resistorTable.item(0, 2)
        item.setText(_translate("MainWindow", "56"))
        item = self.resistorTable.item(0, 3)
        item.setText(_translate("MainWindow", "62"))
        item = self.resistorTable.item(0, 4)
        item.setText(_translate("MainWindow", "SMD"))
        item = self.resistorTable.item(0, 5)
        item.setText(_translate("MainWindow", "test"))
        self.resistorTable.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "Product Name:"))
        self.label_2.setText(_translate("MainWindow", "Product Type:"))
        self.label_3.setText(_translate("MainWindow", "Quantity:"))
        self.Rquantity.setInputMask(_translate("MainWindow", "9999999"))
        self.label_4.setText(_translate("MainWindow", "Quantity Price:"))
        self.RquantityPrice.setInputMask(_translate("MainWindow", "9999999"))
        self.label_5.setText(_translate("MainWindow", "Mounting Type:"))
        self.RmountingType.setItemText(0, _translate("MainWindow", "Dip"))
        self.RmountingType.setItemText(1, _translate("MainWindow", "SMD"))
        self.label_16.setText(_translate("MainWindow", "Description:"))
        self.resistorAdd.setText(_translate("MainWindow", "Resistor Add"))
        self.resistorUpdate.setText(_translate("MainWindow", "Resistor Update"))
        self.resistorDelete.setText(_translate("MainWindow", "Resistor Delete"))
        self.resistorSearch.setText(_translate("MainWindow", "Resistor Search"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.resistors), _translate("MainWindow", "Resistors"))
        self.label_17.setText(_translate("MainWindow", "Mounting Type:"))
        self.CapmountingType.setItemText(0, _translate("MainWindow", "Dip"))
        self.CapmountingType.setItemText(1, _translate("MainWindow", "SMD"))
        self.label_18.setText(_translate("MainWindow", "Description:"))
        self.label_19.setText(_translate("MainWindow", "Product Type:"))
        self.label_20.setText(_translate("MainWindow", "Quantity Price:"))
        self.CapquantityPrice.setInputMask(_translate("MainWindow", "9999999"))
        self.label_21.setText(_translate("MainWindow", "Quantity:"))
        self.Capquantity.setInputMask(_translate("MainWindow", "9999999"))
        self.label_22.setText(_translate("MainWindow", "Product Name:"))
        item = self.capacitorTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Product Name"))
        item = self.capacitorTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Product Type"))
        item = self.capacitorTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Quantity"))
        item = self.capacitorTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Quantity Price"))
        item = self.capacitorTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Mounting Type"))
        item = self.capacitorTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Description"))
        self.capacitorAdd.setText(_translate("MainWindow", "Capacitor Add"))
        self.capacitorUpdate.setText(_translate("MainWindow", "Capacitor Update"))
        self.capacitorDelete.setText(_translate("MainWindow", "Capacitor Delete"))
        self.capacitorSearch.setText(_translate("MainWindow", "Capacitor Search"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.capacitors), _translate("MainWindow", "Capacitors"))
        self.label_23.setText(_translate("MainWindow", "Mounting Type:"))
        self.CoilmountingType.setItemText(0, _translate("MainWindow", "Dip"))
        self.CoilmountingType.setItemText(1, _translate("MainWindow", "SMD"))
        self.label_24.setText(_translate("MainWindow", "Description:"))
        self.label_25.setText(_translate("MainWindow", "Product Type:"))
        self.label_26.setText(_translate("MainWindow", "Quantity Price:"))
        self.CoilquantityPrice.setInputMask(_translate("MainWindow", "9999999"))
        self.label_27.setText(_translate("MainWindow", "Quantity:"))
        self.Coilquantity.setInputMask(_translate("MainWindow", "9999999"))
        self.label_28.setText(_translate("MainWindow", "Product Name:"))
        item = self.coilTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Product Name"))
        item = self.coilTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Product Type"))
        item = self.coilTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Quantity"))
        item = self.coilTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Quantity Price"))
        item = self.coilTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Mounting Type"))
        item = self.coilTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Description"))
        self.coilAdd.setText(_translate("MainWindow", "Coil Add"))
        self.coilUpdate.setText(_translate("MainWindow", "Coil Update"))
        self.coilDelete.setText(_translate("MainWindow", "Coil Delete"))
        self.coilSearch.setText(_translate("MainWindow", "Coil Search"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.coils), _translate("MainWindow", "Coils"))
        self.label_29.setText(_translate("MainWindow", "Mounting Type:"))
        self.ICmountingType.setItemText(0, _translate("MainWindow", "Dip"))
        self.ICmountingType.setItemText(1, _translate("MainWindow", "SMD"))
        self.label_30.setText(_translate("MainWindow", "Description:"))
        self.label_31.setText(_translate("MainWindow", "Product Type:"))
        self.label_32.setText(_translate("MainWindow", "Quantity Price:"))
        self.ICquantityPrice.setInputMask(_translate("MainWindow", "9999999"))
        self.label_33.setText(_translate("MainWindow", "Quantity:"))
        self.ICquantity.setInputMask(_translate("MainWindow", "9999999"))
        self.label_34.setText(_translate("MainWindow", "Product Name:"))
        item = self.icTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Product Name"))
        item = self.icTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Product Type"))
        item = self.icTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Quantity"))
        item = self.icTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Quantity Price"))
        item = self.icTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Mounting Type"))
        item = self.icTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Description"))
        self.icAdd.setText(_translate("MainWindow", "IC Add"))
        self.icUpdate.setText(_translate("MainWindow", "IC Update"))
        self.icDelete.setText(_translate("MainWindow", "IC Delete"))
        self.icSearch.setText(_translate("MainWindow", "IC Search"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ics), _translate("MainWindow", "ICs"))

