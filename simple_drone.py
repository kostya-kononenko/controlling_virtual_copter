import sys

# use to check error in module
if sys.version_info.major == 3 and sys.version_info.minor >= 10:
    import collections
    setattr(collections, "MutableMapping", collections.abc.MutableMapping)


from dronekit import connect, VehicleMode, LocationGlobalRelative
import time
from pymavlink import mavutil

vehicle = connect("127.0.0.1:14550", wait_ready=True)


def arm_and_takeoff(target_altitude):
    print("Basic pre-arm checks")
    while not vehicle.is_armable:
        time.sleep(1)

    print("Arming motors")
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    while not vehicle.armed:
        time.sleep(1)

    print("Taking off!")
    vehicle.simple_takeoff(target_altitude)

    while True:
        print("Altitude: ", vehicle.location.global_relative_frame.alt)
        if (vehicle.location.global_relative_frame.alt
                >= target_altitude * 0.95):
            print("Reached target altitude")
            break
        time.sleep(1)


arm_and_takeoff(100)


def fly_to_point_b(location):
    point = LocationGlobalRelative(location[0], location[1], 100)
    vehicle.simple_goto(point, groundspeed=20)
    while True:
        distance_to_target = (
            location[0] - vehicle.location.global_relative_frame.lat,
            location[1] - vehicle.location.global_relative_frame.lon)
        print("Distance to target: ", distance_to_target)
        if (abs(distance_to_target[0]) < 0.0001
                and abs(distance_to_target[1]) < 0.0001):
            print("Reached target point")
            break
        time.sleep(1)


fly_to_point_b([50.443326, 30.448078])