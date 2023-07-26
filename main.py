import cv2
import  numpy as npq

cap=cv2.VideoCapture('e.mp4')
while cap.isOpened():
     _,frame=cap.read()
     roi=frame[1655:2250,400:1300]
     #roi=frame[1250:1500,400:900]
     rows,col,_=frame.shape
     print(str(rows),str(col))
     gray_frame=cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
     blur=cv2.GaussianBlur(gray_frame,(5,5),0)
     _,thresh=cv2.threshold(blur,4.5,255,cv2.THRESH_BINARY_INV)#to inverse black (fullground)
     contours,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
     contour=sorted(contours,key=lambda x:cv2.contourArea(x),reverse=True)

     for con in contour:
         (x,y,w,h)=cv2.boundingRect(con)
         cv2.rectangle(roi,(x,y),(x+w,y+h),(255,23,255),1)
         cv2.line(roi,(x+int(w/2),0),(x+int(w/2),rows),(0,200,20),1)
         cv2.line(roi,(0,y+int(h/2)),(col,y+int(h/2)),(0,200,20),1)
         break


     cv2.imshow("thresh",thresh)
     cv2.imshow("gray",gray_frame)
     cv2.imshow("frame",roi)
     if cv2.waitKey(50)==ord('q'):
         break
cv2.destroyWindow()
cap.release()