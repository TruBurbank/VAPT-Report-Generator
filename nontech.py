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
		#self.NonTechUI()

	def NonTechUI(self):
		self.setWindowTitle(self.title)
		self.setWindowIcon(QIcon("Pristine.png"))
		self.setGeometry(self.left, self.top, self.width, self.height)

		self.font = QFont()
		self.font.setFamily('Helvetica')
		self.font.setPointSize(16)

		self.VCompany = QLabel('Client Name:',self)
		self.VCompany.move(20, 5)
		self.VCompany.resize(250,50)
		self.VCompany.setFont(self.font)

		self.VCompanyBox = QLineEdit(self)
		self.VCompanyBox.move(260, 10)
		self.VCompanyBox.resize(600,30)
		self.VCompanyBox.setFont(self.font)
		self.VCompanyBox.setText('')

		self.VDate = QLabel('Start Date:',self)
		self.VDate.move(20, 50)
		self.VDate.resize(250,50)
		self.VDate.setFont(self.font)

		self.VDateBox = QLineEdit(self)
		self.VDateBox.move(260, 50)
		self.VDateBox.resize(600,30)
		self.VDateBox.setFont(self.font)

		self.VTitle = QLabel('Title:',self)
		self.VTitle.move(20, 110)
		self.VTitle.resize(250,50)
		self.VTitle.setFont(self.font)

		self.VTitleBox = QLineEdit(self)
		self.VTitleBox.move(260, 115)
		self.VTitleBox.resize(600,30)
		self.VTitleBox.setFont(self.font)
		self.VTitleBox.setText('')

		self.VAuthor = QLabel('Author:',self)
		self.VAuthor.move(20, 155)
		self.VAuthor.resize(250,50)
		self.VAuthor.setFont(self.font)

		self.VAuthorbox = QLineEdit(self)
		self.VAuthorbox.move(260, 160)
		self.VAuthorbox.resize(600,30)
		self.VAuthorbox.setText('')

		self.VManager = QLabel('Project Manager:',self)
		self.VManager.move(20, 195)
		self.VManager.resize(250,50)
		self.VManager.setFont(self.font)

		self.VManagerbox = QLineEdit(self)
		self.VManagerbox.move(260, 200)
		self.VManagerbox.resize(600,30)
		self.VManagerbox.setText('')

		self.VClassification = QLabel('Classification:',self)
		self.VClassification.move(20, 255)
		self.VClassification.resize(250,50)
		self.VClassification.setFont(self.font)

		self.VClassificationbox = QComboBox(self)
		self.VClassificationbox.addItem('Classified',1)
		self.VClassificationbox.addItem('Non-Classified',2)
		self.VClassificationbox.move(260, 260)
		self.VClassificationbox.resize(600,30)

		self.VApproach = QLabel('Approach:',self)
		self.VApproach.move(20, 305)
		self.VApproach.resize(250,50)
		self.VApproach.setFont(self.font)

		self.VApproachbox = QComboBox(self)
		self.VApproachbox.addItem('White-Box',1)
		self.VApproachbox.addItem('Black-Box',2)
		self.VApproachbox.move(260, 310)
		self.VApproachbox.resize(600,30)

		self.Rname = QLabel('Recipient Name:',self)
		self.Rname.move(20, 345)
		self.Rname.resize(250,50)
		self.Rname.setFont(self.font)

		self.Rnamebox = QLineEdit(self)
		self.Rnamebox.move(260, 350)
		self.Rnamebox.resize(600,30)
		self.Rnamebox.setText('')

		self.Rtitle = QLabel('Recipient Title',self)
		self.Rtitle.move(20, 385)
		self.Rtitle.resize(250,50)
		self.Rtitle.setFont(self.font)

		self.Rtitlebox = QLineEdit(self)
		self.Rtitlebox.move(260, 390)
		self.Rtitlebox.resize(600,30)
		self.Rtitlebox.setText('')

		self.VersionC = QLabel('Version:',self)
		self.VersionC.move(20, 325)
		self.VersionC.resize(250,50)
		self.VersionC.setFont(self.font)

		self.VersionCbox = QLineEdit(self)
		self.VersionCbox.move(260, 330)
		self.VersionCbox.resize(600,30)
		self.VersionCbox.setText('')

		self.SaveButton = QPushButton('Back', self)
		self.SaveButton.move(480,580)
		self.SaveButton.clicked.connect(self.back)
		self.SaveButton.setFont(self.font)

		self.saveReport = QPushButton('Add Vulnerabilty',self)
		self.saveReport.move(560,580)
		self.saveReport.clicked.connect(self.on_report)
		self.saveReport.setFont(self.font)

		self.ImgButton = QPushButton('Browse', self)
		self.ImgButton.move(400,580)
		#self.ImgButton.clicked.connect(self.on_browse)
		self.ImgButton.setFont(self.font)

		self.show()

	@pyqtSlot()
	def back(self):
		#self.window = QtWidgets.QMainWindow()
		self.ui = MainWindow.App1()
		self.ui.initUI()
		NonTech.hide(self)
		#self.window.show()
	@pyqtSlot()
	def on_report(self):
		self.doc.setTitle()

		cname = self.VCompanyBox.text()
		rname = self.Rnamebox.text()
		rtitle = self.Rtitlebox.text()
		Author = self.VAuthorbox.text()
		PManager = self.VManagerbox.text()
		Title = self.VTitleBox.text()
		Date= self.VDateBox.text()
		Version = self.VersionCbox.text()
		Classification = self.VClassificationbox.currentText()
		Approach = self.VApproachbox.currentText()

		self.doc.setCName(cname)

		self.doc.pageBreak()

		self.doc.AuthorTable(Author,Classification,Approach,PManager,Title,Version)
		self.doc.RecipientTable(rname,rtitle,cname)
		self.doc.VersionTable(Version,Author,Date)

		self.doc.pageBreak()
		self.doc.setSummary()

		self.doc.Savereport()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = NonTech()
    sys.exit(app.exec_())
