#!/usr/bin/env ipython

#to control the drone using xbox controller

import rospy
import time 
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

#declare a global publisher
#declare the publishers and subscribers
pub_takeoff = rospy.Publisher('/ardrone/takeoff',Empty,queue_size=1)
pub_land    = rospy.Publisher('/ardrone/land',Empty,queue_size=1)
pub_cmdvel  = rospy.Publisher('/cmd_vel',Twist,queue_size = 1)

state = 0 #0-landed , 1-flying
def callback(data):

	global state 
	if data.buttons[0] == 1 or data.buttons[1]==1:

		if data.buttons[0] == 1:
			msg = Empty()
			pub_takeoff.publish(msg)
			state = 1
			rospy.loginfo('taking off')
		elif data.buttons[1]== 1:
			msg = Empty()
			pub_land.publish(msg)
			state = 0
			rospy.loginfo('landing')
	
	else:

		msg = Twist()
		msg.linear.y = data.axes[0] if abs(data.axes[0])>0.1 else 0
		msg.linear.x = data.axes[1] if abs(data.axes[1])>0.1 else 0
		msg.angular.z = data.axes[3] if abs(data.axes[3])>0.1 else 0

		if int(data.axes[2]) == -1:
			msg.linear.z = 0.2
		elif int(data.axes[5])==-1:
			msg.linear.z = -0.2

		pub_cmdvel.publish(msg)




def main():

	rospy.init_node('xcontrol',anonymous=True)
	rospy.Subscriber('joy',Joy,callback)
	rospy.spin()



if __name__ == '__main__':
	main()