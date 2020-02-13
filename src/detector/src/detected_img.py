#!/usr/bin/python

import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge, CvBridgeError

import jetson.inference
import jetson.utils
import numpy as np

import argparse
import sys


# parse the command line
parser = argparse.ArgumentParser(description="Locate objects in a live camera stream using an object detection DNN.", 
						   formatter_class=argparse.RawTextHelpFormatter, epilog=jetson.inference.detectNet.Usage())

parser.add_argument("--network", type=str, default="ssd-mobilenet-v2", help="pre-trained model to load (see below for options)")
parser.add_argument("--overlay", type=str, default="box,labels,conf", help="detection overlay flags (e.g. --overlay=box,labels,conf)\nvalid combinations are:  'box', 'labels', 'conf', 'none'")
parser.add_argument("--threshold", type=float, default=0.5, help="minimum detection threshold to use") 
parser.add_argument("--camera", type=str, default="1", help="index of the MIPI CSI camera to use (e.g. CSI camera 0)\nor for VL42 cameras, the /dev/video device to use.\nby default, MIPI CSI camera 0 will be used.")
parser.add_argument("--width", type=int, default=640, help="desired width of camera stream (default is 1280 pixels)")
parser.add_argument("--height", type=int, default=480, help="desired height of camera stream (default is 720 pixels)")
opt = parser.parse_known_args()[0]


class Detector():
    def __init__(self):
        rospy.init_node("video_detect_node", anonymous=True)
        self.img_pub = rospy.Publisher("/video/image", Image, queue_size=1)
        self.img_sub = rospy.Subscriber("/image_raw", Image, self.camera_callback)
        # self.net = jetson.inference.detectNet(opt.network, sys.argv, opt.threshold)
        self.net = jetson.inference.detectNet(opt.network, sys.argv, opt.threshold)
        self.cv_bridge = CvBridge()
        rospy.sleep(0.5)

    def camera_callback(self, msg):
        self.img = self.cv_bridge.imgmsg_to_cv2(msg) # , desired_encoding="bgr8")
     
    def detecting(self):
        img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGBA).astype(np.uint8)
        #cv2.imshow("--", img)
        #cv2.waitKey(1)
        img = jetson.utils.cudaFromNumpy(img)
        detections = self.net.Detect(img, opt.width, opt.height)
        print("detected {:d} objects in image".format(len(detections)))
        for detection in detections:
            print(detection)
        img = jetson.utils.cudaToNumpy(img, opt.width, opt.height, 4) #array, width, hight, depth
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB).astype(np.uint8)
        #cv2.imshow("--", img)
        #cv2.waitKey(1)
        img = self.cv_bridge.cv2_to_imgmsg(img, encoding="bgr8")
        img.header.stamp = rospy.Time.now()
        self.img_pub.publish(img)
         # Set rate at 30 Hz
        rospy.sleep(0.030)


dtc = Detector()

while not rospy.is_shutdown():
    if dtc.img is None:
        continue
    dtc.detecting()

