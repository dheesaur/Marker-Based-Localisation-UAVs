# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 12:10:10 2016

@author: dheer
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

def contour_match(frame):
	
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.bilateralFilter(gray, 11, 17, 17)
	edges = cv2.Canny(gray, 100, 200)
	_,cnts,_ = cv2.findContours(edges.copy(), cv2.RETR_TREE, 	 cv2.CHAIN_APPROX_SIMPLE)
	cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:2]
	cnt=cnts[0]
	screenCnt = None
    
	for c in cnts:
	    M = cv2.moments(c)
	    cX = int(M["m10"] / M["m00"])
	    cY = int(M["m01"] / M["m0	    peri = cv2.arcLength(c, True)
	    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    
        
       
        
          
          
	    if len(approx) == 4:
	        screenCnt = approx
	        break
	x , y , w, h = cv2.boundingRect(cnts[0])
             
	roi = frame[y: y + h, x: x + w] 
	resized_roi = cv2.resize(roi, (114, 114)) 
	return resized_roi




 
