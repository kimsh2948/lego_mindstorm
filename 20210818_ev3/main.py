#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
Grab_motor = Motor(Port.A)
left_motor = Motor(Port.B)
right_motor = Motor(Port.D)

robot = DriveBase(left_motor, right_motor, 55.5, 104)

ts = TouchSensor(Port.S1)
ultra = UltrasonicSensor(Port.S2)

cs3 = ColorSensor(Port.S3)
cs4 = ColorSensor(Port.S4)

color3 = cs3.color()
color4 = cs4.color()
reflection = cs3.reflection()
ambient = cs3.ambient()

# Write your program here.

robot.straight(100)
Grab_motor.reset_angle(0)
# Grab_motor.run_target(200, -90)

BLACK = 6
WHITE = 54
threshold = (BLACK+WHITE)/2

DRIVE_SPEED = 100
PROPORTIONAL_GAIN = 1.2

while cs4.color() != Color.BLACK
    deviation = cs3.reflection()-threshold
    turn_rate = PROPORTIONAL_GAIN * deviation
    robot.drive(DRIVE_SPEED, turn_rate)
    wait(10)

ev3.speaker.beep()

while ultra.distance() > 100:
    deviation = cs3.reflection()-threshold
    turn_rate = PROPORTIONAL_GAIN * deviation
    robot.drive(DRIVE_SPEED, turn_rate)
    wait(10)

ev3.speaker.beep()
robot.straight(100)
Grab_motor.run_until_stalled(200, then=Stop.COAST, duty_limit=50)
robot.straight(50)

robot.turn(180)

while cs4.color() != Color.BLACK:
    deviation = cs3.reflection()-threshold
    turn_rate = PROPORTIONAL_GAIN * deviation
    robot.drive(DRIVE_SPEED, turn_rate)
    wait(10)

robot.straight(50)
robot.turn(-90)
wait(500)
robot.straight(50)

while cs3.color() != Color.BLACK:
    deviation = cs4.reflection()-threshold
    turn_rate = PROPORTIONAL_GAIN * deviation
    robot.drive(DRIVE_SPEED, turn_rate)
    wait(10)

robot.turn(90)
wait(500)
robot.straight(50)

while cs3.color() != Color.RED:
    robot.drive(100, 0)

Grab_motor.reset_angle(0)
Grab_motor.run_target(200, -90)

robot.turn(180)
robot.straight(50)

while cs3.color() != Color.BLACK:
    deviation = cs4.reflection()-threshold
    turn_rate = PROPORTIONAL_GAIN * deviation
    robot.drive(DRIVE_SPEED, turn_rate)
    wait(10)

robot.turn(-90)

while cs4.color() != Color.BLACK:
    deviation = cs3.reflection()-threshold
    turn_rate = PROPORTIONAL_GAIN * deviation
    robot.drive(DRIVE_SPEED, turn_rate)
    wait(10)

robot.turn(90)

while cs4.color() != Color.BLACK:
    deviation = cs3.reflection()-threshold
    turn_rate = PROPORTIONAL_GAIN * deviation
    robot.drive(DRIVE_SPEED, turn_rate)
    wait(10)


while cs4.color() != Color.BLACK:
    deviation = cs3.reflection()-threshold
    turn_rate = PROPORTIONAL_GAIN * deviation
    robot.drive(DRIVE_SPEED, turn_rate)
    wait(10)






































