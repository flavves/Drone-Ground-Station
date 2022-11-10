# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 10:47:15 2022

@author: okmen
"""
"""

Bu part bizim dron verilerinmizi almamıza yarıyor.

"""

import time
from dronekit import connect
vehicle = connect('COM15', wait_ready=True, baud=115200)
rad=57.2957795
while 1:
    # vehicle is an instance of the Vehicle class
    #print("Autopilot Firmware version: %s" % vehicle.version)
    #print("Autopilot capabilities (supports ftp): %s" % vehicle.capabilities.ftp)
    #print("Global Location: %s" % vehicle.location.global_frame)
    print("Global Location (relative altitude): %s" % vehicle.location.global_relative_frame)
    #print("Local Location: %s" % vehicle.location.local_frame)    #NED
    #print((vehicle.attitude.pitch)*rad)
    #print((vehicle.attitude.yaw)*rad)
    #print((vehicle.attitude.roll)*rad)
    #pitch=((vehicle.attitude.pitch)*rad)
    #roll=((vehicle.attitude.roll)*rad)
                
    #print("pitch: "+str(pitch))
    #print("roll: "+str(roll))
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
    time.sleep(0.2)












