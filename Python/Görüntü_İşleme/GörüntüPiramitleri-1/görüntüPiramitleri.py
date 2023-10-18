import cv2
import numpy as np

resim = cv2.imread("images.jpg")

resmiBuyut = cv2.pyrUp(resim) # resmi büyütmek iki taraftan 2x
resmiKucult = cv2.pyrDown(resim) 

print("orj : ",resim.shape)
print("resmibuyut : ",resmiBuyut.shape)
print("resmikucult : ",resmiKucult.shape)

cv2.imshow("orj", resim)
cv2.imshow("resmibuyut",resmiBuyut)
cv2.imshow("resmikucult",resmiKucult)

cv2.waitKey()
cv2.destroyAllWindows()

