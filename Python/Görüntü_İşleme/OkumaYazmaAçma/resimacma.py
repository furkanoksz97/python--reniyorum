import cv2
import numpy as np

resim = cv2.imread("logo.png",0) # imread resim okuma metodur. -->> 0 parametresini kullanırsak renkleri griye çevirir.

cv2.imshow("Merhaba Dunya", resim) # imshow görüntüyü ekranda görüntüleme metodudur.

cv2.imwrite("griLogo.png",resim) # imwrite Resmi Kaydetme

cv2.waitKey(0) # waitKey görüntülediğimiz resmin ekranda kalma süresini belirler.

cv2.destroyAllWindows() # tüm pencereleri kapamaya yarar.

