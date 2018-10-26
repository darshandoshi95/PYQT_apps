import sys

from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtMultimediaWidgets


class Menu(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Simple menu') 
        self.menu_status()
        self.show()
                 

        
    def menu_status(self):
        exitAct = QAction(QIcon('exit'), ' Quit', self)   

        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('File')
        fileMenu.setStatusTip("File menu")
        fileMenu.addAction(exitAct)
        fileMenu.addSeparator()
        newfile = QAction('New file',self)
        newfile.setStatusTip("New file")
        
        fileMenu.addAction(newfile)
        
        

        #bar = self.menuBar()
        edit = menubar.addMenu("Edit")
        
        edit.addAction("New")
        
        menubar.addSeparator()
        
        
        
        
               
        


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Menu()
    sys.exit(app.exec_())