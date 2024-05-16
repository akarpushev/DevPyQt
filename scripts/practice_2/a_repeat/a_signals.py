"""
Файл для повторения темы сигналов

Напомнить про работу с сигналами и изменением Ui.

Предлагается создать приложение, которое принимает в lineEditInput строку от пользователя,
и при нажатии на pushButtonMirror отображает в lineEditMirror введённую строку в обратном
порядке (задом наперед).
"""

from PySide6 import QtWidgets
from file1 import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButtonMirror.clicked.connect(self.mirror)
        self.ui.lineEditInput.textChanged.connect(self.mirror)
        self.ui.lineEditMirror.textEdited.connect(lambda x: self.ui.lineEdit.setText(x[::-1]))

        self.ui.radioButton.toggled.connect(self.radioButton_toggled)


    def mirror(self):
        print(self.ui.lineEditInput.text())
        input_text = self.ui.lineEditInput.text()[::-1]
        self.ui.lineEditMirror.setText(input_text)

    def radioButton_toggled(self, param):
        if param is True:
            self.ui.lineEdit.setText("нажато")
        if param is False:
            self.ui.lineEdit.clear()







    #     self.__initUi()
    #     self.__initSignals()
    #
    # def __initUi(self):
    #     self.lineEditInput = QtWidgets.QLineEdit()
    #     self.lineEditMirror = QtWidgets.QLineEdit()
    #
    #     self.pushButtonMirror = QtWidgets.QPushButton('Mirror')
    #     self.pushButtonClear = QtWidgets.QPushButton('Clear')
    #
    # def __initSignals(self):
    #     pass
    #
    # def __onPushButtonMirrorClicked(self):
    #     pass
    #
    # def __onPushButtonClearClicked(self):
    #     pass
    #
    # def __onLineEditMirrorTextChanged(self, text):
    #     print(text)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
