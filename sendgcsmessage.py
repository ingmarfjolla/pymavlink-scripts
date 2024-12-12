from __future__ import print_function

import time

from pymavlink import mavutil
import sys

connection = mavutil.mavlink_connection("/dev/ttyUSB0", baud=57600)
print('success')

connection.mav.heartbeat_send(mavutil.mavlink.MAV_TYPE_ONBOARD_CONTROLLER,
                                              mavutil.mavlink.MAV_AUTOPILOT_INVALID, 0, 0, 0)

connection.mav.statustext_send(mavutil.mavlink.MAV_SEVERITY_NOTICE,
                           "send BTC for drone".encode())
