from __future__ import print_function

import time
import os

from pymavlink import mavutil
import sys
os.environ['MAVLINK20'] = '1'
# borroewd from the mavproxy code base
def passphrase_to_key(passphrase):
    '''convert a passphrase to a 32 byte key'''
    import hashlib
    h = hashlib.new('sha256')
    if sys.version_info[0] >= 3:
        print("here")
        passphrase = passphrase.encode('ascii')
    h.update(passphrase)
    return h.digest()

connection = mavutil.mavlink_connection("/dev/ttyUSB0", baud=57600, dialect='common')
connection.mav.heartbeat_send(mavutil.mavlink.MAV_TYPE_GCS,
                                               mavutil.mavlink.MAV_AUTOPILOT_INVALID, 0, 0, 0)
print('success')
print(connection.mavlink20())
#connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (connection.target_system, connection.target_component))
key = passphrase_to_key("password")

connection.setup_signing(key, sign_outgoing=True)
print("signing setup complete:", connection.mav.signing is not None)
print(connection.mavlink20())
connection.mav.set_mode_send(connection.target_system,
                                mavutil.mavlink.MAV_MODE_FLAG_DECODE_POSITION_SAFETY,
                                1)
response = connection.recv_match(blocking=True)
print(response)