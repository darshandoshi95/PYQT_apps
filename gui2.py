import PyQt5
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction

class GUI (QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Pyqt window")
        
        #self.statusBar().showMessage("text")
        
        menubar=self.menuBar()
        file_menu=menubar.addMenu("file")
        
        new_action = QAction("new",self)
        file_menu.addAction(new_action)
        new_action.setStatusTip("New file")
        self.resize(400,400)
    
if __name__=="__main__":
    app = QApplication(sys.argv)
    gui=GUI()
    gui.show()
    sys.exit(app.exec_())
    
        
        
    
