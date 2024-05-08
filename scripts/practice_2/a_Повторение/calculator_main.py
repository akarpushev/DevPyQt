from PySide6 import QtWidgets
from calculator import Ui_Form
class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.n1.clicked.connect(lambda: self.input("1"))
        self.ui.n2.clicked.connect(lambda: self.input("2"))

    def input(self, number):
        self.ui.lineEdit.setText(self.ui.lineEdit.text() + number)




if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()