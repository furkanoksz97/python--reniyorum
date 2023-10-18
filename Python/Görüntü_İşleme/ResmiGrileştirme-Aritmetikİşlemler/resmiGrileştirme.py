import cv2
import numpy as np

resim = cv2.imread("image.jpg")
resimGri = cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)

yukseklik,genislik,kanalsayisi = resim.shape
print("Orjinal: ", yukseklik,genislik,kanalsayisi)
yukseklik1,genislik1 = resimGri.shape #kanal sayisi 1 olacağı için shape o veriyi tutmak istemez o yüzden gri fotoğrafta kanalsayısı sorgusu yapılmaz
print("Grii: : ", yukseklik1,genislik1)



cv2.imshow("orjinal resim",resim)
cv2.imshow("grilestirilmis resim",resimGri)
cv2.waitKey()
cv2.destroyAllWindows
