import cv2
import numpy as np
from matplotlib import pyplot as plt

def contour_match(frame):
	
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	filter_gray = cv2.bilateralFilter(gray, 11, 17, 17)
	edges = cv2.Canny(filter_gray, 100, 200)

	cv2.imshow('steps', np.hstack((gray,filter_gray,edges)))
	cv2.waitKey(0)

	cnts,_ = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	
	cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:2]	
	
	if len(cnts)>0:
		peri = cv2.arcLength(cnts[0], True)
		approx = cv2.approxPolyDP(cnts[0], 0.02 * peri, True)
  
		if len(approx) == 4:

			# candidate for marker    
			x , y , w, h = cv2.boundingRect(cnts[0])
			roi = frame[y: y + h, x: x + w] 
			resized_roi = cv2.resize(roi, (114, 114)) 
			return 1, resized_roi

		else:

			return 0,0 
	else:

		return 0,0


# main
camera_img = cv2.imread('./Test_Images/a.png')
rc, marker_detected = contour_match(camera_img)
print marker_detected
cv2.imshow('op', marker_detected)
cv2.waitKey(0)
 
