#!/usr/bin/env python

import rospy
from joystick.msg import JoyStick
from module.drive import Drive


car = Drive()


def joy_callback(joy):
    Drive.steering = (joy.steering * 40) + 350
    Drive.throttle = (joy.throttle * 70) + 290
    Drive.drive()
    # def cam_callback(camera):


rospy.init_node('joystick_sub')
sub = rospy.Subscriber('joystick', JoyStick, joy_callback)
rospy.spin()