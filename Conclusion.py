import sys
import os 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QWidget ,QMainWindow, QPlainTextEdit
from PyQt5.QtGui import QIcon, QPixmap, QFont 
from PyQt5.QtCore import pyqtSlot
from ReportGenerator import Print_document
from MainWindow import *
import MainWindow

class Conclusion(QWidget):

	def __init__(self):
		super().__init__()
		self.title = 'VAPT Tool'
		self.left = 10
		self.top = 10
		self.width = 1280
		self.height = 720
		self.doc = Print_document()
		self.doc.reinitialize_doc()


		self.initUI()

	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)

		self.font = QFont()
		self.font.setFamily('Helvetica')
		self.font.setPointSize(16)


		self.Conc = QLabel('Conclusion:',self)
		self.Conc.move(120, 105)
		self.Conc.resize(250,50)
		self.Conc.setFont(self.font)

		self.ConcBox = QPlainTextEdit(self)
		self.ConcBox.move(240, 80)
		self.ConcBox.resize(600,300)

		self.button = QPushButton('Save', self)
		self.button.move(100,300)
		self.button.resize(100,50)
		self.button.clicked.connect(self.on_click)

		self.Back_button = QPushButton('Back', self)
		self.Back_button.move(100,400)
		self.Back_button.resize(100,50)
		self.Back_button.clicked.connect(self.back)


		self.show()

	@pyqtSlot()
	def on_click(self):
		conclusion = self.ConcBox.toPlainText()
		self.doc.setConclusion(conclusion)
		name = QFileDialog.getSaveFileName(self,'Save File','/')
		self.doc.Savedoc(name)
		os.remove('Temp.docx')

	@pyqtSlot()
	def back(self):
		#self.window = QtWidgets.QMainWindow()
		self.ui = MainWindow.App1()
		self.ui.initUI()
		Conclusion.hide(self)
		#self.window.show()

    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Conclusion()
    sys.exit(app.exec_())