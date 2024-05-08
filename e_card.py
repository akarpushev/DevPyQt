# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'e_card.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(351, 147)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(351, 147))
        MainWindow.setMaximumSize(QSize(351, 147))
        MainWindow.setStyleSheet(u"background-color: rgb(85, 85, 85);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 333, 108))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(55, 0))
        self.label.setMaximumSize(QSize(55, 16777215))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(268, 0))
        self.lineEdit.setMaximumSize(QSize(268, 16777215))
        self.lineEdit.setStyleSheet(u"border: 1px solid red;\n"
"color: rgb(217, 217, 217);\n"
"")

        self.horizontalLayout.addWidget(self.lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(3)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMinimumSize(QSize(55, 0))
        self.label_2.setMaximumSize(QSize(55, 16777215))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMinimumSize(QSize(268, 20))
        self.lineEdit_2.setMaximumSize(QSize(268, 20))
        self.lineEdit_2.setStyleSheet(u"border: 1px solid red;\n"
"color: rgb(217, 217, 217);\n"
"")

        self.horizontalLayout_2.addWidget(self.lineEdit_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setMinimumSize(QSize(55, 0))
        self.label_3.setMaximumSize(QSize(55, 16777215))
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lineEdit_3 = QLineEdit(self.layoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setEnabled(True)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setMinimumSize(QSize(268, 20))
        self.lineEdit_3.setMaximumSize(QSize(268, 20))
        self.lineEdit_3.setStyleSheet(u"border: 1px solid red;\n"
"color: rgb(217, 217, 217);\n"
"")

        self.horizontalLayout_3.addWidget(self.lineEdit_3)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setMinimumSize(QSize(55, 0))
        self.label_4.setMaximumSize(QSize(55, 16777215))
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.lineEdit_4 = QLineEdit(self.layoutWidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setEnabled(True)
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setMinimumSize(QSize(268, 20))
        self.lineEdit_4.setMaximumSize(QSize(268, 20))
        self.lineEdit_4.setStyleSheet(u"border: 1px solid red;\n"
"color: rgb(217, 217, 217);\n"
"")

        self.horizontalLayout_4.addWidget(self.lineEdit_4)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0430\u0448\u0443 \u0444\u0430\u043c\u0438\u043b\u0438\u044e", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0430\u0448\u0435 \u0438\u043c\u044f", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0430\u0448\u0435 \u043e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0430\u0448 \u0442\u0435\u043b\u0435\u0444\u043e\u043d", None))
    # retranslateUi

