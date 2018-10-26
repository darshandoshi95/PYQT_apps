'''
Created on Aug 25, 2017

@author: Burkhard A. Meier
'''

# Using the final GUI created in Video 1.3
  
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QAction 
# from PyQt5.QtGui import QIcon
#    
# class GUI(QMainWindow):             
#     def __init__(self): 
#         super().__init__()          
#         self.initUI()                           
#    
#     def initUI(self):                              
#         self.setWindowTitle('PyQt5 GUI')       
#         self.resize(400,300)               
#         self.add_menus_and_status()
#                     
#     def add_menus_and_status(self):        
#         self.statusBar().showMessage('Text in statusbar')
#           
#         menubar = self.menuBar()                
#         file_menu = menubar.addMenu('File')          
#         new_icon = QIcon('icons/new_icon.png')          
#         new_action = QAction(new_icon, 'New', self)      
#         new_action.setStatusTip('New File')                 
#         file_menu.addAction(new_action)                 
#           
#         file_menu.addSeparator()               
#           
#         exit_icon = QIcon('icons/exit_icon.png')          
#         exit_action = QAction(exit_icon, 'Exit', self)    
#         exit_action.setStatusTip('Click to exit the application')
#         exit_action.triggered.connect(self.close)       
#         exit_action.setShortcut('Ctrl+Q')                     
#         file_menu.addAction(exit_action)
#           
#         menubar.addMenu('Edit')     
#   
# if __name__ == '__main__':     
#     app = QApplication(sys.argv)            
#     gui = GUI()                         
#     gui.show()                          
#     sys.exit(app.exec_())               


#====================================================
# POSITIONAL LAYOUT WITH HARD-CODED VALUES
#====================================================
# #--------------------------------------------------
#  
# # Add label w/out text
  
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QAction 
# from PyQt5.Qt import QLabel
# from PyQt5.QtGui import QIcon
#    
# class GUI(QMainWindow):             
#     def __init__(self): 
#         super().__init__()          
#         self.initUI()                           
#    
#     def initUI(self):                              
#         self.setWindowTitle('PyQt5 GUI')     
#         self.resize(400,300)               
#         self.add_menus_and_status()
#           
#         self.positional_widget_layout()
#                        
#     def positional_widget_layout(self):
#         label = QLabel(self)             # label w/out text, window is the parent
#  
#      
#     def add_menus_and_status(self):        
#         self.statusBar().showMessage('Text in statusbar')
#           
#         menubar = self.menuBar()                
#         file_menu = menubar.addMenu('File')          
#         new_icon = QIcon('icons/new_icon.png')          
#         new_action = QAction(new_icon, 'New', self)      
#         new_action.setStatusTip('New File')                 
#         file_menu.addAction(new_action)                 
#           
#         file_menu.addSeparator()               
#           
#         exit_icon = QIcon('icons/exit_icon.png')          
#         exit_action = QAction(exit_icon, 'Exit', self)    
#         exit_action.setStatusTip('Click to exit the application')
#         exit_action.triggered.connect(self.close)       
#         exit_action.setShortcut('Ctrl+Q')                     
#         file_menu.addAction(exit_action)
#           
#         menubar.addMenu('Edit')     
#   
# if __name__ == '__main__':     
#     app = QApplication(sys.argv)            
#     gui = GUI()                         
#     gui.show()                          
#     sys.exit(app.exec_())         
#      

     

# #--------------------------------------------------
#  
# # Add label with text, default position disables menus
  
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QAction 
# from PyQt5.Qt import QLabel
# from PyQt5.QtGui import QIcon
#    
# class GUI(QMainWindow):             
#     def __init__(self): 
#         super().__init__()          
#         self.initUI()                           
#    
#     def initUI(self):                              
#         self.setWindowTitle('PyQt5 GUI')       
#         self.resize(400,300)               
#         self.add_menus_and_status()
#           
#         self.positional_widget_layout()
#           
#                   
#     def positional_widget_layout(self):
#         label = QLabel('Our first label', self)     # default position, overlays menubar
#      
#      
#     def add_menus_and_status(self):        
#         self.statusBar().showMessage('Text in statusbar')
#           
#         menubar = self.menuBar()                
#         file_menu = menubar.addMenu('File')          
#         new_icon = QIcon('icons/new_icon.png')          
#         new_action = QAction(new_icon, 'New', self)      
#         new_action.setStatusTip('New File')                 
#         file_menu.addAction(new_action)                 
#           
#         file_menu.addSeparator()               
#           
#         exit_icon = QIcon('icons/exit_icon.png')          
#         exit_action = QAction(exit_icon, 'Exit', self)    
#         exit_action.setStatusTip('Click to exit the application')
#         exit_action.triggered.connect(self.close)       
#         exit_action.setShortcut('Ctrl+Q')                     
#         file_menu.addAction(exit_action)
#           
#         menubar.addMenu('Edit')     
#   
# if __name__ == '__main__':     
#     app = QApplication(sys.argv)            
#     gui = GUI()                         
#     gui.show()                          
#     sys.exit(app.exec_())         
    
    
      
