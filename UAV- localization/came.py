#!/usr/bin/env python

import rospy
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image, CameraInfo
import time
pub_image = rospy.Publisher("/image", Image,queue_size=1)
pub_caminfo = rospy.Publisher("/camer_info", CameraInfo,queue_size=1)
def callback1(data):
	pub_image.publish(msg)
	#rospy.loginfo(rospy.get_caller_id() + "I hear your mom saying %s", data.data)

def callback2(data):
	pub_caminfo.publish(msg)
	#rospy.loginfo(rospy.get_caller_id() + "I hear your dad saying %s", data.data)

def came():
	rospy.init_node('came', anonymous = True)
	rospy.Subscriber("ardrone/bottom/image_raw",Image,callback1)
	rospy.Subscriber("/ardrone/camera_info",CameraInfo,callback2)
	rospy.spin()

if __name__ == '__main__':
	came()
