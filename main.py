#Imports
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import  QMessageBox
import constructed_gui
import os
from datetime import datetime
import easygui
from tkinter import messagebox as msgbox
from pylinac import FieldAnalysis, Protocol, LasVegas, CatPhan503

#Directry change
current_file_path = os.path.realpath(__file__)
script_directory = os.path.dirname(current_file_path)
os.chdir(script_directory)

#Today
today = datetime.now()
str_today_date = today.strftime('%d-%m-%Y')

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = constructed_gui.Ui_MainWindow()
        self.ui.setupUi(self)
        #Icon
        icon = QIcon('img/naslov.ico')
        self.setWindowIcon(icon)

        #About buttons action
        self.ui.fa_about.clicked.connect(self.fa_desc)
        self.ui.pi_about.clicked.connect(self.pi_desc)
        self.ui.cat_about.clicked.connect(self.cat_desc)
        self.ui.wl_about.clicked.connect(self.wl_desc)

        #Calculate buttons
        self.ui.fa_calculate.clicked.connect(self.fa_calc) #FieldAnalysis
        self.ui.pi_calculate.clicked.connect(self.pi_calc) #PlanarImaging
        self.ui.cat_calculate.clicked.connect(self.cat_calc) #CatPhan


    #About message box popups
    def fa_desc(self):
        msg = QMessageBox()
        msg.setWindowTitle("About Field Analysis test...")
        msg.setText("The field analysis module allows for quick analysis of metrics from an EPID image.\n\nIn most instances, a physicist is interested in quickly calculating the flatness, symmetry, or both of the image in question. To get started, select protocol, press calculate and finally follow the prompts to complete the test.\n\nRequired file: EPID image")
        msg.setIcon(QMessageBox.Information)
        msg.setWindowIcon(QtGui.QIcon('img/naslov.ico'))
        msg.exec_()

    def pi_desc(self):
        msg = QMessageBox()
        msg.setWindowTitle("About Planar Imaging test...")
        msg.setText("The planar imaging module analyzes phantom images taken with the kV or MV imager in 2D. In this application, LasVegas and LeedsTOR phantoms are supported. However, pylinac covers a wide range of phantoms so please check the documentation for additional information.\n\nRequired file: EPID image")
        msg.setIcon(QMessageBox.Information)
        msg.setWindowIcon(QtGui.QIcon('img/naslov.ico'))
        msg.exec_() 

    def cat_desc(self):
        msg = QMessageBox()
        msg.setWindowTitle("About CatPhan test...")
        msg.setText("This CT module automatically analyzes DICOM images of a CatPhan 503 and CatPhan 504 phantoms acquired when doing CBCT or CT quality assurance.\n\nIt can analyze the HU regions and image scaling (CTP404), the high-contrast line pairs (CTP528) to calculate the modulation transfer function (MTF), the HU uniformity (CTP486), and Low Contrast (CTP515) on the corresponding slices.\n\nAcquiring a scan of a CatPhan has a few simple requirements:\n\n1) The field of view must be larger than the phantom diameter + a few cm for clearance.\n2) All modules must be visible.\n\nRequired files: Images from CBCT or CT. Must be DICOM format.")
        msg.setIcon(QMessageBox.Information)
        msg.setWindowIcon(QtGui.QIcon('img/naslov.ico'))
        msg.exec_()

    def wl_desc(self):
        msg = QMessageBox()
        msg.setWindowTitle("About WinstonLutz test...")
        msg.setText("The Winston-Lutz module loads and processes EPID images that have acquired Winston-Lutz type images.\n\nMost important features are: Couch shift instructions, automatic field & BB positioning, isocenter size determination, image plotting, axis deviation plots etc.\n\nThe images can be from any EPID and any SID. To ensure the most accurate results, a few simple tips should be followed:\n\n1) The BB should be fully within the field of view.\n2) The MLC field should be symmetric.\n3) The BB should be <2cm from the isocenter.\n\nRequired files: EPID images.")
        msg.setIcon(QMessageBox.Information)
        msg.setWindowIcon(QtGui.QIcon('img/naslov.ico'))
        msg.exec_() 

    #Calculate functions
    def fa_calc(self):
               
        #Check the radio buttons and act accordingly
        if self.ui.fa_elekta.isChecked() == True:

            try:
                fa_files_analysis = easygui.fileopenbox("Please select file(s)")
                n_fa = len(fa_files_analysis)

                fa_files_readable  = [os.path.basename(file_path) for file_path in fa_files_analysis]
                message = "\n".join(fa_files_readable)
                if n_fa < 15:
                    x = msgbox.askokcancel('Confirm selection', message)
                else:
                    x = msgbox.askokcancel('Confirm selection', 'You have selected ' + str(n_fa) + ' file(s)')

                if x != True:
                    msgbox.showerror("Error!", "No files selected! Please try again.")
                    fa_files_analysis = None
            except:
                msgbox.showerror('Error!', "You have not selected file(s) so the calculation cannot proceed.")     

            #Calculation step    
            try:
                fa_result = FieldAnalysis(fa_files_analysis)

                fa_result.analyze(protocol = Protocol.ELEKTA, invert=True)

                msgbox.showinfo("Done! Here are the results.", fa_result.results())
                fa_result.plot_analyzed_image()
                
                fa_result.publish_pdf(f'./files/pdf_reports/[QA]FieldAnalysis_{str_today_date}.pdf')
            except:
                msgbox.showerror("Error!", "Calculation failed. Please read the instructions carefully and try again.")

        elif self.ui.fa_varian.isChecked() == True:
            msgbox.showinfo("Varian", "Varian analysis not yet supported. Comming soon")
        else:
            msgbox.showwarning("Warning", "You need to select which Protocol to follow before you can continue.")
    
    def pi_calc(self):
               
        #Check the radio buttons and act accordingly
        if self.ui.pi_LasVegas.isChecked() == True:

            try:
                pi_files_analysis = easygui.fileopenbox("Please select file(s)")
                n_pi = len(pi_files_analysis)

                pi_files_readable  = [os.path.basename(file_path) for file_path in pi_files_analysis]
                message = "\n".join(pi_files_readable)

                if n_pi < 15:
                    x = msgbox.askokcancel('Confirm selection', message)
                else:
                    x = msgbox.askokcancel('Confirm selection', 'You have selected ' + str(n_pi) + ' file(s)')

                if x != True:
                    msgbox.showerror("Error!", "No files selected! Please try again.")
                    pi_files_analysis = None
            except:
                msgbox.showerror('Error!', "You have not selected file(s) so the calculation cannot proceed.")     

            #Calculation step    
            try:
                pi_result = LasVegas(pi_files_analysis)

                pi_result.analyze()

                msgbox.showinfo("Done! Here are the results.", pi_result.results())
                pi_result.plot_analyzed_image()
                
                pi_result.publish_pdf(f'./files/pdf_reports/[QA]PlanarImaging_{str_today_date}.pdf')
            except:
                msgbox.showerror("Error!", "Calculation failed. Please read the instructions carefully and try again.")

        elif self.ui.pi_LeedsTOR.isChecked() == True:
            msgbox.showinfo("LeedsTOR", "LeedsTOR analysis not yet supported. Comming soon")
        else:
            msgbox.showwarning("Warning", "You need to select which phantom to use before you can continue.")

    def cat_calc(self):
               
        #Check the radio buttons and act accordingly
        if self.ui.cat_503.isChecked() == True:

            try:
                cat_files_analysis = easygui.fileopenbox("Please select file(s)", multiple=True)
                n_cat = len(cat_files_analysis)

                cat_files_readable  = [os.path.basename(file_path) for file_path in cat_files_analysis]
                message = "\n".join(cat_files_readable)

                if n_cat < 15:
                    x = msgbox.askokcancel('Confirm selection', message)
                else:
                    x = msgbox.askokcancel('Confirm selection', 'You have selected ' + str(n_cat) + ' file(s)')

                if x != True:
                    msgbox.showerror("Error!", "No files selected! Please try again.")
                    cat_files_analysis = None
            except:
                msgbox.showerror('Error!', "You have not selected file(s) so the calculation cannot proceed.")     

            #Calculation step    
            try:
                cat_result = CatPhan503(cat_files_analysis)

                cat_result.analyze()

                msgbox.showinfo("Done! Here are the results.", cat_result.results())
                cat_result.plot_analyzed_image()
                
                cat_result.publish_pdf(f'./files/pdf_reports/[QA]CatPhan_{str_today_date}.pdf')
            except:
                msgbox.showerror("Error!", "Calculation failed. Please read the instructions carefully and try again.")

        elif self.ui.cat_504.isChecked() == True:
            msgbox.showinfo("CatPhan504", "CatPhan504 analysis not yet supported. Comming soon")
        else:
            msgbox.showwarning("Warning", "You need to select which phantom to use before you can continue.")



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()