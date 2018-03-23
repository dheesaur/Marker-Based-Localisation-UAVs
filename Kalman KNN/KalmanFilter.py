#!/usr/bin/env ipython

print 'Importing Libraries'

import matplotlib.pyplot as plt 
import numpy as np 
import rospy
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist
from ardrone_autonomy.msg import Navdata
from math import sin,cos,degrees,radians

print 'Libraries imported'
plt.ion()

class KalmanFilter(object):
	"""Defining a Kalman filter class"""
	def __init__(self):
		self.x = np.asarray([0,0,0],dtype='float32') #x,y,phi
		self.P = np.diag([10,10,10])
		self.Q = np.diag([0.005,0.005,0.005])
		self.prev_rotZ = 0
		self.prev_time = 0
		self.first_run = 1

		self.f = open('output_data.txt','w')


	def prediction_update(self,navdata):
		
		if self.first_run==1 or navdata.state in [1,2,6,8] : #the node just started
			self.prev_time = navdata.tm/1000000.0
			self.prev_rotZ = navdata.rotZ
			self.first_run = 0 
		
		else:
			
			#extracting values
			rotZ = 0 #converting from 0 - 360 (anticlockwise)
			#if navdata.rotZ<0:
			#	rotZ = navdata.rotZ + 360
			#else:
			#	rotZ = navdata.rotZ
			rotZ = navdata.rotZ
			vx = navdata.vx/1000.0
			vy = navdata.vy/1000.0
			
			
			dt = (navdata.tm/1000000.0) - self.prev_time
			vphi = (rotZ - self.prev_rotZ)/dt
			self.prev_rotZ = rotZ
			self.prev_time = navdata.tm/1000000.0

			#kalman code

			#1. Update the state x
			new_x = np.asarray([self.x[0]  + dt*( cos(radians(self.x[2]))*vx  -  sin(radians(self.x[2]))*vy )  ,
								self.x[1]  + dt*( sin(radians(self.x[2]))*vx  +  cos(radians(self.x[2]))*vy )  ,
								self.x[2]  + dt*vphi])


			self.x = new_x
			self.f.write(str(self.x[0])+" "+str(self.x[1])+'\n')

			#2. Update the covariance matrix

			F = np.array([  [1 , 0, dt*(-sin(radians(self.x[2]))*vx - cos(radians(self.x[2]))*vy )] ,  
							[0 , 1, dt*(cos(radians(self.x[2]))*vx - sin(radians(self.x[2]))*vy )]  ,
							[0 , 0, 1]

						])
			new_P = np.dot(F,np.dot(self.P,F.T)) + self.Q
			self.P = new_P
	def close_file(self):
		self.f.close()


			
			





def main():

	kf = KalmanFilter()
	rospy.init_node('filter',anonymous=True)
	rospy.Subscriber('/ardrone/navdata',Navdata,kf.prediction_update)
	rospy.spin()
	if rospy.is_shutdown():
		kf.close_file()


if __name__ == '__main__':
	main()
