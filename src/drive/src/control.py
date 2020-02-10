#!/usr/bin/env python

import rospy
from joystick.msg import JoyStick
from module.drive import Drive


car = Drive()


# JoyStick callback function
def car_drive(joy):
    car.steering = int((joy.steering * 70) + 350)
    car.throttle = int((joy.throttle * 40) + 290)
    if joy.brk_status == True:
        car.car_brake()
    else:
        car.drive()
    if joy.rec_status == True:
        car.rec_status = True
    else:
        car.rec_status = False


rospy.init_node('CarController_listener')
sub = rospy.Subscriber('/joystick', JoyStick, car_drive)
rospy.spin()