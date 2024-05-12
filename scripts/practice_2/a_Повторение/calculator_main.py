from PySide6 import QtWidgets
from calculator import Ui_Form
class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.n1.clicked.connect(lambda: self.input("1"))
        self.ui.n2.clicked.connect(lambda: self.input("2"))
        self.ui.n3.clicked.connect(lambda: self.input("3"))
        self.ui.n4.clicked.connect(lambda: self.input("4"))
        self.ui.n5.clicked.connect(lambda: self.input("5"))
        self.ui.n6.clicked.connect(lambda: self.input("6"))
        self.ui.n7.clicked.connect(lambda: self.input("7"))
        self.ui.n8.clicked.connect(lambda: self.input("8"))
        self.ui.n9.clicked.connect(lambda: self.input("9"))
        self.ui.n0.clicked.connect(lambda: self.input("0"))
        #self.pushButton_add.pressed.connect(lambda: self.operation(operator.add))
        self.ui.plus.connect(lambda: self.add())




    def input(self, number):
        self.ui.lineEdit.setText(self.ui.lineEdit.text() + number)

    def add(self):
        self.t = "+"
        self.label.setText(str(self.ans))




if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()