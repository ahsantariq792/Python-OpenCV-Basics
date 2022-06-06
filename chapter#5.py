import cv2
import numpy as np

#Reading Images

img = cv2.imread("Resources/card.jpg")
cv2.imshow("image",img)
cv2.waitKey(0)


#warp perspective
#taking a part of image and adjusting it

width,height = 300,400
ps1 = np.float32([[158,99],[359,130],[116,376],[312,407]])
ps2 = np.float32([[0,0], [width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(ps1,ps2)
imgoutput= cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("output",imgoutput)
cv2.waitKey(0)
