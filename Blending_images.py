import cv2
import numpy as np

puppy_img = cv2.imread("Computer-Vision-with-Python//DATA//dog_backpack.jpg", cv2.COLOR_BGR2RGB)
copyright_img = cv2.imread("Computer-Vision-with-Python//DATA//watermark_no_copy.png", cv2.COLOR_BGR2RGB)

print("Puppy image size = ",puppy_img.shape)
print("Copyright image size = ",copyright_img.shape)


def same_size_img_blend(img1, img2):
	'''
	this functions blends two images which are of the same size and returns blended img
	'''
	reshaped_img1 = cv2.resize(img1, (934, 1280))
	reshaped_img2 = cv2.resize(img2, (934, 1280))
	return cv2.addWeighted(reshaped_img1, 0.9, reshaped_img2, 0.1, 0)

def diff_size_img_overlay(img1, img2):
	'''
	this func replaces a certain portion of larger img with entire of smaller img
	img1 is bigger, img2 is smaller
	'''
	reshaped_img2 = cv2.resize(img2, (934, 340))
	y_start, x_start = 0, 0
	y_end, x_end = reshaped_img2.shape[0], reshaped_img2.shape[1]
	print(y_end, x_end)
	merged_img = img1.copy()
	merged_img[y_start:y_end, x_start:x_end] = reshaped_img2
	merged_img = cv2.resize(merged_img, (0,0), merged_img, 0.5, 0.5)
	return merged_img

def diff_size_img_blend(img1, img2):
	'''
	this function adds a watermark at desired location
	'''
	reshaped_img1 = cv2.resize(img1, (0, 0), img1, 0.5, 0.5)
	reshaped_img2 = cv2.resize(img2, (300, 300))
	roi = reshaped_img1[ reshaped_img1.shape[0]-300:reshaped_img1.shape[0] ,  reshaped_img1.shape[1]-300:reshaped_img1.shape[1]]
	mask = cv2.cvtColor(reshaped_img2, cv2.COLOR_RGB2GRAY)
	inv_mask = cv2.bitwise_not(mask)
	#white_bg = np.full(reshaped_img2.shape, 255, np.uint8)
	#final_mask = cv2.bitwise_or(white_bg, white_bg, mask=inv_mask)
	fg = cv2.bitwise_or(reshaped_img2, reshaped_img2, mask=inv_mask)
	final_roi = cv2.bitwise_or(roi, fg)
	reshaped_img1[reshaped_img1.shape[0]-300:reshaped_img1.shape[0] ,  reshaped_img1.shape[1]-300:reshaped_img1.shape[1]] = final_roi
	return reshaped_img1

blended_img = diff_size_img_blend(puppy_img, copyright_img)

while True:
	#cv2.imshow("My Doggo", reshaped_puppy_img)
	#cv2.imshow("My Img", reshaped_copyright_img)
	cv2.imshow("Blended Img", blended_img)

	if cv2.waitKey(1) & 0xFF == 27:
		break

cv2.destroyAllWindows()



'''
create ROI
create mask
	convert img to grey
	invert grey img -> this is mask but has only 1 channel
	
'''