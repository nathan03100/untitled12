import sys

from gui import Gui
from simulation import Simulation
import time
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp, QWidget, QVBoxLayout, QTabWidget, QPushButton, \
    QInputDialog, QLineEdit
from mainQT import app





interface = Gui()

interface.start()





'''interface.updateCell(10,10,3)'''


if __name__ == '__main__':
    test = QApplication(sys.argv)
    ex = app()
    sys.exit(test.exec_())



