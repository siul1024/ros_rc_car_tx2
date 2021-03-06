#!/usr/bin/env python

import rospy
from controller.msg import Controller
from module.drive import Drive


car = Drive()


# Controller callback function
def car_drive(joy):
    car.steering = int((joy.steering * 110) + 360)
    car.throttle = int((joy.throttle * 40) + 290)
    if joy.brk_status:
        car.car_brake()
    else:
        car.drive()
    if joy.rec_status:
        car.rec_status = True
    else:
        car.rec_status = False


rospy.init_node('CarController_listener')
sub = rospy.Subscriber('/controller', Controller, car_drive)
rospy.spin()
car.pin_clean()
