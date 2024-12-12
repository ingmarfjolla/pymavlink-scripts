from __future__ import print_function

import time

from pymavlink import mavutil
import sys
import os

os.environ['MAVLINK20'] = '1'
connection = mavutil.mavlink_connection("/dev/ttyUSB1", baud=57600, dialect='common')

print('success')
connection.mav.heartbeat_send(mavutil.mavlink.MAV_TYPE_GCS,
                                              mavutil.mavlink.MAV_AUTOPILOT_INVALID, 0, 0, 0)
print('success')
# connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (connection.target_system, connection.target_component))

while True:
        msg = connection.recv_match(blocking=True)
        if msg is not None:
            # print all received messages
            raw_bytes = msg.get_msgbuf()
            print(f"Raw bytes: {raw_bytes.hex()}")
            msg_type = msg.get_type()
            print(f"Received message: {msg_type}")

            # if msg_type == "HEARTBEAT":
            #     print(f"Heartbeat from system (system {msg.system_status})")
            #     print(f"Autopilot: {msg.autopilot}, Type: {msg.type}, Base Mode: {msg.base_mode}, System Status: {msg.system_status}")
            # if msg_type == "STATUSTEXT":
            #     print(f"Status Text: {msg.text}")
            #     print(f"Status ID: {msg.id}")
            # Check for command acknowledgments
            if msg.get_type() == "COMMAND_ACK":
                print(f"Command acknowledged: {msg.command} with result: {msg.result}")