import sys
import Conclusion
import nontech 
import Tech
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QWidget ,QMainWindow
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot
from docx.shared import Cm
from Tech import *
from Conclusion import *
from nontech import *

class App1(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'VAPT Tool'
        self.left = 10
        self.top = 10
        self.width = 1280
        self.height = 720
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon("Pristine.png"))
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        button = QPushButton('Non-Technical', self)
        button.setToolTip('Enter Non-Technical information here')
        button.move(100,70)
        button.resize(100,100)
        button.clicked.connect(self.openNonTech)
        
        button = QPushButton('Technical', self)
        button.setToolTip('Enter Technical information here')
        button.move(450,70)
        button.resize(100,100)
        button.clicked.connect(self.openTech)

        button = QPushButton('Conclusion', self)
        button.setToolTip('Enter Conclusion here')
        button.move(800,70)
        button.resize(100,100)
        button.clicked.connect(self.openCon)

        '''label = QLabel(self)
        pixmap = QPixmap('Pristine.png')#.scaledToWidth(20)
        label.setPixmap(pixmap)
        label.move(450,400)
        label.resize(300,300)
        self.resize(pixmap.width(5),pixmap.height(5))'''
        
        self.show()

    @pyqtSlot()
    def openTech(self):
        #self.window = QtWidgets.QMainWindow()
        self.ui = Tech.App()
        self.ui.initUI()
        App1.hide(self)
        #self.window.show()

    @pyqtSlot()
    def openNonTech(self):
        #self.window = QtWidgets.QMainWindow()
        self.ui = nontech.NonTech()
        self.ui.initUI()
        App1.hide(self)
        #self.window.show()

    @pyqtSlot()
    def openCon(self):
        #self.window = QtWidgets.QMainWindow()
        self.ui = Conclusion.Conclusion()
        self.ui.initUI()
        #self.ui.on_report()
        App1.hide(self)
        #self.window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App1()
    sys.exit(app.exec_())
