# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 17:02:22 2022

@author: okmen
"""

from pymavlink import mavutil

the_connection= mavutil.mavlink_connection('COM15')
print("bekleniyor")
the_connection.wait_heartbeat()
print("bağlandı")
print(the_connection.target_system,the_connection.target_component)






try: 
    altitude = the_connection.messages['GPS_RAW_INT'].alt  # Note, you can access message fields as attributes!
    timestamp = the_connection.time_since('GPS_RAW_INT')
except:
    print('No GPS_RAW_INT message received')

a=the_connection.messages["HOME"]
b=the_connection.messages["HOME"].yaw
str(b)


while 1:
    msg= the_connection.recv_match(type="ATTITUDE",blocking=True)
    print(msg)

msg = the_connection.recv_match(blocking=True)


the_connection.close()