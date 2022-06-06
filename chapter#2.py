import cv2
import numpy as np
img = cv2.imread("Resources/image.jpg")

#GreyScale Images

imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grey Image", imgGrey)
cv2.waitKey(0)

#Blur Images
imgBlur = cv2.GaussianBlur(imgGrey, (7,7),0)
cv2.imshow("Blur Image", imgBlur)
cv2.waitKey(0)

#Edge Detector

imgCanny = cv2.Canny(img,100,100)
cv2.imshow("Edge Detector", imgCanny)
cv2.waitKey(0)

#Broad Edges
kernel = np.ones((5,5),np.uint8)

imgDilation = cv2.dilate(imgCanny, kernel, iterations = 1)
cv2.imshow("Broad Edges", imgDilation)
cv2.waitKey(0)

#Thinner Edges

imgErosion = cv2.erode(imgDilation, kernel, iterations = 1)
cv2.imshow("Thin Edges", imgErosion)
cv2.waitKey(0)




