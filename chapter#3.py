import cv2

#Size of image
img = cv2.imread("Resources/image.jpg")
print(img.shape)

#Crop Images
img2 = img[0:300, 200: 500]  #[height,width]
cv2.imshow("Crop Image", img2)
cv2.waitKey(0)

#Resize Images
img2 = cv2.resize(img,(200,400)) #[width, height]
cv2.imshow("Resize Image", img2)
cv2.waitKey(0)