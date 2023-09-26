from pybricks.hubs import EV3Brick
from pybricks.tools import wait
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop
from pybricks.robotics import DriveBase

ev3 = EV3Brick()
left_motor = Motor(Port.A) 
right_motor = Motor(Port.B)

def brake_motors():
    left_motor.hold()
    right_motor.hold()
    while left_motor.speed() != 0 or right_motor.speed() != 0:
        wait(1)
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)


def found_door():
    brake_motors()
    ev3.speaker.beep(100, 1000)
    
def found_wall():
    brake_motors()
    ev3.speaker.beep(1000, 500)
    wait(250)
    ev3.speaker.beep(1000, 500)
    # Teste
    
def not_found_wall():
    brake_motors()
    ev3.speaker.beep(100, 1000)
    
def alined_to_wall():
    brake_motors()
    ev3.speaker.beep(100, 1000)
    
def deu_bom_familia():
    ev3.speaker.beep(1000, 500)
    wait(250)
    ev3.speaker.beep(1000, 500)

    