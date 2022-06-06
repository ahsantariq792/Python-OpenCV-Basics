import cv2
import numpy as np


# Generating Black image
imgBlack = np.zeros((512,512))
cv2.imshow("Black Image", imgBlack)
cv2.waitKey(0)

# Generating Black image (Another Method)
img = np.zeros((512,512,3), np.uint8)
cv2.imshow("Black Image", img)
cv2.waitKey(0)

# Making Black Image Blue
img[:] = 255,0,0
cv2.imshow("Blue Image", img)
cv2.waitKey(0)

# Making a specific location of Black Image Blue
img[0:20, 0:30] = 255,0,0
cv2.imshow("Blue Image", img)
cv2.waitKey(0)

#drawing line on image
imgline= cv2.line(img,(0,0),(img.shape[1], img.shape[0]), (0,255,0),3)
cv2.imshow("Line Image", imgline)
cv2.waitKey(0)

#drawing rectangle on image
imgRectangle= cv2.rectangle(img,(0,0),(250,350), (0,255,0),3)
cv2.imshow("Rectangle Image", imgRectangle)
cv2.waitKey(0)

imgRectangleFilled= cv2.rectangle(img,(0,0),(250,350), (0,255,0),cv2.FILLED)
cv2.imshow("Filled Rectangle Image", imgRectangleFilled)
cv2.waitKey(0)


#Putting Text on Image
imgText = cv2.putText(img, "text",(300,100),cv2.FONT_ITALIC,1,(0,500,0),3)
cv2.imshow("Filled Rectangle Image", imgText)
cv2.waitKey(0)









