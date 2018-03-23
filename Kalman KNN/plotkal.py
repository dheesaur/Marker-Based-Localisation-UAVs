import numpy
import rospy
from std_msgs.msg import Float32MultiArray
from matplotlib import pyplot as plt

hl, = plt.plot([], [])

def callback(data):
	rospy.loginfo(rospy.get_caller_id(), data.data)

def update_line(hl, new_data):
    hl.set_xdata(numpy.append(hl.get_xdata(), new_data[0]))
    hl.set_ydata(numpy.append(hl.get_ydata(), new_data[1]))
    plt.draw()

def pkal():
	rospy.init_node('kalplot', anonymous=True)
	rospy.Subscriber("",Float32MultiArray, callback)
	update_line(hl, data)
	rospy.spin()

if __name__ == '__main__':
	pkal()