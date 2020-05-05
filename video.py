import cv2
import time

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video = cv2.VideoCapture(0)

a = 1

while True:
	a  = a + 1
	check, frame = video.read()
	print(frame)
	if check != False:
		gray = cv2.cvtColor(frame ,cv2.COLOR_BGR2GRAY)
		face = face_cascade.detectMultiScale(gray, scaleFactor = 1.05, minNeighbors = 5)
		for x,y,w,h in face:
			img = cv2.rectangle(frame, (x,y), (x+w,y+h),(0,255,0),3)
		cv2.imshow("ME",frame)
		key = cv2.waitKey(1)
		if key == ord('q'):
			break
	else:
		break

video.release()
cv2.destroyAllWindows()