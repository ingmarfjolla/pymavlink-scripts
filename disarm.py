from __future__ import print_function

import time

from pymavlink import mavutil
import sys
connection = mavutil.mavlink_connection("/dev/ttyUSB1", baud=57600)
connection.mav.heartbeat_send(mavutil.mavlink.MAV_TYPE_GCS,
                                               mavutil.mavlink.MAV_AUTOPILOT_INVALID, 0, 0, 0)
print('success')
connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (connection.target_system, connection.target_component))


#https://discuss.ardupilot.org/t/pymavlink-disarm-command/25425
connection.mav.command_long_send(
1, #1# autopilot system id
1, #1# autopilot component id
400, # command id, ARM/DISARM
0, # confirmation
0.0, # disarm!
21196.0,
0.0,0.0,0.0,0.0,0.0, # unused parameters for this command,
force_mavlink1=False
)
response = connection.recv_match(type='COMMAND_ACK',blocking=True)
print(response)