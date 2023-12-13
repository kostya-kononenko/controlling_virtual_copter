# Controlling a virtual copter

A simple program for controlling a virtual copter. 


## Brief description of the program:
The program takes off and directs the copter from point A to point B, 
after arriving at point B the copter turns to an azimuth (yaw) of 350 degrees 
and returns to point A. The flight altitude is 100 meters. 
Flight speed 20 km/h.


## How to installing and run using GitHub

- Clone this repository
- Create venv: python -m venv venv
- Activate venv: source venv/bin/activate
- Install requirements: pip install -r requirements.txt
- Crate ARDUPILOT SITL Simulator (use this link: https://ardupilot.org/dev/docs/sitl-simulator-software-in-the-loop.html)
- Launch SITL Simulator use this command:
    1. cd ~/ardupilot/ArduCopter
    2. ../Tools/autotest/sim_vehicle.py --console --map --out=udpbcast:127.0.0.1:14550 --location=50.450739,30.461242
- Run: python simple_drone.py

## Picture

![Знімок екрана з 2023-12-13 16-03-34](https://github.com/kostya-kononenko/controlling_virtual_copter/assets/107486491/414a56ba-059a-4dec-b208-b3a7b8a7542f)

## Flight video recording

https://www.loom.com/share/a981358827ad4a1c86d2edfe3574c568?sid=5ee99dc1-d251-4f4d-87ad-c5e66382f5eb
