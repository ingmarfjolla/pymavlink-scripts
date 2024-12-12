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

connection.setup_signing()
# disables the safety checks, our "injected" command
connection.mav.set_mode_send(connection.target_system,
                                mavutil.mavlink.MAV_MODE_FLAG_DECODE_POSITION_SAFETY,
                                0)
message = connection.mav.command_long_send(
                        connection.target_system,
                        connection.target_component,
                        mavutil.mavlink.MAV_CMD_GET_MESSAGE_INTERVAL,
                        0,
                        0, 0, 0, 0, 0, 0, 0)
response = connection.recv_match(type='COMMAND_ACK',blocking=True)
print(response)