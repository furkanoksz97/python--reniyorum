import cv2
import numpy as np

resim = cv2.imread("image.jpg")

cv2.rectangle(resim,(510,90),(700,250),[0,0,255],3) 
"""
rectangle parametreleri 
1.Hangi resim uygulanacak
2.y ekseni nerden başlasın
3.x ekseni nerden başlasın
4.çervenin rengi
5.çerçevenin kalınlığı
"""
print(resim[500,500])

 
cv2.imshow("Cehennem Melekleri ",resim)
cv2.waitKey()       
cv2.destroyAllWindows()
