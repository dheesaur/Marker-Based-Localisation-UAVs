import numpy as np 
import time 
from Quadcopter import Quadcopter


q = Quadcopter()



for i in range(1000):

	# prints the position, the same can be confirmed from inside VREP
	print q.get_position()

	time.sleep(0.1)




