#!/usr/bin/env python

import pygame
import rospy
from joystick.msg import JoyStick
from module import xbox360_controller

rospy.init_node('CarController_talker')
pub = rospy.Publisher('/joystick', JoyStick, queue_size=1)
rate = rospy.Rate(10.0)

pygame.init()
joy = xbox360_controller.Controller()

brk_status = False
rec_status = False

while not rospy.is_shutdown():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    msg = JoyStick(0.0, 0.0, brk_status, rec_status)
    # stick status
    lt_x, lt_y = joy.get_left_stick()
    rt_x, rt_y = joy.get_right_stick()
    # brake status
    if round(joy.get_triggers()) == -1.0:
        brk_status = True
    else:
        brk_status = False
    # recode status
    button = joy.get_buttons()
    if button[xbox360_controller.START] == 1:
        rec_status = True
    elif button[xbox360_controller.BACK] == 1:
        rec_status = False

    msg.steering = lt_x
    msg.throttle = rt_y
    msg.brk_status = brk_status
    msg.rec_status = rec_status

    print('lt_x: {}, lt_y: {}'.format(round(lt_x, 2), round(lt_y, 2)))
    print('brake: {},\trec: {}'.format(brk_status, rec_status))
    pub.publish(msg)
    rate.sleep()



