#!/usr/bin/python3
import sys
from PySide2 import QtCore, QtWidgets

app = QtWidgets.QApplication(sys.argv)
label = QtWidgets.QLabel('<font><h1>Hello World</h1></font>')
label.show()
app.exec_()
sys.exit()
