from djitellopy import Tello
tello = Tello()
import time
from time import sleep

#take off to 32 in
tello.connect()
tello.takeoff()

#move up to 6 ft
tello.send_rc_control(0,0,50,0)
sleep(3.8)

#turn 12 degrees ccw
tello.send_rc_control(0,0,0,-50)
sleep(.47)

#forward 436cm (14.3 ft)
tello.send_rc_control(0,50,0,0)
sleep(3.89)

#stop moving
tello.send_rc_control(0,0,0,0)

#land
tello.land