# #--------------------------------------------------
#  
# # Add label below Menubar
# 
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QAction 
# from PyQt5.Qt import QLabel
# from PyQt5.QtGui import QIcon
#    
# class GUI(QMainWindow):             
#     def __init__(self): 
#         super().__init__()          
#         self.initUI()                           
#    
#     def initUI(self):                              
#         self.setWindowTitle('PyQt5 GUI')       
#         self.resize(400,300)               
#         self.add_menus_and_status()
#           
#         self.positional_widget_layout()
#           
#                   
#     def positional_widget_layout(self):
#         label = QLabel('Our first label', self)     
#         label.move(10, 20)                       # position label below menubar
#      
#      
#     def add_menus_and_status(self):        
#         self.statusBar().showMessage('Text in statusbar')
#           
#         menubar = self.menuBar()                
#         file_menu = menubar.addMenu('File')          
#         new_icon = QIcon('icons/new_icon.png')          
#         new_action = QAction(new_icon, 'New', self)      
#         new_action.setStatusTip('New File')                 
#         file_menu.addAction(new_action)                 
#           
#         file_menu.addSeparator()               
#           
#         exit_icon = QIcon('icons/exit_icon.png')          
#         exit_action = QAction(exit_icon, 'Exit', self)    
#         exit_action.setStatusTip('Click to exit the application')
#         exit_action.triggered.connect(self.close)       
#         exit_action.setShortcut('Ctrl+Q')                     
#         file_menu.addAction(exit_action)
#           
#         menubar.addMenu('Edit')     
#   
# if __name__ == '__main__':     
#     app = QApplication(sys.argv)            
#     gui = GUI()                         
#     gui.show()                          
#     sys.exit(app.exec_())         


# #--------------------------------------------------
#   
# # Add second label
# 
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QAction 
# from PyQt5.Qt import QLabel
# from PyQt5.QtGui import QIcon
#    
# class GUI(QMainWindow):             
#     def __init__(self): 
#         super().__init__()          
#         self.initUI()                           
#    
#     def initUI(self):                              
#         self.setWindowTitle('PyQt5 GUI')       
#         self.resize(400,300)               
#         self.add_menus_and_status()
#           
#         self.positional_widget_layout()
#           
#                   
#     def positional_widget_layout(self):
#         label_1 = QLabel('Our first label', self)   
#  
#         print(self.menuBar().size())                # default size: PyQt5.QtCore.QSize(100, 30)
#         mbar_height = self.menuBar().height()  
#         print(mbar_height)
#         label_1.move(10, mbar_height)               # position label below menubar
#           
#         label_2 = QLabel('Another label', self)     # create another label
#         label_2.move(10, mbar_height * 2)           # align and position below label_1
#      
#      
#     def add_menus_and_status(self):        
#         self.statusBar().showMessage('Text in statusbar')
#           
#         menubar = self.menuBar()                
#         file_menu = menubar.addMenu('File')          
#         new_icon = QIcon('icons/new_icon.png')          
#         new_action = QAction(new_icon, 'New', self)      
#         new_action.setStatusTip('New File')                 
#         file_menu.addAction(new_action)                 
#           
#         file_menu.addSeparator()               
#           
#         exit_icon = QIcon('icons/exit_icon.png')          
#         exit_action = QAction(exit_icon, 'Exit', self)    
#         exit_action.setStatusTip('Click to exit the application')
#         exit_action.triggered.connect(self.close)       
#         exit_action.setShortcut('Ctrl+Q')                     
#         file_menu.addAction(exit_action)
#           
#         menubar.addMenu('Edit')     
#   
# if __name__ == '__main__':     
#     app = QApplication(sys.argv)            
#     gui = GUI()                         
#     gui.show()                          
#     sys.exit(app.exec_())  



