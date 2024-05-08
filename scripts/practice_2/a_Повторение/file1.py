# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'file1.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(450, 300)
        self.pushButtonMirror = QPushButton(Form)
        self.pushButtonMirror.setObjectName(u"pushButtonMirror")
        self.pushButtonMirror.setGeometry(QRect(30, 190, 401, 24))
        self.radioButton = QRadioButton(Form)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(30, 160, 89, 20))
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 40, 401, 101))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEditInput = QLineEdit(self.widget)
        self.lineEditInput.setObjectName(u"lineEditInput")

        self.horizontalLayout.addWidget(self.lineEditInput)

        self.lineEditMirror = QLineEdit(self.widget)
        self.lineEditMirror.setObjectName(u"lineEditMirror")

        self.horizontalLayout.addWidget(self.lineEditMirror)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButtonMirror.setText(QCoreApplication.translate("Form", u"pushButtonMirror", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"RadioButton", None))
    # retranslateUi

