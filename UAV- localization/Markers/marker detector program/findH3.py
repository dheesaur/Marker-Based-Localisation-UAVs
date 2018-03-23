# finding the homography between 2 sets of 4 homogeneous points 

import matplotlib.pyplot as plt 
import numpy as np 
import matplotlib.image as mpimage 
import cv2 
import time

def findH(ipPoints,opPoints):
	'Computer the H matrix (3x3) between 2 sets of matched homogeneous co-ordinates'

	# computing the A matrix to calculate Ah = 0
	A = []
	for x1,x2 in zip(ipPoints,opPoints):

		a_x = [-x1[0], -x1[1], -1, 0, 0, 0, x2[0]*x1[0], x2[0]*x1[1], x2[0] ]
		a_y = [ 0,0,0, -x1[0], -x1[1], -1, x2[1]*x1[0], x2[1]*x1[1], x2[1]  ]
		A.append(a_x)
		A.append(a_y)
	
	A = np.array(A)
	
	# finding SVD of A 
	u,s,v = np.linalg.svd(A)
	#taking the column corresponding to the smallest singular value
	h = v[8]
	#rearranging in 3x3 format 
	H = np.array([  [h[0],h[1],h[2]], [h[3],h[4],h[5]], [h[6],h[7],h[8]]  ]) 
	return H

def cameraPoseFromHomography(H):
	'Estimate the camera pose from the homography'
	H1 = H[:,0]
	H2 = H[:,1]
	H3 = np.cross(H1, H2)

	norm1 = np.linalg.norm(H1)
	norm2 = np.linalg.norm(H2)
	tnorm = (norm1 + norm2)/2.0

	T     = H[:,2]/tnorm
	return np.mat([H1, H2, H3, T])

def main():

	imgInput = cv2.imread('testImg2.jpg',cv2.IMREAD_GRAYSCALE)
	ipPoints = [[203, 178], [390, 184], [210, 298], [423, 306]]
	opPoints = [  [0,0],[100,0],[0,100],[100,100]  ]

	#for pt in ipPoints:
	#	cv2.circle(imgInput, tuple(pt), 2, color=(255,0,0))
 
	#cv2.imshow('input', imgInput)
	#cv2.waitKey(0)
	H = findH(ipPoints, opPoints)
	print cameraPoseFromHomography(H)
	
	#print imgInput.shape
	#print 'printing tuple of values'
	imgOutput = np.zeros((100,100))
	xmax = max([pt[0] for pt in ipPoints])
	xmin = min([pt[0] for pt in ipPoints])
	ymax = max([pt[1] for pt in ipPoints])
	ymin = min([pt[1] for pt in ipPoints])

	it = np.nditer(imgInput,flags = ['multi_index'])
	while not it.finished:
		pt = it.multi_index
		if pt[0]>=ymin and pt[0]<=ymax and pt[1]>=xmin and pt[1]<=xmax: 
			pt1 = np.array([pt[1],pt[0],1])
			pt2_homo =  np.dot(H,np.transpose(pt1))
			pt2 = pt2_homo/pt2_homo[2]
			pt2 = np.asarray(pt2[0:2],dtype='int32')
			if pt2[0]>0 and pt2[0]<100 and pt2[1]>0 and pt2[1]<100:
				imgOutput[pt2[1],pt2[0]] = imgInput[pt[0],pt[1]]


		it.iternext()
	
	cv2.imwrite('outputFile3.png', imgOutput)

if __name__ == '__main__':
	main()