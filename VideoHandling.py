import cv2  
import time


pt1 = (0,0)
pt2 = (0,0)
topLeft_click = False
botRight_click = False


def draw_rect(img, width, height):

	x1, y1 = width//2, height//2
	x2, y2 = x1+width//4, y1+height//4
	cv2.rectangle(img, (x1,y1), (x2,y2), (0,0,255), 4)


def draw_interactive_rect(event, x, y, flag, param):

	global pt1, pt2, topLeft_click, botRight_click

	if event == cv2.EVENT_LBUTTONDOWN:

		if topLeft_click and botRight_click:
			pt1, pt2 = (0,0), (0,0)
			topLeft_click, botRight_click = False, False

		if topLeft_click == False:
			pt1 = (x,y)
			topLeft_click = True

		elif botRight_click == False:
			pt2 = (x,y)
			botRight_click = True


def video_capture():

	cap = cv2.VideoCapture(0)

	width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
	height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
	frame_rate = cap.get(cv2.CAP_PROP_FRAME_COUNT)  #why is frame rate -1 ?

	print(width, height, frame_rate)

	global pt1, pt2, topLeft_click, botRight_click

	cv2.namedWindow("My feed")
	cv2.setMouseCallback("My feed", draw_interactive_rect)

	#writer = cv2.VideoWriter("Webcam_feed.mp4", cv2.VideoWriter_fourcc(*'XVID'), 20, (width, height))	

	while True:
		ret, frame = cap.read()

		#draw_rect(frame, width, height)
		if topLeft_click:
			cv2.circle(frame, pt1, 2, (0,0,255), -1)
			
		if topLeft_click and botRight_click:
			cv2.rectangle(frame, pt1, pt2, (0,0,255),2)

		#writer.write(frame)

		cv2.imshow("My feed",frame)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	cap.release()
	#writer.release()
	cv2.destroyAllWindows()	


def video_play():

	cap = cv2.VideoCapture("Webcam_feed.mp4")

	width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
	height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
	frame_rate = cap.get(cv2.CAP_PROP_FRAME_COUNT)
	fps = 20

	print(width, height, frame_rate)

	if cap.isOpened() == False:
		print("Error in opening file")

	while cap.isOpened():
		ret, frame = cap.read()

		if ret==True:
			time.sleep(1/fps)
			cv2.imshow("Playing saved video", frame)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
		else:
			break

	cap.release()
	cv2.destroyAllWindows()


def main():
	video_capture()
	#video_play()


if __name__ == '__main__':
	main()