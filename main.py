import sys
# pip install pyqt6
from PyQt6 import QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from gui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        self.uic.Button_start.clicked.connect(self.link_pics)
        self.uic.Button_next.clicked.connect(self.next_pic)
        self.uic.Button_back.clicked.connect(self.back_pic)
        self.i = 0
        self.a = None

    def link_pics(self):
        files = QFileDialog.getOpenFileNames(filter="*.png *.jpg")
        self.a = files[0]
        print(self.a)
        print(len(self.a))
        self.show_pic(i=0)

    def next_pic(self):
        if self.i < len(self.a)-1:
            self.i += 1
            print(self.i)
            self.show_pic(self.i)

    def back_pic(self):
        if self.i > 0:
            self.i -= 1
            print(self.i)
            self.show_pic(self.i)

    def show_pic(self, i):
        self.uic.screen.setPixmap(QtGui.QPixmap(self.a[i]))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())