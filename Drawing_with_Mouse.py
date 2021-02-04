import cv2
import numpy as np

def drawCircle(event, x, y, flags, param):
	if event == cv2.EVENT_LBUTTONDOWN:
		cv2.circle(img, (x,y), 100, (0,255,255),-1)
	elif event == cv2.EVENT_RBUTTONDOWN:
		cv2.circle(img, (x,y), 100, (255,255,0),-1)

img = np.zeros((512,512,3))

cv2.namedWindow("My canvas")
cv2.setMouseCallback("My canvas", drawCircle)

while True:
	cv2.imshow("My canvas", img)

	if cv2.waitKey(1) & 0xFF == 27:
		break

cv2.destroyAllWindows()