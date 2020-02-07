#!/usr/bin/env python

import rospy, message_filters
import cv2, csv, threading, os.path
import numpy as np

from cv_bridge import CvBridge, CvBridgeError
from joystick.msg import JoyStick
from sensor_msgs.msg import Image
from recoder.msg import RecodeBag


DEFAULT_LOCATION = "/home/n9646/bag/"
RGB_IMG_PATH = "/home/n9646/bag/imgs/"
DEPTH_IMG_PATH = "/home/n9646/bag/depth_imgs/"
DRIVING_LOG_PATH="/home/n9646/bag/driving_log.csv"


class Recoder:
    def __init__(self):
        self.steering = 0.0
        self.throttle = 0.0
        self.rgb_img = None
        self.depth_img = None
        self.seq = 0
        rospy.init_node("recorder_device", anonymous=True)
        self.record_pub = rospy.Publisher("/recorder_pub", RecodeBag, queue_size=1)
        self.joy_sub = rospy.Subscriber("joystick", JoyStick, self.joy_callback)

        # Open driving_log file
        if os.path.isfile(DRIVING_LOG_PATH) is True:
            f = open(DRIVING_LOG_PATH, 'ab')
            self.driving_log = csv.DictWriter(f, fieldnames=["RGB Image", "Depth Image", "Steering", "Throttle"])
        else:
            f = open(DRIVING_LOG_PATH, 'wb')
            self.driving_log = csv.DictWriter(f, fieldnames=["RGB Image", "Depth Image", "Steering", "Throttle"])
            self.driving_log.writeheader()
        # Lock camera image
        #self.lock = threading.RLock()
        self.cv_bridge = CvBridge()
        # message filters
        self.rgb_cam_sub = message_filters.Subscriber("/camera/rgb/image_raw", Image)
        print('1')
        self.depth_cam_sub = message_filters.Subscriber("/camera/depth/image_raw", Image)
        print('2')
        self.ts = message_filters.ApproximateTimeSynchronizer([self.rgb_cam_sub, self.depth_cam_sub], 10, 0.5)
        print('3')
        self.ts.registerCallback(self.camera_callback)
        print('4')

    def camera_callback(self, img, depth_img):
        self.rgb_img = self.cv_bridge.imgmsg_to_cv2(img)
        print('rgb image')
        self.depth_img = self.cv_bridge.imgmsg_to_cv2(depth_img, "passthrough")
        print('depth image')

    # -1~0~1
    def joy_callback(self, msg):
        self.steering = msg.steering
        self.throttle = msg.throttle

    def recoding(self):
        timestamp = rospy.get_rostime()
        # save_rgb_img
        rgb_fname = RGB_IMG_PATH+str(timestamp)\
                +"_"+str(self.seq)+"_"+str(self.steering)+"_"+str(self.throttle)+".jpg"
        print(rgb_fname)
        depth_fname = DEPTH_IMG_PATH+str(timestamp)\
                      +"_"+str(self.seq)+"_"+str(self.steering)+"_"+str(self.throttle)+".jpg"
        print(depth_fname)
        cv2.imwrite(rgb_fname, self.rgb_img)
        cv2.imwrite(depth_fname, self.depth_img)
        # new csv line
        self.driving_log.writerow({'RGB Image': rgb_fname, 'Depth Image': depth_fname,
                                   'Steering': self.steering, 'Throttle': self.throttle})
        # publish data to /recorder_pub
        msg = RecodeBag(self.steering, self.throttle, rgb_fname, depth_fname)
        msg.steering = self.steering
        msg.throttle = self.throttle
        msg.img_path = rgb_fname
        msg.depth_path = depth_fname
        self.record_pub.publish(msg)
        self.seq += 1
        # Set rate at 30 Hz
        rospy.sleep(0.034)
        print("recoding stop: X button")


recode = Recoder()

while not rospy.is_shutdown():
    if recode.depth_img is None:
        # print('frame is none')
        continue
    recode.recoding()