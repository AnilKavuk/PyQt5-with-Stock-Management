from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1269, 797)
        MainWindow.setMinimumSize(QtCore.QSize(1269, 797))
        MainWindow.setMaximumSize(QtCore.QSize(1269, 797))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/icon/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        MainWindow.setStyleSheet(
            "QToolTip\n"
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
            "}"
        )
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(320, 150, 761, 81))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_37 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        self.label_37 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.horizontalLayout_37.addWidget(self.label_37)
        self.ProductDescription = QtWidgets.QPlainTextEdit(
            self.horizontalLayoutWidget_6
        )
        self.ProductDescription.setObjectName("ProductDescription")
        self.horizontalLayout_37.addWidget(self.ProductDescription)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(630, 40, 191, 80))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_38 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.label_38 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_38.setFont(font)
        self.label_38.setObjectName("label_38")
        self.horizontalLayout_38.addWidget(self.label_38)
        self.ProductQuantity = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.ProductQuantity.setMouseTracking(False)
        self.ProductQuantity.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.ProductQuantity.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ProductQuantity.setInputMethodHints(QtCore.Qt.ImhNone)
        self.ProductQuantity.setText("")
        self.ProductQuantity.setFrame(True)
        self.ProductQuantity.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.ProductQuantity.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.ProductQuantity.setDragEnabled(False)
        self.ProductQuantity.setClearButtonEnabled(False)
        self.ProductQuantity.setObjectName("ProductQuantity")
        self.horizontalLayout_38.addWidget(self.ProductQuantity)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(1090, 40, 160, 411))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.ProductAdd = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.ProductAdd.setObjectName("ProductAdd")
        self.verticalLayout_13.addWidget(self.ProductAdd)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_13.addItem(spacerItem)
        self.ProductUpdate = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.ProductUpdate.setObjectName("ProductUpdate")
        self.verticalLayout_13.addWidget(self.ProductUpdate)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_13.addItem(spacerItem1)
        self.ProductDelete = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.ProductDelete.setObjectName("ProductDelete")
        self.verticalLayout_13.addWidget(self.ProductDelete)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_13.addItem(spacerItem2)
        self.ProductSearch = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.ProductSearch.setObjectName("ProductSearch")
        self.verticalLayout_13.addWidget(self.ProductSearch)
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_13.addItem(spacerItem3)
        self.ProductList = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.ProductList.setObjectName("ProductList")
        self.verticalLayout_13.addWidget(self.ProductList)
        spacerItem4 = QtWidgets.QSpacerItem(
            20, 230, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_13.addItem(spacerItem4)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(30, 150, 271, 80))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_39 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_39.setObjectName("horizontalLayout_39")
        self.label_39 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.horizontalLayout_39.addWidget(self.label_39)
        self.ProductMountingType = QtWidgets.QComboBox(self.horizontalLayoutWidget_5)
        self.ProductMountingType.setCurrentText("")
        self.ProductMountingType.setObjectName("ProductMountingType")
        self.ProductMountingType.addItem("")
        self.ProductMountingType.addItem("")
        self.horizontalLayout_39.addWidget(self.ProductMountingType)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 470, 1221, 271))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_14.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.ProductTable = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ProductTable.sizePolicy().hasHeightForWidth())
        self.ProductTable.setSizePolicy(sizePolicy)
        self.ProductTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ProductTable.setColumnCount(7)
        self.ProductTable.setObjectName("ProductTable")
        self.ProductTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.ProductTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ProductTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ProductTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.ProductTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.ProductTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.ProductTable.setHorizontalHeaderItem(5, item)
        self.ProductTable.horizontalHeader().setCascadingSectionResizes(False)
        self.ProductTable.horizontalHeader().setStretchLastSection(True)
        self.ProductTable.verticalHeader().setCascadingSectionResizes(False)
        self.ProductTable.verticalHeader().setSortIndicatorShown(False)
        self.ProductTable.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_14.addWidget(self.ProductTable)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 40, 271, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_40 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_40.setObjectName("horizontalLayout_40")
        self.label_40 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.horizontalLayout_40.addWidget(self.label_40)
        self.ProductName = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.ProductName.setObjectName("ProductName")
        self.horizontalLayout_40.addWidget(self.ProductName)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(860, 40, 221, 80))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_41 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_41.setObjectName("horizontalLayout_41")
        self.label_41 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_41.setFont(font)
        self.label_41.setObjectName("label_41")
        self.horizontalLayout_41.addWidget(self.label_41)
        self.ProductQuantityPrice = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.ProductQuantityPrice.setMouseTracking(False)
        self.ProductQuantityPrice.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.ProductQuantityPrice.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ProductQuantityPrice.setInputMethodHints(QtCore.Qt.ImhNone)
        self.ProductQuantityPrice.setText("")
        self.ProductQuantityPrice.setFrame(True)
        self.ProductQuantityPrice.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.ProductQuantityPrice.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.ProductQuantityPrice.setDragEnabled(False)
        self.ProductQuantityPrice.setClearButtonEnabled(False)
        self.ProductQuantityPrice.setObjectName("ProductQuantityPrice")
        self.horizontalLayout_41.addWidget(self.ProductQuantityPrice)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(330, 40, 271, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_42 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_42.setObjectName("horizontalLayout_42")
        self.label_42 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")
        self.horizontalLayout_42.addWidget(self.label_42)
        self.ProductType = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.ProductType.setObjectName("ProductType")
        self.horizontalLayout_42.addWidget(self.ProductType)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusbar.sizePolicy().hasHeightForWidth())
        self.statusbar.setSizePolicy(sizePolicy)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1269, 21))
        self.menuBar.setObjectName("menuBar")
        self.menutools = QtWidgets.QMenu(self.menuBar)
        self.menutools.setObjectName("menutools")
        MainWindow.setMenuBar(self.menuBar)
        self.actionImport_csv = QtWidgets.QAction(MainWindow)
        self.actionImport_csv.setObjectName("actionImport_csv")
        self.actionExport_CSV = QtWidgets.QAction(MainWindow)
        self.actionExport_CSV.setObjectName("actionExport_CSV")
        self.menutools.addAction(self.actionImport_csv)
        self.menutools.addAction(self.actionExport_CSV)
        self.menuBar.addAction(self.menutools.menuAction())

        self.retranslateUi(MainWindow)
        self.ProductMountingType.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Product Manager"))
        self.label_37.setText(_translate("MainWindow", "Description:"))
        self.label_38.setText(_translate("MainWindow", "Quantity:"))
        self.ProductAdd.setText(_translate("MainWindow", "Product Add"))
        self.ProductUpdate.setText(_translate("MainWindow", "Product Update"))
        self.ProductDelete.setText(_translate("MainWindow", "Product Delete"))
        self.ProductSearch.setText(_translate("MainWindow", "Product Search"))
        self.ProductList.setText(_translate("MainWindow", "Product Listing"))
        self.label_39.setText(_translate("MainWindow", "Mounting Type:"))
        self.ProductMountingType.setItemText(0, _translate("MainWindow", "DIP"))
        self.ProductMountingType.setItemText(1, _translate("MainWindow", "SMD"))
        self.ProductTable.setSortingEnabled(False)
        item = self.ProductTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Product Name"))
        item = self.ProductTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Product Type"))
        item = self.ProductTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Quantity"))
        item = self.ProductTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Quantity Price"))
        item = self.ProductTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Mounting Type"))
        item = self.ProductTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Description"))
        self.label_40.setText(_translate("MainWindow", "Product Name:"))
        self.label_41.setText(_translate("MainWindow", "Quantity Price:"))
        self.label_42.setText(_translate("MainWindow", "Product Type:"))
        self.menutools.setTitle(_translate("MainWindow", "tools"))
        self.actionImport_csv.setText(_translate("MainWindow", "Import CSV"))
        self.actionExport_CSV.setText(_translate("MainWindow", "Export CSV"))
