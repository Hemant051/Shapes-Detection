# Contours/Shape Detection
import cv2
import numpy as np
#defining the contour function
def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        # Bounding the minimum area of the detected shapes to be 500
        if area>500:
             # line to draw contour
             cv2.drawContours(imgContour,cnt,-1,(0,255,0),2)
             peri = cv2.arcLength(cnt,True)
             print(peri)
             approx = cv2.approxPolyDP(cnt,0.02*peri,True)
             print(len(approx))
             objectcorner = len(approx)
             x, y, w, h = cv2.boundingRect(approx)
             # code for detecting triangle
             if objectcorner == 3: objectType = "Tri"
             #code for detecting square and rectangle
             elif objectcorner ==4:
                 aspRatio = w/float(h)
                 if aspRatio > 0.95 and aspRatio < 1.05: objectType = "Square"
                 else: objectType = "Rect"
             # code for detecting circle
             elif objectcorner > 4: objectType = "Circle"
             else: objectType="None"
             # making a red color boundry outside detected shapes
             cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,0,255),5)
             cv2.putText(imgContour,objectType,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)
# reading the image for detecting the shape
img = cv2.imread("Shape.jpg")
#making a copy of the image
imgContour = img.copy()
#making the color image as gray
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# blurring the gray image
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
#detecting the borders from the blurr image
imgCanny = cv2.Canny(imgBlur,50,50)
#calling the getContours function
getContours(imgCanny)
#printing the original image
cv2.imshow("Original",img)
#printing the gray image
cv2.imshow("Gray",imgGray)
#printing the blur image
cv2.imshow("Blur",imgBlur)
#printing the image with borders
cv2.imshow("Canny",imgCanny)
#printing the resulted image
cv2.imshow("Contours",imgContour)
#putting the wait key so that we see th images before they disappear
cv2.waitKey(0)
