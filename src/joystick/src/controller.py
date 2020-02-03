#!/usr/bin/env python

import pygame
import rospy
from joystick.msg import JoyStick
from module.xbox360_controller import Controller

rospy.init_node('CarController_publisher')
pub = rospy.Publisher('joystick', JoyStick)
rate = rospy.Rate(10.0)

pygame.init()
joy = Controller()

while not rospy.is_shutdown():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    msg = JoyStick(0.0, 0.0)
    lt_x, lt_y = joy.get_left_stick()
    msg.steering = lt_x
    msg.throttle = lt_y
    # print('lt_x: {}, lt_y: {}'.format(round(lt_x, 2), round(lt_y, 2)))
    pub.publish(msg)
    rate.sleep()



