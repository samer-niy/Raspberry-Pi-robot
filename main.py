from sbot import *
from time import sleep
from sbot import BRAKE, COAST
import Rpi.GPIO as GPIO
r = Robot(wait_start=False)

while True:
    r.motor_board.motors[0].power = 0.1
    r.motor_board.motors[1].power = 0.1

    sleep(3)
    r.motor_board.motors[0].power = 0
    r.motor_board.motors[1].power = 0 # both work??
    r.motor_board.motors[0].power = BRAKE  # makes power 0 basically
    r.motor_board.motors[1].power = BRAKE
    # braking this motor makes the direction change etc right wheel turns off it goes right

    r.motor_board.motors[1].power = COAST # removes power (can still move with momentum)
    sleep(3)

def turn_right():
    r.motor_board.motors[0].power = 0.1
    r.motor_board.motors[1].power = 0

def turn_left():
    r.motor_board.motors[0].power = 0
    r.motor_board.motors[1].power = 0.1

def forward():
    r.motor_board.motors[0].power = 0.1
    r.motor_board.motors[1].power = 0.1

def forward_reverse():
    r.motor_board.motors[0].power = 0.1
    r.motor_board.motors[1].power = -0.1

def reverse():
    r.motor_board.motors[0].power = -0.1
    r.motor_board.motors[1].power = -0.1forward()

def constant_speed():
    r.motor_board.motors[0].power = COAST
    r.motor_board.motors[1].power = COAST

def stop():
    r.motor_board.motors[0].power = BRAKE
    r.motor_board.motors[1].power = BRAKE

try:
    GPIO.setmode(GPIO.BOARD)

    PIN_TRIGGER = 7
    PIN_ECHO = 11

    GPIO.setup(PIN_TRIGGER,GPIO.OUT)
    GPIO.setup(PIN_ECHO,GPIO.IN)

    GPIO.output(PIN_TRIGGER,GPIO.LOW)
    print('Waits for sensor to settle')
    time.sleep(2)

    print("Calculating distance")

    GPIO.output(PIN_TRIGGER, GPIO.HIGH)

    time.sleep(0.00001)

    GPIO.output(PIN_TRIGGER, GPIO.LOW)

    while GPIO.input(PIN_ECHO)==0:
            pulse_start_time = time.time()
    while GPIO.input(PIN_ECHO)==1:
            pulse_end_time = time.time()

    pulse_duration = pulse_end_time - pulse_start_time

    distance = round(pulse_duration * 17150, 2)

    print ("Distance:",distance,"cm")

finally:
    GPIO.cleanup()

while True:
    centre = getObstacle(0)
    left = getObstacle(1)
    right = getObstacle(2)
    time.sleep(1)
    forward()
    constant_speed()
    if distance < 20:
        stop()


forward()
constant_speed()
time.sleep(3)
turn_right()
time.sleep(1)
turn_left()
time.sleep(1)
forward()
constant_speed()
time.sleep(4)
stop()



r.waitstart()
