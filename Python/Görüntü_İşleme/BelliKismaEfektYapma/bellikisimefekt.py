import cv2
import numpy as np

resim = cv2.imread("Kemalsunal.jpg")

resim[100:150,250:370,0]=50
resim[100:150,250:370,1]=70

cv2.imshow("Kemal Sunal", resim)
cv2.waitKey()
cv2.destroyAllWindows()