# #--------------------------------------------------
#   
# # Add buttons
 
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction 
from PyQt5.Qt import QLabel, QPushButton
from PyQt5.QtGui import QIcon
    
class GUI(QMainWindow):             
    def __init__(self): 
        super().__init__()          
        self.initUI()                           
    
    def initUI(self):                              
        self.setWindowTitle('PyQt5 GUI')       
        self.resize(400,300)               
        self.add_menus_and_status()
           
        self.positional_widget_layout()
           
                   
    def positional_widget_layout(self):
        label_1 = QLabel('Our first label', self)   
  
        print(self.menuBar().size())                # default size: PyQt5.QtCore.QSize(100, 30)
        mbar_height = self.menuBar().height()  
        print(mbar_height)
        label_1.move(10, mbar_height)               # position label below menubar
           
        label_2 = QLabel('Another label', self)     # create another label
        label_2.move(10, mbar_height * 2)           # align and position below label_1
          
        button_1 = QPushButton('click 1', self)
        button_2 = QPushButton('click 2', self)
          
        button_1.move(label_1.width(), label_1.height())
        button_2.move(label_1.width(), label_1.height() * 2)
          
      
    def add_menus_and_status(self):        
        self.statusBar().showMessage('Text in statusbar')
           
        menubar = self.menuBar()                
        file_menu = menubar.addMenu('File')          
        new_icon = QIcon('icons/new_icon.png')          
        new_action = QAction(new_icon, 'New', self)      
        new_action.setStatusTip('New File')                 
        file_menu.addAction(new_action)                 
           
        file_menu.addSeparator()               
           
        exit_icon = QIcon('icons/exit_icon.png')          
        exit_action = QAction(exit_icon, 'Exit', self)    
        exit_action.setStatusTip('Click to exit the application')
        exit_action.triggered.connect(self.close)       
        exit_action.setShortcut('Ctrl+Q')                     
        file_menu.addAction(exit_action)
           
        menubar.addMenu('Edit')     
   
if __name__ == '__main__':     
    app = QApplication(sys.argv)            
    gui = GUI()                         
    gui.show()                          
    sys.exit(app.exec_())  



# #--------------------------------------------------
#   
# # resize button
# # shows alignment challenge using hard-coded values
# 
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QAction 
# from PyQt5.Qt import QLabel, QPushButton
# from PyQt5.QtGui import QIcon
#   
# class GUI(QMainWindow):             
#     def __init__(self): 
#         super().__init__()          
#         self.initUI()                           
#   
#     def initUI(self):                              
#         self.setWindowTitle('PyQt5 GUI')        
#         self.resize(400,300)               
#         self.add_menus_and_status()
#          
#         self.positional_widget_layout()
#          
#                  
#     def positional_widget_layout(self):
#         label_1 = QLabel('Our first label', self)   
# 
#         print(self.menuBar().size())                # default size: PyQt5.QtCore.QSize(100, 30)
#         mbar_height = self.menuBar().height()  
#         print(mbar_height)
#         label_1.move(10, mbar_height)               # position label below menubar
#          
#         label_2 = QLabel('Another label', self)     # create another label
#         label_2.move(10, mbar_height * 2)           # align and position below label_1
#         
#         button_1 = QPushButton('click 1', self)
#         button_2 = QPushButton('click 2', self)
#         
#         button_1.move(label_1.width(), label_1.height())
#         button_2.move(label_1.width(), label_1.height() * 2)
#         
#         button_1.resize(100, 20)                    # no longer aligned
#         
#     
#     def add_menus_and_status(self):        
#         self.statusBar().showMessage('Text in statusbar')
#          
#         menubar = self.menuBar()                
#         file_menu = menubar.addMenu('File')          
#         new_icon = QIcon('icons/new_icon.png')          
#         new_action = QAction(new_icon, 'New', self)      
#         new_action.setStatusTip('New File')                 
#         file_menu.addAction(new_action)                 
#          
#         file_menu.addSeparator()               
#          
#         exit_icon = QIcon('icons/exit_icon.png')          
#         exit_action = QAction(exit_icon, 'Exit', self)    
#         exit_action.setStatusTip('Click to exit the application')
#         exit_action.triggered.connect(self.close)       
#         exit_action.setShortcut('Ctrl+Q')                     
#         file_menu.addAction(exit_action)
#          
#         menubar.addMenu('Edit')     
#  
# if __name__ == '__main__':     
#     app = QApplication(sys.argv)            
#     gui = GUI()                         
#     gui.show()                          
#     sys.exit(app.exec_())  



