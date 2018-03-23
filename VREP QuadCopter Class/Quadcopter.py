import vrep
import numpy as np
import cv2 
import time 

class Quadcopter():
	"""Get data from and to V-REP"""
	def __init__(self):

		vrep.simxFinish(-1)
		self.clientID = vrep.simxStart('127.0.0.1', 19997, True, True, 5000, 5)

		# start simulation
		rc = vrep.simxStartSimulation(self.clientID, vrep.simx_opmode_oneshot_wait)
		
		# object handles
		res, self.quad_obj = vrep.simxGetObjectHandle(self.clientID, 'Quadricopter', vrep.simx_opmode_oneshot_wait)
		res, self.camera   = vrep.simxGetObjectHandle(self.clientID, 'Vision_sensor', vrep.simx_opmode_oneshot_wait)
		
		# Initialise data streaming from V-REP
		err, resolution, image  = vrep.simxGetVisionSensorImage(self.clientID, self.camera, 0, vrep.simx_opmode_streaming)
		_,pos                   = vrep.simxGetObjectPosition(self.clientID, self.quad_obj, -1, vrep.simx_opmode_streaming)
		time.sleep(2)

		# Variables
		_,self.last_pos = vrep.simxGetObjectPosition(self.clientID, self.quad_obj, -1, vrep.simx_opmode_buffer)
		
	def get_position(self):
		'Get the quadcopters position'
		_, pos = vrep.simxGetObjectPosition(self.clientID, self.quad_obj, -1, vrep.simx_opmode_buffer)
		return pos 

	def get_odometry(self):
		'Get the del_x and del_y between current and previous position'
		cur_pos = self.get_position()
		odometry = [cur_pos[0]-self.last_pos[0], cur_pos[1]-self.last_pos[1]]
		#update last position
		self.last_pos = cur_pos
		return odometry

	def get_camera_image(self):
		'Get the image from the camera'

		err, resolution, image = vrep.simxGetVisionSensorImage(self.clientID, self.camera, 0, vrep.simx_opmode_buffer)
		img = np.array(image,dtype=np.uint8)
		img.resize([resolution[1],resolution[0],3])
		img = np.fliplr(img)
		temp = np.copy(img[:,:,0])
		img[:,:,0] = np.copy(img[:,:,2])
		img[:,:,2] = temp 
		return img 

