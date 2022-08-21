import sys
from PySide2 import QtCore, QtWidgets, QtUiTools

if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QtWidgets.QApplication(sys.argv)
    loader = QtUiTools.QUiLoader()
    ui = loader.load('./hello.ui')
    ui.show()
    sys.exit(app.exec_())
