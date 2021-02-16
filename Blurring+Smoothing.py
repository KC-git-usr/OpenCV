import cv2
import numpy as np

#2D convolution aka image filtering

def gamma_correction(img, gamma='2'):
	'''returns image after changing gamma value'''
	i_img = img.copy()
	i_img = np.power(i_img, gamma)
	return i_img

def put_text(img, text='bricks'):
	'''returns image after adding text on it'''
	i_img = img.copy()
	font = cv2.FONT_HERSHEY_COMPLEX
	cv2.putText(i_img, text, (10, 260), font, 5, (0,0,255), 2)
	return i_img

def blur(img, option=2):
	'''
	1 : implementing custom made kernel blur effect on image
	2 : in-built blur
	3 : Gaussian blur
	4 : Median blur (best option to remove noise and blur)
	5 : Bi-lateral filter (removes surface texture, but preserves egdes)
	'''
	if option==1:
		kernel = np.ones((5,5), np.float32)/25
		i_img = cv2.filter2D(img, -1, kernel)
		return i_img
	elif option==2:
		i_img = cv2.blur(img, (5,5))
		return i_img
	elif option==3:
		i_img = cv2.GaussianBlur(img, (5,5), 10)
		return i_img
	elif option==4: #best option
		i_img = cv2.medianBlur(img, 5)
		return i_img
	elif option==5:
		i_img = cv2.bilateralFilter(img, 9, 75, 75)
		return i_img

def main():

	img = cv2.imread("Computer-Vision-with-Python//DATA//bricks.jpg").astype(np.float32) / 255
	img = cv2.resize(img, (0,0), img, 0.5, 0.5)

	edited_img = put_text(img)
	edited_img = blur(edited_img, 4)

	while True:
		cv2.imshow("Original Img", img)
		cv2.imshow("Edited Img", edited_img)

		if cv2.waitKey(1) & 0xFF == 27:
			break

	cv2.destroyAllWindows()

if __name__ == '__main__':
	main()