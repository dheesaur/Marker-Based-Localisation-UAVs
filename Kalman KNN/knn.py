import numpy as np 
import cv2 


def knn(test, train_images):
	'compare test against train_images'

	test_ravel = np.ravel(test)
	train_ravel = [np.ravel(img) for img in train_images]

	min_metric = np.norm(test_ravel-train_ravel[0])
	min_idx    = 0

	for i,img in enumerate(train_ravel):

		metric = np.norm(test_ravel-img)
		if metric<min_metric:
			min_metric = metric
			min_idx    = i 

	return min_idx, min_metric



