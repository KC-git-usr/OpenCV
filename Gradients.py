'''
Gradients == vector arrows pointing from lighter to darker region
Sobel_Feldman operators (aka Sobel) : rate of change of color intensity
	Helps in edge detection
	Sobel operator in the x-direction looks like you're shining a torch from the RHS of img
	Similarly, Sobel operator in y-direction is like shining a torch from the bottom of the img

https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_gradients/py_gradients.html
'''

import cv2
import numpy as np 


def get_sobel(img, x, y):
	sobel = cv2.Sobel(src=img, ddepth=cv2.CV_16S, dx=x, dy=y, ksize=7) #careful with ddepth here, I haven't understood it 
	return sobel


def get_laplace(img):
	laplace_img = cv2.Laplacian(src=img, ddepth=cv2.CV_64F)
	return laplace_img


def blend(img1, img2):
	b_img = cv2.addWeighted(src1=img1, alpha=0.5, src2=img2, beta=0.5, gamma=0)
	return b_img


def get_gradient(img):
	kernel = np.ones((3,3), np.int16)
	t_img = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
	return t_img


def threshold(img):
	ret, t_img = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
	return t_img


def main():
	img = cv2.imread("Computer-Vision-with-Python//DATA//sudoku.jpg", 0)
	img = cv2.resize(img, (0,0), img, 0.5, 0.5)

	print(type(img))

	sobelx_img = get_sobel(img,0,1)
	sobely_img = get_sobel(img,1,0)
	sobel_img = blend(sobelx_img, sobely_img)

	laplace_img = get_laplace(img)

	gradient_img = get_gradient(sobel_img)
	gradient_img_o = get_gradient(img)

	threshold_img = threshold(img)

	while True:
		#cv2.imshow("Original img", img)
		cv2.imshow("Sobel img", sobel_img)
		cv2.imshow("Laplace img", laplace_img)
		cv2.imshow("Gradient on Sobel img", gradient_img)
		#cv2.imshow("Gradient on Original img", gradient_img_o)
		cv2.imshow("Threshold on Original", threshold_img)
		if cv2.waitKey(1) & 0xFF == 27:
			break
	cv2.destroyAllWindows()


if __name__ == '__main__':
	main()