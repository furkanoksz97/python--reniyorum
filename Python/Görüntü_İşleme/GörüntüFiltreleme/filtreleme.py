import cv2
import numpy as np

image = cv2.imread("image2.jpg")
#doğrusal filtreleme
meanFilter = cv2.blur(image,(3,3)) #işlem yapılacak resim, şablon bilgisi
meanFilter1 = cv2.blur(image,(5,5))
meanFilter2 = cv2.blur(image,(7,7))
#doğrusal olmayan filtreleme
medianFilter = cv2.medianBlur(image,3) # işlem yapılacak resim, kaça kaç şablon olacak
medianFilter1 = cv2.medianBlur(image,5)
medianFilter2 = cv2.medianBlur(image,7)
#eşit ağırlıklandırma yaparak filtreler daha iyi filtreleme yapar
gauss = cv2.GaussianBlur(image,(3,3),0)
gauss1 = cv2.GaussianBlur(image,(5,5),0)
gauss2 = cv2.GaussianBlur(image,(7,7),0)
cv2.imshow("orj",image)

cv2.imshow("filter",meanFilter)
cv2.imshow("filter1",meanFilter1)
cv2.imshow("filter2",meanFilter2)

cv2.imshow("mFilter",medianFilter)
cv2.imshow("mFilter1",medianFilter1)
cv2.imshow("mFilter2",medianFilter2)

cv2.imshow("Gauss",gauss)
cv2.imshow("Gauss1",gauss1)
cv2.imshow("Gauss2",gauss2)

cv2.waitKey()
cv2.destroyAllWindows()




















