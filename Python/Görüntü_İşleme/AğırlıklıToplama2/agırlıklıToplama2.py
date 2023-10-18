import cv2
import numpy as np
# Resimleri birbinin üstüne toplamak için boyutları aynı olmalı
resim1 = cv2.imread("image.jpg")
resim2 = cv2.imread("image2.jpg")

cv2.imshow("Resim1",resim1)
cv2.imshow("Resim2",resim2)

toplam = cv2.add(resim1,resim2)
agirlikliToplama = cv2.addWeighted(resim1,0.7,resim2,0.3,0) # saydamlık veriyoruz verilen oranların toplamı 1 olmak zorunda

cv2.imshow("Toplanmis Resim",toplam)
cv2.imshow("Agirlikli Toplama",agirlikliToplama)

cv2.waitKey()
cv2.destroyAllWindows()
