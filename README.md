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

![Знімок екрана з 2023-12-13 16-03-34.png](..%2F..%2F%D0%97%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%BD%D1%8F%2F%D0%97%D0%BD%D1%96%D0%BC%D0%BA%D0%B8%20%D0%B5%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%2F%D0%97%D0%BD%D1%96%D0%BC%D0%BE%D0%BA%20%D0%B5%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20%D0%B7%202023-12-13%2016-03-34.png)
