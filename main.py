from sbot import *
from time import sleep
from sbot import BRAKE, COAST
from sbot import GPIOPinMode

r = Robot()
my_arduino = r.arduino
coordinates = [(675,0),(1350,0),(2025,0),(2700,0),(3375,0),(4050,0),(4725,0),
               (5400,675),(5400,1350),(5400,2025),(5400,2700),(5400,3375),(5400,4050),(5400,4725),
               (4725,5400),(4050,5400),(3375,5400),(2700,5400),(2025,5400),(1350,5400),(675,5400),
               (0,4725),(0,4050),(0,3375),(0,2700),(0,2025),(0,1350),(0,675)]


found = False
base_tag = 28
my_corner_tag = base_tag + r.zone
territory_tag = []
dist = 0
angle = 0
identity = 0


##if my_corner_tag 


def turn_left():
    r.motor_board.motors[0].power = -0.2
    r.motor_board.motors[1].power = -0

def turn_right():
    r.motor_board.motors[0].power = -0
    r.motor_board.motors[1].power = -0.2

def forward():
    r.motor_board.motors[0].power = -0.2
    r.motor_board.motors[1].power = -0.2

def forward_reverse():
    r.motor_board.motors[0].power = -0.1
    r.motor_board.motors[1].power = 0.17

def reverse():
    r.motor_board.motors[0].power = 0.2
    r.motor_board.motors[1].power = 0.2

def constant_speed():
    r.motor_board.motors[0].power = COAST
    r.motor_board.motors[1].power = COAST

def stop():
    r.motor_board.motors[0].power = BRAKE
    r.motor_board.motors[1].power = BRAKE



#sensor = r.arduino.ultrasound_sensors[4, 5]

#pulse_time = sensor.pulse()

#distance = sensor.distance()
    
#print(f"time taken for pulse to reflect: {pulse_time}")
#print(f"distance to object: {distance}")




#markers = r.camera.see()
#r.power_board.piezo.buzz(0.5, Note.C6)
#r.camera.save("snapshot.jpg")
#
#for m in markers:
 #   print("distance", float(m.distance / 10))
  #  print("rotation", float((m.spherical.rot_y * 180) / 3.14))
#good = True
#while good == True:
   # forward()
    #sleep(5)
    #good = False


forward()
sleep(4)
turn_left()
sleep(1.5)
forward()
sleep(2)
reverse()
sleep(2)
turn_left()
sleep(1.5)
forward()
sleep(4.1)
turn_right()
sleep(1.7)
forward()
sleep(4)
turn_right()
sleep(1.5)
forward()
sleep(3)

#reverse()
##sleep(2)
#turn_left
#sleep(1)
#forward()
#sleep(3)
#turn_right()
#sleep(1)
#forward()
#sleep(3)
#forward_reverse()
#sleep(10)

