from logic import *
from calcpy import *
import sys
from PyQt5 import QtWidgets


class CalculatorApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.logic = CalcLogic()
        self.connect_signal_slots()

    def connect_signal_slots(self):
        self.calcButton.clicked.connect(self.perform_calc)

    def perform_calc(self):
        num1 = int(self.input1.toPlainText())
        num2 = int(self.input2.toPlainText())
        operator = self.operatorBox.currentText()

        if operator == "+":
            result = self.logic.soma(num1, num2)
        elif operator == "-":
            result = self.logic.sub(num1, num2)
        elif operator == "/":
            result = self.logic.divide(num1, num2)
        elif operator == "x":
            result = self.logic.multiply(num1, num2)
        else:
            result = "Invalid operator"

        self.resultLabel.setText(str(result))
        self.resultLabel.adjustSize()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec())
