import sys

# use to check error in module
if sys.version_info.major == 3 and sys.version_info.minor >= 10:
    import collections
    setattr(collections, "MutableMapping", collections.abc.MutableMapping)


from dronekit import connect, VehicleMode, LocationGlobalRelative
import time
from pymavlink import mavutil

vehicle = connect("127.0.0.1:14550", wait_ready=True)