import sys

from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog

class MyPizza(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.orderButton.clicked.connect(self.printing)

        self.show()



    def printing(self):
        if self.ui.smallPizza.isChecked() or self.ui.normalPizza.isChecked() or self.ui.BigPizza.isChecked() :
            pizza = ""
            if self.ui.smallPizza.isChecked():
                pizza += " Mała pizza "
            elif self.ui.normalPizza.isChecked():
                pizza += " Średnia pizza "
            elif self.ui.BigPizza.isChecked():
                pizza += " Duza pizza "
            if self.ui.cheese.isChecked():
                pizza += " Ser x1"
            if self.ui.mushroom.isChecked():
                pizza += " Pieczarki x1 "
            if self.ui.pineaple.isChecked():
                pizza += " Ananas x1 "
            if self.ui.salami.isChecked():
                pizza += " Salami x1 "
            self.ui.wynik.setText(f'Twoje zamowienie to: {pizza}');

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyPizza()
    sys.exit(app.exec())
