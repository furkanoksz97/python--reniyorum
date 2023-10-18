import cv2
import numpy as np

resim = cv2.imread("Kemalsunal.jpg")

resim[:,:,0]=255 # 0 Mavi  1 Yeşil  2 Kırmızı

cv2.imshow("Kemal Sunal", resim)
cv2.waitKey()
cv2.destroyAllWindows()