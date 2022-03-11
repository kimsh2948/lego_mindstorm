
# Write your program here.

#직진
# robot.straight(100)
#ev3.speaker.beep()

# robot.straight(-100)
# ev3.speaker.beep()

#ex
# robot.straight(100)

# robot.turn(90)
# ev3.speaker.beep()

# robot.straight(100)

# robot.turn(90)
# ev3.speaker.beep()

# robot.straight(100)

#턴
# robot.turn(-180)
# ev3.speaker.beep()

#for
# for i in range(4):
#     robot.straight(100)
#     robot.turn(90)

#ststop
# robot.drive(100,0)
# ev3.speaker.beep()

# wait(1000)

# robot.stop()

#touch
# while True:
#     if ts.pressed():
#         print("터치센서 눌림")
#         wait(1000)
#     else:
#         print("터치센서 안눌림")
#         wait(1000)

# while True:
#     if ts.pressed():
#         ev3.speaker.beep()
#         print("터치센서 눌림")

# while not ts.pressed():
#     pass

# print("터치센서눌림")
# ev3.speaker.beep()

# distance = ultra.distance()
# print(distance)

# presence

# robot.drive(150,0)

# while ultra.distance() > 200:
#     pass

# robot.straight(-100)
# robot.stop

# color
# robot.drive(150, 0)

# while cs3.color() != Color.RED:
#     pass

# robot.stop()

# BLACK = 8
# WHITE = 85
# threshold = (BLACK+WHITE)/2

# DRIVE_SPEED = 100
# PROPORTIONAL_GAIN = 1.2

# while True:
#     deviation = line_sensor.reflection()-threshold
#     turn_rate = PROPORTIONAL_GAIN * deviation
#     robot.drive(DRIVE_SPEED, turn_rate)
#     wait(10)


# run_motor.run_until_stalled(200, then=Stip.COAST, duty_limit=50)
# ev3.speaker.beep()

Grab_motor.run_until_stalled(200, then=Stop.COAST, duty_limit=50)