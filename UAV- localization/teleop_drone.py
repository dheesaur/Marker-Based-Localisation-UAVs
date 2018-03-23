#!/usr/bin/env python

import rospy 
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist
from getch import getch, pause
import time

def main():
	'MAIN FUNCTION'

	#declare the publishers and subscribers
	pub_takeoff = rospy.Publisher('/ardrone/takeoff',Empty,queue_size=1)
	pub_land    = rospy.Publisher('/ardrone/land',Empty,queue_size=1)
	pub_cmdvel  = rospy.Publisher('/cmd_vel',Twist,queue_size = 1)


	#initiate the node
	rospy.init_node('teleop_drone',anonymous = True)

	while not rospy.is_shutdown():


		ip = getch()
		if ip == 't' or ip == 'T':
			msg = Empty()
			pub_takeoff.publish(msg)
		elif ip == 'l' or ip == 'L':
			msg = Empty()
			pub_land.publish(msg)
		elif ip == 'w':
			msg = Twist()
			msg.linear.x = 0.8
			pub_cmdvel.publish(msg)
		elif ip == 's':
			msg = Twist()
			msg.linear.x = -0.8
			pub_cmdvel.publish(msg)
		elif ip == 'a':
			msg = Twist()
			msg.linear.y = 0.8
			pub_cmdvel.publish(msg)
		elif ip == 'd':
			msg = Twist()
			msg.linear.y = -0.8
			pub_cmdvel.publish(msg)
		elif  ip == 'e':
			msg = Twist()
			msg.angular.z = -0.8
			pub_cmdvel.publish(msg)
		elif  ip == 'q':
			msg = Twist()
			msg.angular.z = 0.8
			pub_cmdvel.publish(msg)


		else:
			print 'Not a valid Input!'
			msg = Twist()
			msg.linear.x = 0
			msg.linear.y = 0
			msg.linear.z = 0
			msg.angular.x = 0
			msg.angular.y = 0
			msg.angular.z = 0
			pub_cmdvel.publish(msg)
		#time.sleep(1)


	print 'Shutdown...'




if __name__ == '__main__':
	main()