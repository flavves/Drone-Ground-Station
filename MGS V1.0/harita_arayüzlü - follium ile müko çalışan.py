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
from TasarımDosyalari.MGS_python import Ui_MainWindow

import shutil
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5 import QtCore,QtGui

import io
import sys

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

            
            self.progress.emit()
            time.sleep(2)
            
    

class MainWindow(QMainWindow):
        global vehicle
        def __init__(self):
            super(MainWindow, self).__init__()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.myworker = None
            global vehicle
            
            
            
            #self.ui.webEngineView.load(QtCore.QUrl().fromLocalFile('/test.html'))
            
        
            try:
                    
                global myworker
                self.myworker = verilerial() 
                self.myworker.progress.connect(self.progressfonk)
                
                #self.myworker.surekontrol.connect(self.surekontrol_fonksiyon)            
                self.myworker.start()
            except:
                print("baslatma hatası")
        def progressfonk(self):
            global vehicle
            
            def harita(lat,lon):
                
                m = folium.Map(location=[lat, lon],zoom_start = 17)
                
                #point olusturma
                folium.Marker(
                    location=[lat, lon], 
                    popup='Drone', 
                    icon=folium.Icon()
                ).add_to(m)
                roundnum = "function(num) {return L.Util.formatNum(num, 5);};"
                plugins.MousePosition(position='topright', separator=' | ', prefix="Position:",lat_formatter=roundnum, lng_formatter=roundnum).add_to(m)

                
                data = io.BytesIO()
                m.save(data, close_file=False)
                
                self.ui.webEngineView.setHtml(data.getvalue().decode())
                
                
      
            harita(lat=vehicle.location.global_frame.lat,lon=vehicle.location.global_frame.lon)
            


if __name__ == "__main__":
        app = QApplication(sys.argv)

        window = MainWindow()
        window.setWindowTitle("Mana Ground Station")
        window.show()

        sys.exit(app.exec_())
        








