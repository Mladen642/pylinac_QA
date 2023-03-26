# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui_blueprint.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(666, 262)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.FieldAnalysis = QtWidgets.QGroupBox(self.centralwidget)
        self.FieldAnalysis.setGeometry(QtCore.QRect(20, 80, 141, 121))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.FieldAnalysis.setFont(font)
        self.FieldAnalysis.setObjectName("FieldAnalysis")
        self.fa_about = QtWidgets.QPushButton(self.FieldAnalysis)
        self.fa_about.setGeometry(QtCore.QRect(120, 8, 20, 20))
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(True)
        self.fa_about.setFont(font)
        self.fa_about.setObjectName("fa_about")
        self.fa_elekta = QtWidgets.QRadioButton(self.FieldAnalysis)
        self.fa_elekta.setGeometry(QtCore.QRect(10, 30, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.fa_elekta.setFont(font)
        self.fa_elekta.setObjectName("fa_elekta")
        self.fa_varian = QtWidgets.QRadioButton(self.FieldAnalysis)
        self.fa_varian.setGeometry(QtCore.QRect(10, 54, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.fa_varian.setFont(font)
        self.fa_varian.setObjectName("fa_varian")
        self.fa_calculate = QtWidgets.QPushButton(self.FieldAnalysis)
        self.fa_calculate.setGeometry(QtCore.QRect(3, 89, 81, 28))
        self.fa_calculate.setObjectName("fa_calculate")
        self.welcomeTitle = QtWidgets.QLabel(self.centralwidget)
        self.welcomeTitle.setGeometry(QtCore.QRect(20, 8, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.welcomeTitle.setFont(font)
        self.welcomeTitle.setObjectName("welcomeTitle")
        self.hline_div_main = QtWidgets.QFrame(self.centralwidget)
        self.hline_div_main.setGeometry(QtCore.QRect(20, 50, 621, 16))
        self.hline_div_main.setFrameShape(QtWidgets.QFrame.HLine)
        self.hline_div_main.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hline_div_main.setObjectName("hline_div_main")
        self.PlanarImaging = QtWidgets.QGroupBox(self.centralwidget)
        self.PlanarImaging.setGeometry(QtCore.QRect(180, 80, 141, 121))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.PlanarImaging.setFont(font)
        self.PlanarImaging.setObjectName("PlanarImaging")
        self.pi_about = QtWidgets.QPushButton(self.PlanarImaging)
        self.pi_about.setGeometry(QtCore.QRect(120, 8, 20, 20))
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(True)
        self.pi_about.setFont(font)
        self.pi_about.setObjectName("pi_about")
        self.pi_LasVegas = QtWidgets.QRadioButton(self.PlanarImaging)
        self.pi_LasVegas.setGeometry(QtCore.QRect(10, 30, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pi_LasVegas.setFont(font)
        self.pi_LasVegas.setObjectName("pi_LasVegas")
        self.pi_LeedsTOR = QtWidgets.QRadioButton(self.PlanarImaging)
        self.pi_LeedsTOR.setGeometry(QtCore.QRect(10, 54, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pi_LeedsTOR.setFont(font)
        self.pi_LeedsTOR.setObjectName("pi_LeedsTOR")
        self.pi_calculate = QtWidgets.QPushButton(self.PlanarImaging)
        self.pi_calculate.setGeometry(QtCore.QRect(3, 89, 81, 28))
        self.pi_calculate.setObjectName("pi_calculate")
        self.CatPhan = QtWidgets.QGroupBox(self.centralwidget)
        self.CatPhan.setGeometry(QtCore.QRect(340, 80, 141, 121))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.CatPhan.setFont(font)
        self.CatPhan.setObjectName("CatPhan")
        self.cat_about = QtWidgets.QPushButton(self.CatPhan)
        self.cat_about.setGeometry(QtCore.QRect(120, 8, 20, 20))
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(True)
        self.cat_about.setFont(font)
        self.cat_about.setObjectName("cat_about")
        self.cat_503 = QtWidgets.QRadioButton(self.CatPhan)
        self.cat_503.setGeometry(QtCore.QRect(10, 30, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.cat_503.setFont(font)
        self.cat_503.setObjectName("cat_503")
        self.cat_504 = QtWidgets.QRadioButton(self.CatPhan)
        self.cat_504.setGeometry(QtCore.QRect(10, 54, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.cat_504.setFont(font)
        self.cat_504.setObjectName("cat_504")
        self.cat_calculate = QtWidgets.QPushButton(self.CatPhan)
        self.cat_calculate.setGeometry(QtCore.QRect(3, 89, 81, 28))
        self.cat_calculate.setObjectName("cat_calculate")
        self.WinstonLutz = QtWidgets.QGroupBox(self.centralwidget)
        self.WinstonLutz.setGeometry(QtCore.QRect(500, 80, 141, 121))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.WinstonLutz.setFont(font)
        self.WinstonLutz.setObjectName("WinstonLutz")
        self.wl_about = QtWidgets.QPushButton(self.WinstonLutz)
        self.wl_about.setGeometry(QtCore.QRect(120, 8, 20, 20))
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(True)
        self.wl_about.setFont(font)
        self.wl_about.setObjectName("wl_about")
        self.wl_vanilla = QtWidgets.QRadioButton(self.WinstonLutz)
        self.wl_vanilla.setGeometry(QtCore.QRect(10, 30, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.wl_vanilla.setFont(font)
        self.wl_vanilla.setObjectName("wl_vanilla")
        self.wl_multi = QtWidgets.QRadioButton(self.WinstonLutz)
        self.wl_multi.setGeometry(QtCore.QRect(10, 54, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.wl_multi.setFont(font)
        self.wl_multi.setObjectName("wl_multi")
        self.wl_calculate = QtWidgets.QPushButton(self.WinstonLutz)
        self.wl_calculate.setGeometry(QtCore.QRect(3, 89, 81, 28))
        self.wl_calculate.setObjectName("wl_calculate")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setMouseTracking(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 666, 26))
        self.menuBar.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menuBar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionRestart = QtWidgets.QAction(MainWindow)
        self.actionRestart.setObjectName("actionRestart")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionFull_documentation = QtWidgets.QAction(MainWindow)
        self.actionFull_documentation.setObjectName("actionFull_documentation")
        self.menuFile.addAction(self.actionAbout)
        self.menuFile.addAction(self.actionFull_documentation)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionRestart)
        self.menuFile.addAction(self.actionExit)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pylinac QA"))
        self.FieldAnalysis.setTitle(_translate("MainWindow", "Field Analysis"))
        self.fa_about.setText(_translate("MainWindow", "?"))
        self.fa_elekta.setText(_translate("MainWindow", "Elekta"))
        self.fa_varian.setText(_translate("MainWindow", "Varian"))
        self.fa_calculate.setText(_translate("MainWindow", "Calculate"))
        self.welcomeTitle.setText(_translate("MainWindow", "Quick QA with pylinac"))
        self.PlanarImaging.setTitle(_translate("MainWindow", "Planar Imaging"))
        self.pi_about.setText(_translate("MainWindow", "?"))
        self.pi_LasVegas.setText(_translate("MainWindow", "LasVegas"))
        self.pi_LeedsTOR.setText(_translate("MainWindow", "LeedsTOR"))
        self.pi_calculate.setText(_translate("MainWindow", "Calculate"))
        self.CatPhan.setTitle(_translate("MainWindow", "CatPhan"))
        self.cat_about.setText(_translate("MainWindow", "?"))
        self.cat_503.setText(_translate("MainWindow", "CatPhan503"))
        self.cat_504.setText(_translate("MainWindow", "CatPhan504"))
        self.cat_calculate.setText(_translate("MainWindow", "Calculate"))
        self.WinstonLutz.setTitle(_translate("MainWindow", "Winston-Lutz"))
        self.wl_about.setText(_translate("MainWindow", "?"))
        self.wl_vanilla.setText(_translate("MainWindow", "Vanilla"))
        self.wl_multi.setText(_translate("MainWindow", "Multi target"))
        self.wl_calculate.setText(_translate("MainWindow", "Calculate"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionRestart.setText(_translate("MainWindow", "Restart"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionFull_documentation.setText(_translate("MainWindow", "Full documentation"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
