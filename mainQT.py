import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp, QWidget, QVBoxLayout, QTabWidget, QPushButton, \
    QInputDialog, QLineEdit


class app (QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('Ready')

        menubar = self.menuBar()
        fichierMenu = menubar.addMenu("Fichier")

        openAct = QAction("Ouvrir",self)
        openAct.triggered.connect(self.open)
        openAct.setShortcut('ctrl+O')
        openAct.setStatusTip('Ouvrir un fichier')

        recAct = QAction("Enregistrer",self)
        recAct.triggered.connect(self.rec)
        recAct.setShortcut('ctrl+S')
        recAct.setStatusTip('Enregistrer un fichier')


        quitAct = QAction("Quitter",self)
        quitAct.triggered.connect(self.exit)
        quitAct.setShortcut('ctrl+Q')
        quitAct.setStatusTip('Quitter')



        fichierMenu.addAction(openAct)
        fichierMenu.addAction(recAct)
        fichierMenu.addSeparator()
        fichierMenu.addAction(quitAct)

        self.setMaximumSize(1280, 720)

        self.setWindowTitle('Ravi Example')

        self.myWidget = MyTableWidget(self)

        self.setCentralWidget(self.myWidget)

        self.show()

    def open(self):
        print("open")

    def rec(self):
        print("rec")

    def exit(self):
        print("exit")
        self.quit


class MyTableWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()


        # Add tabs
        self.tabs.addTab(self.tab1, "paramétre du damier")

        self.tab1.layout = QVBoxLayout(self)
        openButton = QPushButton("longueur du damier ")
        openButton.clicked.connect(self.openClick)

        openButton1 = QPushButton("largeur du damier ")
        openButton1.clicked.connect(self.openClick1)

        self.tab1.layout.addWidget(openButton)
        self.tab1.layout.addWidget(openButton1)
        self.tab1.setLayout(self.tab1.layout)



        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def openClick(self,i=-1,p=-1):
        num, ok = QInputDialog.getInt(self, "integer input dualog", "enter a number")
        print(num)
        return num

    def openClick1(self,i=-1):
        print("click")
        longueur, type = QInputDialog.getText(self, "input dialog", "largeur")
        print(longueur)
        longueur = i
        return i

if __name__ == '__main__':
    test = QApplication(sys.argv)
    ex = app()
    sys.exit(test.exec_())
