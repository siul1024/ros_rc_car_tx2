#!/usr/bin/env python
'''
This script activate pilot mode to take control over Jetson Car.

Use X button on joystick to stop 
'''

# Keras Model
import keras
import tensorflow as tf
from keras.models import model_from_json
from keras import backend as K

# Utils
import numpy as np
import cv2
import threading
import time

# ROS libraries
import roslib
import rospy
from cv_bridge import CvBridge, CvBridgeError

# ROS message
from sensor_msgs.msg import Image
from controller.msg import Controller


steering = 0.0
throttle = 0.0
cv_bridge = CvBridge()

print("Building Pilot Model...")


class Pilot:
    def __init__(self, get_model_call_back, model_callback):
        self.image = None
        self.model = None
        self.get_model = get_model_call_back
        self.predict = model_callback
        self.completed_cycle = False
        self.start = 0.
        self.lock = threading.RLock()
        rospy.init_node("pilot_model", anonymous=True)
        # self.joy = rospy.Subscriber('joy', Joy, self.joy_callback)
        self.control_signal = rospy.Publisher('/controller', Controller, queue_size=1)
        self.camera = rospy.Subscriber('/video/image', Image, self.callback, queue_size=1)
        rospy.Timer(rospy.Duration(0.005), self.send_control)

    def callback(self, camera):
        global steering, throttle
        if self.lock.acquire(True):
            self.image = cv_bridge.imgmsg_to_cv2(camera)
	    self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            if self.model is None:
                self.model = self.get_model()
            steering, throttle = self.predict(self.model, self.image)
            self.completed_cycle = True
            self.lock.release()

    def send_control(self, event):
        global steering, throttle
        if self.image is None:
            return
        if self.completed_cycle is False:
            return
        # Publish a rc_car_msgs
        msg = Controller()
#        msg.header.stamp = rospy.Time.now()
        msg.steering = steering
        msg.throttle = throttle
        self.control_signal.publish(msg)
        print("Steering: {:5.4f} Throttle {:5.4f}".format(steering, throttle))
        self.completed_cycle = False


