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

import win32api, win32con
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
            
            
            # vehicle is an instance of the Vehicle class
            #print("Autopilot Firmware version: %s" % vehicle.version)
            #print("Autopilot capabilities (supports ftp): %s" % vehicle.capabilities.ftp)
            #print("Global Location: %s" % vehicle.location.global_frame)
            #print("Global Location (relative altitude): %s" % vehicle.location.global_relative_frame)
            #print("Local Location: %s" % vehicle.location.local_frame)    #NED
            #print("Attitude: %s" % vehicle.attitude)
            #print("Velocity: %s" % vehicle.velocity)
            #print("GPS: %s" % vehicle.gps_0)
            #print("Groundspeed: %s" % vehicle.groundspeed)
            #print("Airspeed: %s" % vehicle.airspeed)
            #print("Gimbal status: %s" % vehicle.gimbal)
            #print("Battery: %s" % vehicle.battery)
            #print("EKF OK?: %s" % vehicle.ekf_ok)
            #print("Last Heartbeat: %s" % vehicle.last_heartbeat)
            #print("Rangefinder: %s" % vehicle.rangefinder)
            #print("Rangefinder distance: %s" % vehicle.rangefinder.distance)
            #print("Rangefinder voltage: %s" % vehicle.rangefinder.voltage)
            #print("Heading: %s" % vehicle.heading)
            #print("Is Armable?: %s" % vehicle.is_armable)
            #print("System status: %s" % vehicle.system_status.state)
            #print("Mode: %s" % vehicle.mode.name)    # settable
            #print("Armed: %s" % vehicle.armed)    # settable
            """
            veriler={"firmware":str(vehicle.version),"ftpdestegi":str(vehicle.capabilities.ftp),
                     "globalloc":str(vehicle.location.global_frame),"globalloc_2":str(vehicle.location.global_relative_frame),
                     "Attitude":str(vehicle.attitude),"Velocity":str(vehicle.velocity),
                     "GPS":str(vehicle.gps_0),"Groundspeed":str(vehicle.groundspeed),"Airspeed":str(vehicle.airspeed),
                     "Gimbal":str(vehicle.gimbal),"Battery":str(vehicle.battery),"EKF":str(vehicle.ekf_ok),
                     "Heartbeat":str(vehicle.last_heartbeat),"Rangefinder":str(vehicle.rangefinder),
                     "Rangefinder_Distance":str(vehicle.rangefinder.distance),
                     "Rangefinder_voltage":str(vehicle.rangefinder.voltage),"Heading":str(vehicle.heading),
                     "Armable":str(vehicle.is_armable),"status":str(vehicle.system_status.state),
                     "Mode":str(vehicle.mode.name),"Armed":str(vehicle.armed)}
            
            """
            
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
            
            
            
            self.ui.webEngineView.load(QtCore.QUrl().fromLocalFile('/test.html'))
        
        
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
      
            print(vehicle.attitude.pitch)
            


if __name__ == "__main__":
        app = QApplication(sys.argv)

        window = MainWindow()
        window.setWindowTitle("Mana Ground Station")
        window.show()

        sys.exit(app.exec_())
        








