#!/usr/bin/env python3

import rospy, message_filters
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
import sys, threading


class StereoCamera():
    def __init__(self):
        rospy.init_node("stereo_cam_node", anonymous=True)
        self.img_pub = rospy.Publisher("/stereo/image_raw", Image, queue_size=1)
        self.imgs = None
        self.img_left = None
        self.img_right = None
        self.cv_bridge = CvBridge()
        self.left_cam_sub = rospy.Subscriber("/left/image_raw", Image, self.camera_callback_l)
        self.right_cam_sub = rospy.Subscriber("/right/image_raw", Image, self.camera_callback_r)

    def camera_callback_l(self, left):
        img_left = self.cv_bridge.imgmsg_to_cv2(left)
        img_left = cv2.resize(img_left,(320, 240))
        self.img_left = cv2.cvtColor(img_left, cv2.COLOR_BGR2RGB).astype(np.uint8)

    def camera_callback_r(self, right):
        img_right = self.cv_bridge.imgmsg_to_cv2(right)
        img_right = cv2.resize(img_right,(320, 240))
        self.img_right = cv2.cvtColor(img_right, cv2.COLOR_BGR2RGB).astype(np.uint8)

    def pub(self):
        self.imgs = np.concatenate((self.img_left, self.img_right), axis=1)
        # cv2.imshow("concat_img", self.imgs)
        # cv2.waitKey(1)
        img = self.cv_bridge.cv2_to_imgmsg(self.imgs, encoding="bgr8")
        img.header.stamp = rospy.Time.now()
        self.img_pub.publish(img)
        rospy.sleep(0.034)


cam = StereoCamera()

while not rospy.is_shutdown():
    if cam.img_left is None:
        continue
    if cam.img_right is None:
        continue
    cam.pub()

