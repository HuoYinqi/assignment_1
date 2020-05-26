import sys
from PyQt5 import QtWidgets

from josephus.adapter.qt_interface import JosephusWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = JosephusWindow()
    window.show()
    sys.exit(app.exec_())
    