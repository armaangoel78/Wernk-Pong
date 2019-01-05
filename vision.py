import numpy as np
import cv2

cap = cv2.VideoCapture(0)

def process(i):
    hsv = cv2.cvtColor(i,cv2.COLOR_BGR2HSV)
        
    min = np.array([0,0,253])
    max = np.array([255,255,255])
    
    
    filtered = cv2.inRange(hsv, min, max)
    
    kernel = np.ones((5,5),np.uint8)
    eroded = cv2.erode(filtered,kernel,iterations = 2)
    dilated = cv2.dilate(eroded,kernel,iterations = 4)
            
    edged = cv2.Canny(dilated, 30, 200)
    
    a, cnts, b = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
        
    if (len(cnts) > 0):
        x,y,w,h = cv2.boundingRect(cnts[0])
        cv2.rectangle(i,(x,y),(x+w,y+h),(0,255,0),2)

        print(y-h/2)
    
    return i


while(True):
    ret, frame = cap.read()

    o = process(frame)

    cv2.imshow('frame',o)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
