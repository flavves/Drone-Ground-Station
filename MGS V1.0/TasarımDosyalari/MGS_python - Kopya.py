# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/masaüstü/yazılımileilgilihersey/mavlink/TasarımDosyalari/MGS.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(968, 660)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(680, 340, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(140, 390, 256, 192))
        self.listWidget.setObjectName("listWidget")
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
        
        
        
        #self.verticalLayout = QtWidgets.QVBoxLayout(MainWindow)
        #self.verticalLayout.setObjectName("verticalLayout")
        #self.centralwidget = QtWidgets.QWidget(MainWindow)
        #self.centralwidget.setObjectName("centralwidget")
        self.webEngineView =QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.webEngineView.setGeometry(QtCore.QRect(840, 20, 1101, 901))
        self.webEngineView.load(QtCore.QUrl().fromLocalFile('/test.html'))
        
        #self.verticalLayout.addWidget(self.webEngineView)
    
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
        
        
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.actionT_rk_e.setText(_translate("MainWindow", "Türkçe"))
        self.action_ngilizce.setText(_translate("MainWindow", "İngilizce"))
        self.actionAlmanca.setText(_translate("MainWindow", "Almanca"))

