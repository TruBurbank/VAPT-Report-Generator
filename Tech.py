import sys
import os
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, QPlainTextEdit, QComboBox, QFileDialog, QTabWidget, QVBoxLayout
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot
from MainWindow import *
import MainWindow
from ReportGenerator import Print_document

class App(QWidget):

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
        self.setWindowIcon(QIcon("Prinstine.png"))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.font = QFont()
        self.font.setFamily('Helvetica')
        self.font.setPointSize(16)
        
        self.Vname = QLabel('Vulnerabilty Name:',self)
        self.Vname.move(20, 5)
        self.Vname.resize(250,50)
        self.Vname.setFont(self.font)

        self.Vnamebox = QLineEdit(self)
        self.Vnamebox.move(260, 10)
        self.Vnamebox.resize(600,30)
        self.Vnamebox.setFont(self.font)

        self.VDesc = QLabel('Vulnerabilty Description:',self)
        self.VDesc.move(20, 80)
        self.VDesc.resize(250,50)
        self.VDesc.setFont(self.font)

        self.VDescbox = QPlainTextEdit(self)
        self.VDescbox.move(260, 50)
        self.VDescbox.resize(600,100)

        self.Vurl = QLabel('Vulnearable URL:',self)
        self.Vurl.move(20, 155)
        self.Vurl.resize(250,50)
        self.Vurl.setFont(self.font)

        self.Vurlbox = QLineEdit(self)
        self.Vurlbox.move(260, 160)
        self.Vurlbox.resize(600,30)

        self.VSeverity = QLabel('Severity:',self)
        self.VSeverity.move(20, 205)
        self.VSeverity.resize(250,50)
        self.VSeverity.setFont(self.font)

        self.VSeveritybox = QComboBox(self)
        self.VSeveritybox.addItem('Critical',1)
        self.VSeveritybox.addItem('High',2)
        self.VSeveritybox.addItem('Medium',3)
        self.VSeveritybox.addItem('Low',4)
        self.VSeveritybox.addItem('Informational',5)
        self.VSeveritybox.move(260, 210)
        self.VSeveritybox.resize(600,30)

        self.VImpact = QLabel('Impact:',self)
        self.VImpact.move(20, 280)
        self.VImpact.resize(250,80)
        self.VImpact.setFont(self.font)

        self.VImpactBox = QPlainTextEdit(self)
        self.VImpactBox.move(260, 250)
        self.VImpactBox.resize(600,130)

        self.VRemediation = QLabel('Remediation:',self)
        self.VRemediation.move(20, 425)
        self.VRemediation.resize(250,50)
        self.VRemediation.setFont(self.font)

        self.VRemediationBox = QPlainTextEdit(self)
        self.VRemediationBox.move(260, 400)
        self.VRemediationBox.resize(600,100)

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
        self.ImgButton.clicked.connect(self.on_browse)
        self.ImgButton.setFont(self.font)

        self.show()

    @pyqtSlot()
    def on_report(self):
        
        vname = self.Vnamebox.text()
        print(vname)
        self.doc.setVname(vname)

        severity = self.VSeveritybox.currentText()
        self.doc.setVSeverity(severity)
        print(severity)
 
        VDesc = self.VDescbox.toPlainText() 
        self.doc.SetVdesc(VDesc)

        Vurl = self.Vurlbox.text()
        self.doc.setVurl(Vurl)

        self.doc.setImg(self.__Img)

        VImpact = self.VImpactBox.toPlainText()
        self.doc.setImpact(VImpact) 
        
        Vrem = self.VRemediationBox.toPlainText() 
        self.doc.setVremed(Vrem)

        self.doc.pageBreak()

    @pyqtSlot()
    def on_browse(self):
        self.__Img = QFileDialog.getOpenFileNames(self,'Open Files','/',("Images(*.png)"))

    @pyqtSlot()
    def on_click(self):
        self.doc.Savereport()
        
    @pyqtSlot()
    def back(self):
        #self.window = QtWidgets.QMainWindow()
        self.doc.Savereport()
        self.ui = MainWindow.App1()
        self.ui.initUI()
        App.hide(self)
        #self.window.show()

  
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    a = App.on_report()
    sys.exit(app.exec_())