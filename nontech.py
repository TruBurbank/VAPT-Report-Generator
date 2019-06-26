import sys
import os
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, QPlainTextEdit, QComboBox, QFileDialog, QTabWidget, QVBoxLayout
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot
from ReportGenerator import Print_document
import MainWindow 
from MainWindow import *

class NonTech(QWidget):

	def __init__(self):
		super().__init__()
		self.title = 'VAPT Report Generator'
		self.left = 10
		self.top = 10
		self.width = 1280
		self.height = 720
		self.__Img = None
		self.__doc = None
		self.doc = Print_document()
		self.doc.start_doc()
		self.doc.initialize_doc()
		self.initUI()
        
	def initUI(self):        
		self.setWindowTitle(self.title)
		self.setWindowIcon(QIcon("Pristine.png"))
		self.setGeometry(self.left, self.top, self.width, self.height)

		self.button = QPushButton('Back', self)
		self.button.move(100,300)
		self.button.resize(100,50)
		self.button.clicked.connect(self.back)



		self.show()

	@pyqtSlot()
	def back(self):
		#self.window = QtWidgets.QMainWindow()
		self.ui = MainWindow.App1()
		self.ui.initUI()
		NonTech.hide(self)
		#self.window.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = NonTech()
    sys.exit(app.exec_())