#!/usr/bin/env python3

import rospy  # , message_filters
import cv2, csv, os.path
import numpy as np

from cv_bridge import CvBridge, CvBridgeError
from controller.msg import Controller
from sensor_msgs.msg import Image
from recoder.msg import RecodeBag

import sys


DEFAULT_LOCATION = "/home/work/git/bag/"
RGB_IMG_PATH = "/home/work/git/bag/imgs/"
DEPTH_IMG_PATH = "/home/work/git/bag/depth_imgs/"
DRIVING_LOG_PATH="/home/work/git/bag/driving_log.csv"


class Recoder:
    def __init__(self):
        self.steering = 0.0
        self.throttle = 0.0
        self.rec_status = False
        self.rgb_img = None
        # self.depth_img = None
        self.seq = 0
        # ros init node
        rospy.init_node("recorder_node", anonymous=True)
        self.record_pub = rospy.Publisher("/recorder_pub", RecodeBag, queue_size=1)
        self.joy_sub = rospy.Subscriber("/controller", Controller, self.joy_callback)

        # Open driving_log file
        if os.path.isfile(DRIVING_LOG_PATH) is True:
            f = open(DRIVING_LOG_PATH, 'a', newline="")
            self.driving_log = csv.DictWriter(f, fieldnames=["RGB Image", "Depth Image", "Steering", "Throttle"])
        else:
            f = open(DRIVING_LOG_PATH, 'w', newline="")
            self.driving_log = csv.DictWriter(f, fieldnames=["RGB Image", "Depth Image", "Steering", "Throttle"])
            self.driving_log.writeheader()
        # Lock camera image
        #self.lock = threading.RLock()
        self.cv_bridge = CvBridge()
        # message filters
        self.rgb_cam_sub = rospy.Subscriber("/video/image", Image, self.camera_callback)
        # self.rgb_cam_sub = message_filters.Subscriber("/camera/rgb/image_raw", Image)
        # self.depth_cam_sub = message_filters.Subscriber("/camera/depth/image_raw", Image)
        # self.ts = message_filters.ApproximateTimeSynchronizer([self.rgb_cam_sub, self.depth_cam_sub], 10, 0.5)
        # self.ts.registerCallback(self.camera_callback)

    def camera_callback(self, img):
        self.rgb_img = self.cv_bridge.imgmsg_to_cv2(img, desired_encoding="bgr8")
        # self.depth_img = self.cv_bridge.imgmsg_to_cv2(depth_img) # , encoding="passthrough")

    # -1~0~1
    def joy_callback(self, msg):
        self.steering = msg.steering
        self.throttle = msg.throttle
        self.rec_status = msg.rec_status

    def recoding(self):
        if self.rec_status == False:
            return
        rgb_img = self.rgb_img
        steering = self.steering
        throttle = self.throttle
        timestamp = rospy.get_rostime()
        # save image file
        rgb_fname = RGB_IMG_PATH+str(timestamp)\
                    +"_"+str(self.seq)+"_"+str(steering)+"_"+str(throttle)+".jpg"
        # depth_fname = DEPTH_IMG_PATH+str(timestamp)\
        #               +"_"+str(self.seq)+"_"+str(self.steering)+"_"+str(self.throttle)+".jpg"
        depth_fname = "unused"
        
        cv2.imwrite(rgb_fname, rgb_img)
        # cv2.imwrite(depth_fname, self.depth_img)
        # new csv line
        self.driving_log.writerow({'RGB Image': rgb_fname, 'Depth Image': depth_fname,
                                   'Steering': steering, 'Throttle': throttle})
        # publish data to /recorder_pub
        msg = RecodeBag(steering, throttle, rgb_fname, depth_fname)
        msg.steering = steering
        msg.throttle = throttle
        msg.img_path = rgb_fname
        # msg.depth_path = depth_fname
        self.record_pub.publish(msg)
        self.seq += 1
        # Set rate at 30 Hz
        rospy.sleep(0.034)
        print("recoding stop: 'BACK' button")

	
recode = Recoder()

while not rospy.is_shutdown():
    if recode.rgb_img is None:
        continue
    recode.recoding()
