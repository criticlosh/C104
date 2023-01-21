import cv2
image = cv2.imread("butterfly.jpg")
greyImage = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
cv2.imshow("output", greyImage)
cv2.waitKey(0)