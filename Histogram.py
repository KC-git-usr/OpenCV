'''We are trying to plot color intensity(x-axis) vs freq. or no. of occurences(y-axis)'''

import numpy as np 
import cv2
import matplotlib.pyplot as plt 


def display_img(img, text):
	while True:
		cv2.imshow(text, img)
		if cv2.waitKey(1) & 0xFF==27:
			break
	cv2.destroyAllWindows()


def equalize_color_histogram(img):
	'''
	Function equalizes histogram of color images:
		1. cvt BGR to HSV
		2. equalize 'V' of HSV
		3. cvt back to BGR
	'''
	eq_hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  
	eq_hsv_img[:,:,2] = cv2.equalizeHist(src=eq_hsv_img[:,:,2])
	eq_img = cv2.cvtColor(eq_hsv_img, cv2.COLOR_HSV2BGR)
	display_img(eq_img, "Equalized image")
	get_histogram(eq_img)


def equalize_gray_histogram(img):
	eq_gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	display_img(eq_gray_img, "Original gray img")
	eq_gray_img = cv2.equalizeHist(eq_gray_img)
	hist_values = cv2.calcHist([eq_gray_img], channels=[0], mask=None, histSize=[256], ranges=[0,256])
	display_img(eq_gray_img, "Equalized gray img")
	plt.plot(hist_values)
	plt.show()


def get_histogram(img, mask_choice='n'):

	if mask_choice.lower() == 'y':
		mask = np.zeros(img.shape[:2], np.uint8)
		mask[300:400, 100:400] = 255
	else:
		mask = None

	colors = ('b','g','r')

	for i, color in enumerate(colors):
		hist_values = cv2.calcHist([img], channels=[i], mask=mask, histSize=[256], ranges=[0,256])
		print (hist_values.shape)
		plt.plot(hist_values, color)
		plt.xlim([0,256]) #change limit as per requirement
		#plt.ylim([0,300000])

	plt.title("Image histogram")
	plt.show()


def main():
	img = cv2.imread("Computer-Vision-with-Python//DATA//gorilla.jpg")
	img = cv2.resize(img, (0,0), img, 0.5, 0.5) #resizing to smaller img makes you loose data
	
	display_img(img, "Original image")

	#get_histogram(img, mask_choice= 'Y')
	#equalize_color_histogram(img)
	equalize_gray_histogram(img)
	

if __name__ == '__main__':
	main()