#!/usr/bin/env python

from __future__ import print_function
import cv2, rospy, cv_bridge, numpy
import argparse
from sensor_msgs.msg import Image


	# if not traffic_light_cascade.load(cv2.samples.findFile(traffic_light_cascade_name)):
    	# print('--(!)Error loading traffic light cascade')
    	# exit(0)

	# camera_device = args.camera
	# cap = cv2.VideoCapture(camera_device)


class Detect:

    def __init__(self):
	self.parser = argparse.ArgumentParser(description='Code for Cascade Classifier tutorial.')
	self.parser.add_argument('--traffic_light_cascade', help='Path to traffic light cascade.', default='/home/work/git/git/ros_rc_car_tx2/src/usb_camera/src/traffic_light.xml')
	#self.parser.add_argument('--camera', help='Camera divide number.', type=int, default=1)
	self.args = self.parser.parse_args()
	self.traffic_light_cascade_name = self.args.traffic_light_cascade
	self.traffic_light_cascade = cv2.CascadeClassifier()
	if not self.traffic_light_cascade.load(cv2.samples.findFile(self.traffic_light_cascade_name)):
    	    #print('--(!)Error loading traffic light cascade')
            exit(0)

	self.bridge = cv_bridge.CvBridge()
	# cv2.namedWindow("Window", 1)
	self.img_sub = rospy.Subscriber('/camera/rgb/image_raw', Image, self.image_callback)
	

    def image_callback(self, msg):
    	frame = self.bridge.imgmsg_to_cv2(msg)
        self.detectAndDisplay(frame)
	# cv2.imshow("window", img)
	# cv2.waitKey(3)

    def detectAndDisplay(self, frame):
	red_light = False
    	green_light = False
    	yellow_light = False

    	v=0
    	threshold = 150
    	# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    	gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    	traffic_light = self.traffic_light_cascade.detectMultiScale(gray, 1.1, 5)
    	for (x, y, w, h) in traffic_light:
            cv2.rectangle(frame, (x+5, y+5), (x+w-5, y+h-5), (255, 255, 255), 2)
            v = y + h -5

        # stop
        # if w / h == 1:
        #     cv2.putText(frame, 'STOP', (x, y -10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        # traffic light
        # else:
            if w / h != 1:
                roi = gray[y+10:y+h-10,x+10:x+w-10]
                mask = cv2.GaussianBlur(roi, (25,25), 0)
                (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(mask)

            # check if light is on
                if maxVal - minVal > threshold:
                    cv2.circle(roi, maxLoc, 5, (255,0,0), 2)

                # RED light
                    if 1.0/8 * (h-30) < maxLoc[1] < 4.0/8 * (h-30):
                        cv2.putText(frame, 'RED', (x + 5, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                        red_light = True

                # GREEN light
                    elif 5.5 / 8 * (h - 30) < maxLoc[1] < h - 30:
                        cv2.putText(frame, 'GREEN', (x + 5, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                        green_light = True

        cv2.imshow("window", frame)
	cv2.waitKey(1)



rospy.init_node('detect_sign')
det = Detect()
rospy.spin()
