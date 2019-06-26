import os
from docx import Document
from docx.shared import Inches
from docx import section
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt
from docx.shared import Cm
from docx.shared import RGBColor
import docx

class Print_document():

    def start_doc(self):
        self.document = Document()

    def reinitialize_doc(self):
        self.document = Document('Temp.docx')

    def initialize_doc(self):
        sections = self.document.sections
        for section in sections:
            section.top_margin = Cm(2.54)
            section.bottom_margin = Cm(2.54)
            section.left_margin = Cm(2.54)
            section.right_margin = Cm(2.54)


        style = self.document.styles['Normal']
        font = style.font
        font.name = 'Times New Roman'
        font.size = Pt(14)

        style = self.document.styles['Heading 2']
        font1 = style.font
        font1.name = 'TimesNewRoman'
        font1.size = Pt(16)

        header = self.document.sections[0].header
        ht0=header.add_paragraph()
        kh=ht0.add_run()
        kh.add_picture('Pristine.png', width=Inches(2))
        kh.alignment = WD_ALIGN_PARAGRAPH.LEFT

        footer = self.document.sections[0].footer
        f = footer.add_paragraph('All Rights Reserved by Pristine InfoSolutions Pvt. Ltd.')
        f.alignment = WD_ALIGN_PARAGRAPH.CENTER
        f.style = self.document.styles['Normal']
        f.bold = True
        f.size = Pt(16)


    def setVname(self,Vname):
        
        self.document.add_heading('Vulnerability Name:', 2) 
        p = self.document.add_paragraph(Vname)
        p.style = self.document.styles['Normal']

    def setVSeverity(self,severity):
        p = self.document.add_heading('Severity', 2)
        p.style = self.document.styles['Heading 2']
        p.bold = True
        p.size = Pt(16)
        p.name = 'TimesNewRoman'
        p = self.document.add_paragraph(severity)
        p.style = self.document.styles['Normal']

    def SetVdesc(self,VDesc):
        vuldesh = self.document.add_heading('Vulnerability Description:', 2)
        p = self.document.add_paragraph(VDesc)

    def setVurl(self,Vurl):
        self.document.add_heading('Vulnerable URL: ', 2)
        p = self.document.add_paragraph(Vurl)
        p.style = self.document.styles['Normal']

    def setImg(self,Img):
        self.document.add_heading('Proof of Concept: ',2)
        if (Img):
            lengthImg = len(Img[0]) 
            for i in range (0,lengthImg):
                self.document.add_picture(Img[0][i], width=Cm(15.95))

    def setImpact(self,VImpact):
        self.document.add_heading('Impact: ',2)
        p = self.document.add_paragraph(VImpact)
        p.style = self.document.styles['Normal']

    def setVremed(self,Vrem):
        self.document.add_heading('Remediation', 2 )
        p = self.document.add_paragraph(Vrem)
        p.style = self.document.styles['Normal']

    def setConclusion(self,Conclusion):
        self.document.add_heading('Conclusion', 2 )
        p = self.document.add_paragraph(Conclusion)
        p.style = self.document.styles['Normal']

    def pageBreak(self):
        self.document.add_page_break()
    

    def Savedoc(self,name):
        self.document.save(name[0] + '.docx')

    def Savereport(self):
        self.document.save('Temp.docx')