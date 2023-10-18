import cv2
import numpy as np

resim = cv2.imread("kus.png")
cv2.imshow("Kus resmi",resim)

print(resim) # çıktıdaki resmin matrislerini görürüz
print(resim.size) # resmin boyutu
print(resim.dtype) # veri tipi
print(resim.shape) # genişlik yükseklik kanal sayısı.

cv2.waitKey()
cv2.destroyAllWindows()