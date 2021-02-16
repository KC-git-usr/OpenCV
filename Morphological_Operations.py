#Morphological operations help in reducing noise

import numpy as np 
import cv2


def erosion(img):
	''' 
	Erodes away boundaries of foreground objects. 
	Works best when foreground is light color (preferrably white) and background is dark 
	'''
	kernel = np.ones((5,5), np.uint8)
	eroded_img = cv2.erode(img, kernel, iterations=3)
	return eroded_img


def add_white_noise(img):
	white_noise = np.random.randint(low=0, high=2, size=(600,600)) * 255
	noise_img = img + white_noise
	return noise_img


def add_black_noise(img):
	black_noise = np.random.randint(low=0, high=2, size=(600,600)) * -255
	noise_img = img + black_noise
	return noise_img


def opening(img):
	'''
	Opening is erosion followed by dilation. Useful in removing background noise
	'''
	kernel = np.ones((5,5), np.uint8)
	opening_img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
	return opening_img


def closing(img):
	'''
	Closing is ueful in removing noise from foreground objects, 
	such as black dots on top of the white text.
	'''
	kernel = np.ones((5,5), np.uint8)
	closing_img = cv2.morphologyEx(img, cv2.MORPH_CLOSE , kernel)
	return closing_img


def morphological_gradient(img):
	'''
	Difference between dilation and erosion of an image
	It's a types of edge detection
	'''
	kernel = np.ones((5,5), np.uint8)
	gradient_img = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
	return gradient_img


def main():
	img = np.zeros((600,600))
	font = cv2.FONT_HERSHEY_SIMPLEX
	cv2.putText(img, "ABCDE", (70,300), font, 5, (255,255,255), 25, cv2.LINE_AA)

	#i_img = add_black_noise(img)
	edited_img = morphological_gradient(img)

	while True:
		cv2.imshow("Original img", img)
		#cv2.imshow("Intermediate img", i_img)
		cv2.imshow("Edited img", edited_img)
		if cv2.waitKey(1) & 0xFF == 27:
			break
	cv2.destroyAllWindows()
	

if __name__ == '__main__':
	main()