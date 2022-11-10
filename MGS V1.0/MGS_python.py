# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/masaüstü/yazılımileilgilihersey/mavlink/MGS.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(968, 660)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(40, 90, 871, 481))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionT_rk_e = QtWidgets.QAction(MainWindow)
        self.actionT_rk_e.setObjectName("actionT_rk_e")
        self.action_ngilizce = QtWidgets.QAction(MainWindow)
        self.action_ngilizce.setObjectName("action_ngilizce")
        self.actionAlmanca = QtWidgets.QAction(MainWindow)
        self.actionAlmanca.setObjectName("actionAlmanca")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.actionT_rk_e.setText(_translate("MainWindow", "Türkçe"))
        self.action_ngilizce.setText(_translate("MainWindow", "İngilizce"))
        self.actionAlmanca.setText(_translate("MainWindow", "Almanca"))

