import numpy
import scipy
import rospy 
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist
import time

def PID(object):
	def __init__(self, P = 0.0, D = 1.0, I = 0.0, Proportional=0.0, Derivative = 0.0, Integrate=0.0, Imax=500, Imin=-500):
		self._Kp=P
		self._Ki=I
		self._Kd=D
		self._Proportional = Proportional
		self._Derivative = Derivative
		self._Integrate = Integrate
		self.Imax=Imax
		self.Imin=Imin

		self._setPoint = 0.0
		self.prevError = 0.0
		self.prevError = 0.0
		self.currTime = 0.0
		self.prevTime = 0.0

	
	@property
	def setPoint(self):
		return self._setpoint

	@SetPoint.setter
	def setPoint(self, set_point):
		self._setPoint = set_point

	def Compute(self, curr_value):
		self.curTime = time.time()
		dt = self.curTime - self.prevTime
		error = self._setpoint - curr_value
		de = error - self.prevError
		self._Proportional = self._Kp*error
		self_Derivative=self._Kd*(de/dt)

		if self.Integrator > self.Integrator_max:
			self.Integrator = self.Integrator_max
		elif self.Integrator < self.Integrator_min:
			self.Integrator = self.Integrator_min

		self._Integrate = prevError + self._Ki*error
		PID = self._Proportional+self._Derivative+self._Integrate
		return (PID)
		PIDdif = PID/dt
		return (PIDdif) 
		prevError = error
		self.prevTime = self.curTime;
