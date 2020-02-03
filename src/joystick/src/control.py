#!/usr/bin/env python

import rospy
from joystick.msg import JoyStick
from module.drive import Drive


car = Drive()


def joy_callback(joy):
    car.steering = int((joy.steering * 70) + 350)
    car.throttle = int((joy.throttle * 40) + 290)
    if joy.brake == True:
        car.car_brake()
    else:
        car.drive()


rospy.init_node('joystick_sub')
sub = rospy.Subscriber('joystick', JoyStick, joy_callback)
rospy.spin()