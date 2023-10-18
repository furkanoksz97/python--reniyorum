import cv2
import numpy as np

image1 = cv2.imread("1.png")
image2 = cv2.imread("2.png")

#bitwise_and = cv2.bitwise_and(image1,image2)
#bitwise_or = cv2.bitwise_or(image1,image2)
#bitwise_not = cv2.bitwise_not(image1)
#bitwise_not_2 = cv2.bitwise_not(image2)
bitwise_xor = cv2.bitwise_xor(image1,image2)


cv2.imshow("Image 1",image1)
cv2.imshow("Image 2",image2)
#cv2.imshow("bitwise and",bitwise_and)
#cv2.imshow("bitwise or",bitwise_or)
#cv2.imshow("bitwise not",bitwise_not)
#cv2.imshow("bitwise not 2",bitwise_not_2)
cv2.imshow("bitwise xor",bitwise_xor)


cv2.waitKey()
cv2.destroyAllWindows()