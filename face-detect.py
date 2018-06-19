#!/usr/bin/env python
from __future__ import division
import sys, cv2, pylab
import numpy as np

def detect(im):
	cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
	faces = cascade.detectMultiScale(im, scaleFactor=1.1, minNeighbors=5)
	for(x,y,w,h) in faces:
		print" ", x,y,x+w,y+h
		reg = im[y:y+h,x:x+w]
		cv2.rectangle(im, (x,y),(x+w,y+h),(0,255,255),2)

	return im

for fn in sys.argv[1:]:
	# Takes image and outputs dimensions.
	im = cv2.imread(fn) #attempts to open a file with the same name from the command line argument
	ny, nx, nc = im.shape #sets the images pixel count to NX, the lines to NC, and the chanels to NC
	print fn + ":" 
	print "  Dimensions:", nx, "pixels,", ny, "lines,", nc, "channels." #prints out the images pixel count,line count, and chanels.



	
	newIm = detect(im)
	#aa = np.hstack((im, newIm)) #puts original image and masked image side by side
	cv2.imshow(fn, newIm)
	cv2.waitKey(0)
    	cv2.destroyWindow(fn)
	print

