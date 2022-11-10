# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 13:37:19 2022

@author: okmen
"""
from gmplot import gmplot
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
            global vehicle,m,harita_sayac
            
            
            
            #self.ui.webEngineView.load(QtCore.QUrl().fromLocalFile('/test.html'))
            
            harita_sayac=0
            try:
                    
                global myworker
                self.myworker = verilerial() 
                self.myworker.progress.connect(self.progressfonk)
                
                #self.myworker.surekontrol.connect(self.surekontrol_fonksiyon)            
                self.myworker.start()
            except:
                print("baslatma hatası")
            
            #lat=39.8070302
            #lon=32.3905487
            
            
            
        def progressfonk(self):
            global vehicle,m,harita_sayac
            
            
            def harita(lat,lon):
                
                
                GOOGLE_API_KEY="AIzaSyB5J2ljDu2KJ3bcbW9EyGjk5umtBLI_A0Y"
                apikey = GOOGLE_API_KEY
                gmap = gmplot.GoogleMapPlotter(39.8070302, 32.3905487, 744.57, apikey=apikey,map_type="satellite")
                gmap.marker(39.8070302, 32.3905487, 'cornflowerblue')
                gmap.draw("harita.html")


                self.ui.webEngineView.load(QtCore.QUrl().fromLocalFile('/harita.html'))
                # burada point koyma ile ilgili hata yaptık ya onu da düzelttik
                
            if (harita_sayac>20):
                 harita(lat=vehicle.location.global_frame.lat,lon=vehicle.location.global_frame.lon)
                 harita_sayac=0
            harita_sayac +=1
            self.ui.firmware.setText("Autopilot Firmware version: "+str(vehicle.version))
            self.ui.ftpdestegi.setText("Autopilot capabilities: "+str(vehicle.capabilities.ftp))
            self.ui.globalloc.setText("Global Location: "+str(vehicle.location.global_frame))
            self.ui.globalloc_2.setText(""+str(vehicle.location.global_relative_frame))
            self.ui.Attitude.setText("Attitude: "+str(vehicle.attitude))
            self.ui.Velocity.setText("Velocity: "+str(vehicle.velocity))
            self.ui.GPS.setText("GPS: "+str(vehicle.gps_0))
            self.ui.Groundspeed.setText("Groundspeed: "+str(vehicle.groundspeed))
            self.ui.Airspeed.setText("Airspeed: "+str(vehicle.airspeed))
            self.ui.Gimbal.setText("Gimbal: "+str(vehicle.gimbal))
            self.ui.Battery.setText("Battery: "+str(vehicle.battery))
            self.ui.EKF.setText("EKF: "+str(vehicle.ekf_ok))
            self.ui.Heartbeat.setText("Heartbeat: "+str(vehicle.last_heartbeat))
            self.ui.Rangefinder.setText("Rangefinder: "+str(vehicle.rangefinder))
            self.ui.Rangefinder_Distance.setText("Rangefinder Distance: "+str(vehicle.rangefinder.distance))
            self.ui.Rangefinder_voltage.setText("Rangefinder voltage: "+str(vehicle.rangefinder.voltage))
            self.ui.Heading.setText("Heading: "+str(vehicle.heading))
            self.ui.Armable.setText("Armable: "+str(vehicle.is_armable))
            self.ui.status.setText("status: "+str(vehicle.system_status.state))
            self.ui.Mode.setText("Mode: "+str(vehicle.mode.name))
            self.ui.Armed.setText("Armed: "+str(vehicle.armed))
      


if __name__ == "__main__":
        app = QApplication(sys.argv)

        window = MainWindow()
        window.setWindowTitle("Mana Ground Station- v1.0")
        window.show()

        sys.exit(app.exec_())
        








