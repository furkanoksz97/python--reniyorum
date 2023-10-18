import cv2 

image = cv2.imread("image.jpg",0)

"""
ret (Return Value): Eşikleme işlemi sırasında kullanılan gerçek eşik değerini temsil eder. 
Bu değer, belirttiğiniz eşik değeriyle ilgili olabilir veya belirli bir otomatik eşikleme yöntemi kullanıldığında 
hesaplanmış bir değer olabilir.

thresh1 (Thresholded Image): Görüntünün eşiklenmiş (thresholded) hali. Bu görüntü, belirlediğiniz eşik değeri veya 
otomatik olarak hesaplanan eşik değerine göre siyah ve beyaz piksellerden oluşur.
"""

ret,thresh1 = cv2.threshold(image,127,255,cv2.THRESH_BINARY) # 127 altı sıfıra yuvarlanacak
ret,thresh2 = cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(image,127,255,cv2.THRESH_TRUNC)   
ret,thresh4 = cv2.threshold(image,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(image,127,255,cv2.THRESH_TOZERO_INV)

cv2.imshow("Orjinal",image)
cv2.imshow("Thresh1",thresh1)
cv2.imshow("Thresh2",thresh2)
cv2.imshow("Thresh3",thresh3)
cv2.imshow("Thresh4",thresh4)
cv2.imshow("Thresh5",thresh5)

cv2.waitKey()
cv2.destroyAllWindows()