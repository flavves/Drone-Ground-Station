# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 13:37:19 2022

@author: okmen
"""

from PyQt5.QtWidgets import QFileDialog,QLabel,QTableWidgetItem
import sys
import time
import PyQt5
#import mysql.connector
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox,QMessageBox
global suresayac
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal,Qt,QTimer



import datetime
from TasarımDosyalari.MGS_derece_python import Ui_MainWindow

import shutil
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5 import QtCore,QtGui

import io
import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QPropertyAnimation, QPoint
import folium
from PyQt5 import QtWidgets, QtWebEngineWidgets
import time
from dronekit import connect
import json

import os 

from folium import plugins
#import rioxarray as rxr
import earthpy as et
import earthpy.spatial as es


global vehicle

class verilerial(QThread):
    global vehicle

    progress = pyqtSignal()

    def __init__(self):
        super().__init__()

    def run(self):
        global vehicle
        vehicle = connect('COM15', wait_ready=True, baud=115200)
        
        while 1:
            pass
            
            self.progress.emit()
            time.sleep(0.2)
            

class MainWindow(QMainWindow):
       
        def __init__(self):
            super(MainWindow, self).__init__()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.myworker = None
            #self.ui.x.setGeometry(120, 451, 400, 16)
            global a
            a=0
            try:
                    
                global myworker
                self.myworker = verilerial() 
                self.myworker.progress.connect(self.progressfonk)
                
                #self.myworker.surekontrol.connect(self.surekontrol_fonksiyon)            
                self.myworker.start()
            except:
                print("baslatma hatası")
                
                
        def progressfonk(self):
                global a
                rad=57.2957795
                
                pitch=((vehicle.attitude.pitch)*rad)
                aci=((vehicle.attitude.yaw)*rad)
                roll=((vehicle.attitude.roll)*rad)
                hiz=vehicle.groundspeed
                yukseklik=vehicle.location.global_relative_frame.alt
                
                self.ui.Yukseklik.setText("{0:.2f}".format(yukseklik))
                self.ui.aci.setText("{0:.4f}".format(aci))
                self.ui.x_deger.setText("{0:.4f}".format(pitch))
                self.ui.y_deger.setText("{0:.4f}".format(roll))
                self.ui.hiz.setText("{0:.2f}".format(hiz))
              
                
                
                
                if pitch >0:
                        #print("yukarı")
                        self.ui.x.setGeometry(120, int(250-(pitch*2)), 400, 16)
                      
                else:
                        #print("aşağı")
                        self.ui.x.setGeometry(120, int(250+(abs(pitch*2))), 400, 16)
                
                
                
                
                #self.frame_2.setStyleSheet("background-color: rgb(170, 255, 0);")
                #self.frame_3.setStyleSheet("background-color: rgb(0, 255, 255);")
                
                if roll >0:
                        
                        self.ui.y.setGeometry(int(310+(abs(roll*2.22))), 60, 16, 400)

                        if int(310+(abs(roll*2.22)))>510:
                                kordinat=int(310+(abs(roll*2.22)))
                                #print(kordinat)
                                kordinat=abs(510-(kordinat-510))
                                self.ui.y.setGeometry(kordinat, 60, 16, 400)
                                self.ui.frame_2.setStyleSheet("background-color: rgb(0, 255, 255);")
                                self.ui.frame_3.setStyleSheet("background-color: rgb(170, 255, 0);")
                        else:
                                self.ui.frame_2.setStyleSheet("background-color: rgb(170, 255, 0);")
                                self.ui.frame_3.setStyleSheet("background-color: rgb(0, 255, 255);")       
                
                        
                else:
                        
                        self.ui.y.setGeometry(int(310-(abs(roll*2.22))), 60, 16, 400)
                        if int(310-(abs(roll*2.22)))<110:
                                kordinat=int(310-(abs(roll*2.22)))
                                
                                (110-kordinat)
                                kordinat=abs(((110-kordinat)+110))
                                self.ui.y.setGeometry(kordinat, 60, 16, 400)
                                self.ui.frame_2.setStyleSheet("background-color: rgb(0, 255, 255);")
                                self.ui.frame_3.setStyleSheet("background-color: rgb(170, 255, 0);")
                        else:
                                self.ui.frame_2.setStyleSheet("background-color: rgb(170, 255, 0);")
                                self.ui.frame_3.setStyleSheet("background-color: rgb(0, 255, 255);")
                                
                                

                if a==0:
                        self.ui.baglanti.setText(str("Bağlandı"))
                        a=1
            


if __name__ == "__main__":
        app = QApplication(sys.argv)

        window = MainWindow()
        window.setWindowTitle("Mana Ground Station- v2.0")
        window.show()
        
        sys.exit(app.exec_())
        








