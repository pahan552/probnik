# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'autorazation.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 7, 781, 71))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.logoLabel = QLabel(self.widget)
        self.logoLabel.setObjectName(u"logoLabel")
        self.logoLabel.setMaximumSize(QSize(64, 64))
        self.logoLabel.setPixmap(QPixmap(u"../\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0441\u0442\u043e\u043b/Images/\u0427\u0443\u0434\u043e \u041e\u0431\u0443\u0432\u044c.ico"))
        self.logoLabel.setScaledContents(True)

        self.horizontalLayout.addWidget(self.logoLabel)

        self.titleLabel = QLabel(self.widget)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setStyleSheet(u"QLabel#titleLabel {\n"
"font-family: 'Calibri';\n"
"font-size: 18pt;\n"
"font-weight: bold;\n"
"color: #70B2AF;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.titleLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.userinfolabel = QLabel(self.widget)
        self.userinfolabel.setObjectName(u"userinfolabel")
        self.userinfolabel.setStyleSheet(u"QLabel#userinfolabel {\n"
"font-family: 'Calibri';\n"
"font-size: 12pt;\n"
"font-weight: bold;\n"
"}")

        self.horizontalLayout.addWidget(self.userinfolabel)

        self.LogoutButton = QPushButton(self.widget)
        self.LogoutButton.setObjectName(u"LogoutButton")
        self.LogoutButton.setStyleSheet(u"QPushButton {\n"
"background-color: #70B2AF;\n"
"color: #FFFFFF;\n"
"border: none;\n"
"padding: 8px 16px;\n"
"font-family: 'Calibri';\n"
"font-size: 12pt;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover  {\n"
"back-ground-color: #5A9B98;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #4A8582;\n"
"}")

        self.horizontalLayout.addWidget(self.LogoutButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 19))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logoLabel.setText("")
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0430\u043b\u043e\u0433 \u0442\u043e\u0432\u0430\u0440\u043e\u0432", None))
        self.userinfolabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.LogoutButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0439\u0442\u0438", None))
    # retranslateUi

