# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLCDNumber, QLabel, QLineEdit, QMainWindow,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(587, 385)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(33)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(100, 0))
        MainWindow.setMaximumSize(QSize(700, 400))
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"background-color: rgb(100, 100, 100);")
        self.actionnew = QAction(MainWindow)
        self.actionnew.setObjectName(u"actionnew")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Parametrs = QGroupBox(self.centralwidget)
        self.Parametrs.setObjectName(u"Parametrs")
        self.Parametrs.setGeometry(QRect(10, 10, 470, 235))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(100)
        sizePolicy1.setVerticalStretch(100)
        sizePolicy1.setHeightForWidth(self.Parametrs.sizePolicy().hasHeightForWidth())
        self.Parametrs.setSizePolicy(sizePolicy1)
        self.Parametrs.setMaximumSize(QSize(470, 235))
        self.Parametrs.setStyleSheet(u"border-color: rgb(194, 194, 194);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";\n"
"")
        self.layoutWidget = QWidget(self.Parametrs)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 70, 421, 24))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.lineEdit_4 = QLineEdit(self.layoutWidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(30)
        sizePolicy2.setVerticalStretch(30)
        sizePolicy2.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy2)
        self.lineEdit_4.setStyleSheet(u"color: rgb(0, 255, 0);\n"
"font: 700 9pt \"Segoe UI\";")

        self.horizontalLayout_2.addWidget(self.lineEdit_4)

        self.layoutWidget1 = QWidget(self.Parametrs)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(30, 30, 421, 25))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";")

        self.horizontalLayout.addWidget(self.label)

        self.lcdNumber = QLCDNumber(self.layoutWidget1)
        self.lcdNumber.setObjectName(u"lcdNumber")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(60)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lcdNumber.sizePolicy().hasHeightForWidth())
        self.lcdNumber.setSizePolicy(sizePolicy3)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.lcdNumber.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.lcdNumber.setStyleSheet(u"border-color: rgb(255, 255, 0);\n"
"color: rgb(255, 255, 0);\n"
"selection-color: rgb(255, 255, 0);")
        self.lcdNumber.setFrameShape(QFrame.Shape.Box)
        self.lcdNumber.setDigitCount(22)
        self.lcdNumber.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)
        self.lcdNumber.setProperty("value", 22.000000000000000)

        self.horizontalLayout.addWidget(self.lcdNumber)

        self.layoutWidget2 = QWidget(self.Parametrs)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(30, 110, 421, 40))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.layoutWidget2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font: 700 9pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.lineEdit_5 = QLineEdit(self.layoutWidget2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        sizePolicy1.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy1)
        self.lineEdit_5.setSizeIncrement(QSize(100, 0))
        self.lineEdit_5.setStyleSheet(u"color: rgb(0, 255, 0);\n"
"font: 700 9pt \"Segoe UI\";\n"
"\n"
"border: 2px inset;")

        self.horizontalLayout_3.addWidget(self.lineEdit_5)

        self.layoutWidget_2 = QWidget(self.Parametrs)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(30, 150, 421, 24))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.layoutWidget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";")

        self.horizontalLayout_4.addWidget(self.label_7)

        self.lineEdit_6 = QLineEdit(self.layoutWidget_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        sizePolicy2.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy2)
        self.lineEdit_6.setStyleSheet(u"font: 700 9pt \"Segoe UI\";\n"
"color: rgb(0, 255, 0);")

        self.horizontalLayout_4.addWidget(self.lineEdit_6)

        self.layoutWidget_3 = QWidget(self.Parametrs)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(30, 190, 421, 24))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.layoutWidget_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";")

        self.horizontalLayout_5.addWidget(self.label_8)

        self.lineEdit_7 = QLineEdit(self.layoutWidget_3)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        sizePolicy2.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy2)
        self.lineEdit_7.setStyleSheet(u"\n"
"color: rgb(0, 255, 0);\n"
"font: 700 9pt \"Segoe UI\";")

        self.horizontalLayout_5.addWidget(self.lineEdit_7)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionnew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.Parametrs.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043a\u043e\u0440\u0430\u0431\u043b\u044f", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0433\u0435\u0440\u043c\u0435\u0442\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0443\u0435\u0442", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430 \u043d\u0430 \u0431\u043e\u0440\u0442\u0443", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043a \u21161", None))
        self.lineEdit_5.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0440\u043c\u0430", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043a \u21162", None))
        self.lineEdit_6.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0440\u043c\u0430", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043a \u21163", None))
        self.lineEdit_7.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0440\u043c\u0430", None))
    # retranslateUi

