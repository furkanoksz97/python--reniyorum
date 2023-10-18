import cv2
import numpy as np

resim = cv2.imread("aslan.jpg")
cv2.imshow("Aslan Resmi",resim)

print(resim[(50,230)]) # yüklenilen resmin verilen değerlerdeki renk kodunu verir.

print("Resmin Boyutu: "+str(resim.size)+" Byte")
print("Resmin Özellikleri: "+str(resim.shape))
print("Resmin Veri Tipi: "+str(resim.dtype))

cv2.waitKey()
cv2.destroyAllWindows()

