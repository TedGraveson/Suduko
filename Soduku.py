from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 300, 300)

    s00= QtWidgets.QPushButton(win)
    s00.setText("Click me")
    s00.clicked.connect(clicked)

    win.show()
    sys.exit(app.exec_())
    

def clicked():
    print("clicked")
    
window()
