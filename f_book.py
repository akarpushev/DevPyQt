# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'f_book.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QStatusBar, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(290, 350)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QSize(290, 350))
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QSize(280, 16777215))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 60, 2, 2))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 10, 259, 311))
        self.verticalLayout_2 = QVBoxLayout(self.widget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.groupBox_2 = QGroupBox(self.widget1)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setStyleSheet(u"color: rgb(170, 0, 255);\n"
"border-color: rgb(130, 130, 130);\n"
"font: 700 14pt \"Segoe UI\";\n"
"background-color: rgb(0, 0, 0);\n"
"border: transparent;")
        self.textEdit = QTextEdit(self.groupBox_2)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 30, 241, 101))
        self.textEdit.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(90, 90, 90);")

        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(self.widget1)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"color: rgb(170, 0, 255);\n"
"border-color: rgb(130, 130, 130);\n"
"font: 700 14pt \"Segoe UI\";\n"
"background-color: rgb(0, 0, 0);\n"
"border: transparent;")
        self.widget2 = QWidget(self.groupBox)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(10, 50, 91, 74))
        self.verticalLayout_3 = QVBoxLayout(self.widget2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.radioButton = QRadioButton(self.widget2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 9pt \"Segoe UI\";")

        self.verticalLayout_3.addWidget(self.radioButton)

        self.radioButton_3 = QRadioButton(self.widget2)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 9pt \"Segoe UI\";")

        self.verticalLayout_3.addWidget(self.radioButton_3)

        self.radioButton_2 = QRadioButton(self.widget2)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 9pt \"Segoe UI\";")

        self.verticalLayout_3.addWidget(self.radioButton_2)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.pushButton = QPushButton(self.widget1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(130, 130, 130);")
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(False)

        self.verticalLayout_2.addWidget(self.pushButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043a\u043d\u0438\u0433\u0443", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:14pt; font-weight:700; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:400;\">\u0413\u0430\u0440\u0440\u0438 \u041f\u043e\u0442\u0442\u0435\u0440</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:400;\">\u0423\u043d\u0435\u0441\u0435\u043d\u043d\u044b\u0435 \u0432\u0435\u0442\u0440\u043e\u043c</span></p"
                        ">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:400;\">\u0412\u043e\u0439\u043d\u0430 \u0438 \u043c\u0438\u0440</span></p></body></html>", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0441\u043f\u043e\u0441\u043e\u0431 \u043e\u043f\u043b\u0430\u0442\u044b", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e \u043a\u0430\u0440\u0442\u0435", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043b\u0438\u0447\u043d\u044b\u043c\u0438", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e QR", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u043b\u0430\u0442\u0438\u0442\u044c", None))
    # retranslateUi

