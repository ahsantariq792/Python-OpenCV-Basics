import cv2

#Reading Images

img = cv2.imread("Resources/image.jpg")
imgShow = cv2.imshow("image",img)
cv2.waitKey(0)
#image window will not close immediately


#Reading Videos

cap = cv2.VideoCapture("Resources/video.mp4")

while True:
    success,img = cap.read()
    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break #press q to exit



#Opening Web Cam

cap = cv2.VideoCapture(0)
# 0 for default webcam
cap.set(3,640) #width
cap.set(4,480) #height
cap.set(10,0) #brightness

while True:
    success, img = cap.read()
    cv2.imshow("Web Cam", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

