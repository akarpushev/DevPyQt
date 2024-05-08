# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculator.ui'
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
from PySide6.QtWidgets import (QApplication, QLCDNumber, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(474, 378)
        self.lcdNumber = QLCDNumber(Form)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(50, 30, 371, 51))
        self.n1 = QPushButton(Form)
        self.n1.setObjectName(u"n1")
        self.n1.setGeometry(QRect(40, 130, 41, 41))
        self.n1.setCheckable(False)
        self.n2 = QPushButton(Form)
        self.n2.setObjectName(u"n2")
        self.n2.setGeometry(QRect(90, 130, 41, 41))
        self.n3 = QPushButton(Form)
        self.n3.setObjectName(u"n3")
        self.n3.setGeometry(QRect(140, 130, 41, 41))
        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(40, 180, 41, 41))
        self.pushButton_5 = QPushButton(Form)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(90, 180, 41, 41))
        self.pushButton_6 = QPushButton(Form)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(140, 180, 41, 41))
        self.pushButton_7 = QPushButton(Form)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(90, 230, 41, 41))
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(50, 300, 371, 22))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.n1.setText(QCoreApplication.translate("Form", u"1", None))
        self.n2.setText(QCoreApplication.translate("Form", u"2", None))
        self.n3.setText(QCoreApplication.translate("Form", u"3", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"4", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"5", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"6", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"+", None))
    # retranslateUi

