# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/masaüstü/yazılımileilgilihersey/Mana Ground Station/MGS V2.0/TasarımDosyalari/MGS_derece.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(653, 540)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 631, 521))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.x = QtWidgets.QFrame(self.frame)
        self.x.setGeometry(QtCore.QRect(120, 250, 400, 16))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.x.setFont(font)
        self.x.setLineWidth(10)
        self.x.setMidLineWidth(10)
        self.x.setFrameShape(QtWidgets.QFrame.HLine)
        self.x.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.x.setObjectName("x")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(110, 60, 20, 400))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(90, 470, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.Yukseklik = QtWidgets.QLabel(self.frame)
        self.Yukseklik.setGeometry(QtCore.QRect(530, 260, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Yukseklik.setFont(font)
        self.Yukseklik.setObjectName("Yukseklik")
        self.x_deger = QtWidgets.QLabel(self.frame)
        self.x_deger.setGeometry(QtCore.QRect(150, 470, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.x_deger.setFont(font)
        self.x_deger.setObjectName("x_deger")
        self.line_4 = QtWidgets.QFrame(self.frame)
        self.line_4.setGeometry(QtCore.QRect(120, 450, 400, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(270, 20, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.hiz = QtWidgets.QLabel(self.frame)
        self.hiz.setGeometry(QtCore.QRect(50, 230, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.hiz.setFont(font)
        self.hiz.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.hiz.setObjectName("hiz")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(330, 470, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(70, 210, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.aci = QtWidgets.QLabel(self.frame)
        self.aci.setGeometry(QtCore.QRect(320, 10, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.aci.setFont(font)
        self.aci.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.aci.setObjectName("aci")
        self.y_deger = QtWidgets.QLabel(self.frame)
        self.y_deger.setGeometry(QtCore.QRect(380, 470, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.y_deger.setFont(font)
        self.y_deger.setObjectName("y_deger")
        self.y = QtWidgets.QFrame(self.frame)
        self.y.setGeometry(QtCore.QRect(310, 60, 16, 400))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.y.setFont(font)
        self.y.setLineWidth(10)
        self.y.setMidLineWidth(10)
        self.y.setFrameShape(QtWidgets.QFrame.VLine)
        self.y.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.y.setObjectName("y")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(530, 230, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(510, 60, 20, 400))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(120, 50, 400, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.baglanti = QtWidgets.QLabel(self.frame)
        self.baglanti.setGeometry(QtCore.QRect(520, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.baglanti.setFont(font)
        self.baglanti.setObjectName("baglanti")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(120, 250, 401, 211))
        self.frame_2.setStyleSheet("background-color: rgb(170, 255, 0);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(120, 60, 401, 211))
        self.frame_3.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_3.raise_()
        self.frame_2.raise_()
        self.y_deger.raise_()
        self.line.raise_()
        self.Yukseklik.raise_()
        self.label_4.raise_()
        self.x.raise_()
        self.line_4.raise_()
        self.x_deger.raise_()
        self.label.raise_()
        self.hiz.raise_()
        self.label_5.raise_()
        self.aci.raise_()
        self.label_2.raise_()
        self.y.raise_()
        self.label_3.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.x.raise_()
        self.x.raise_()
        self.line.raise_()
        self.label_4.raise_()
        self.Yukseklik.raise_()
        self.x_deger.raise_()
        self.line_4.raise_()
        self.label.raise_()
        self.hiz.raise_()
        self.label_5.raise_()
        self.label_2.raise_()
        self.aci.raise_()
        self.y_deger.raise_()
        self.y.raise_()
        self.label_3.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.baglanti.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
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
        self.label_4.setText(_translate("MainWindow", "pitch: "))
        self.Yukseklik.setText(_translate("MainWindow", "0"))
        self.x_deger.setText(_translate("MainWindow", "0"))
        self.label.setText(_translate("MainWindow", "AÇI:"))
        self.hiz.setText(_translate("MainWindow", "0"))
        self.label_5.setText(_translate("MainWindow", "roll: "))
        self.label_2.setText(_translate("MainWindow", "HIZ"))
        self.aci.setText(_translate("MainWindow", "0 "))
        self.y_deger.setText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", "Yükseklik"))
        self.baglanti.setText(_translate("MainWindow", "BEKLE"))
        self.actionT_rk_e.setText(_translate("MainWindow", "Türkçe"))
        self.action_ngilizce.setText(_translate("MainWindow", "İngilizce"))
        self.actionAlmanca.setText(_translate("MainWindow", "Almanca"))

