# This script will detect faces via your webcam.
# Tested with OpenCV3

import cv2
import time

cap = cv2.VideoCapture(0)

cap.set(3,720/10)     #horizontal pixels
cap.set(4,480/10)     #vertical pixels
cap.set(5, 15)      #frame rate
time.sleep(2)  

# Create the haar cascade
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()

	# Our operations on the frame come here
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# Detect faces in the image
	faces = faceCascade.detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30, 30)
		#flags = cv2.CV_HAAR_SCALE_IMAGE
	)

	print("Found {0} faces!".format(len(faces)))
	
	if len(faces) > 0:
		(x, y, w, h) = faces[0]
	
		print(y+h/2)

		is_up = 480/4

		if (y+h/2 < 480/3):
			print("up")
		elif (y+h/2 > 480*2/3):
			print("down")
		else:
			print("middle")

	

	# Draw a rectangle around the faces
	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)


	# Display the resulting frame
	cv2.imshow('frame', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
