import cv2
import numpy as np 

img1 = cv2.imread("Computer-Vision-with-Python//DATA//rainbow.jpg", 0)
img2 = cv2.imread("Computer-Vision-with-Python//DATA//crossword.jpg", 0)


def threshold_func(img, option):
	'''
	function that returns an image after performing a thresholding transformation
	1 : THRESH_BINARY, 2 : THRESH_BINARY_INV, 3 : cv2.THRESH_TRUNC, 4 : THRESH_TOZERO, 5 : THRESH_TOZERO_INV
	https://docs.opencv.org/3.4/d7/d1b/group__imgproc__misc.html#ggaa9e58d2860d4afa658ef70a9b1115576a147222a96556ebc1d948b372bcd7ac59
	'''
	if option==1:
		ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
		return thresh1
	elif option==2:
		ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
		return thresh2
	elif option==3:
		ret, thresh3 = cv2.threshold(img, 150, 255, cv2.THRESH_TRUNC)
		return thresh3
	elif option==4:
		ret, thresh4 = cv2.threshold(img, 180, 255, cv2.THRESH_TOZERO)
		return thresh4
	elif option==5:
		ret, thresh5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)
		return thresh5

def adaptive_threshold(img):
	binary_img1 = threshold_func(img, 1)
	binary_img2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 13, 15)
	blended_img = cv2.addWeighted(binary_img1, 0.3, binary_img2, 0.7, gamma = 0)
	return blended_img

converted_img = adaptive_threshold(img2)

while True:
	cv2.imshow("Original Img", img2)
	cv2.imshow("Converted Img", converted_img)

	if cv2.waitKey(1) & 0xFF == 27:
		break

cv2.destroyAllWindows