import cv2
import numpy as np

resim = np.zeros((300,300,3),dtype="uint8") # 0-255 arası uint8

cv2.line(resim,(0,0),(300,300),(0,0,255),3) #tanımlanan resim, nerden nereye, hangi renk, kalınlık

cv2.circle(resim,(150,150),50,(0,255,0),2) #tanımlanan resim, merkez belirle, yarıçapı, hangi renk, kalınlık

cv2.putText(resim,"DenemeText",(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),1) #tanımlanan resim, ne yazılacak, başlangıç, yazı tipi, yazı boyutu, renk, kalınlık

cv2.imshow("deneme",resim)

cv2.waitKey()
cv2.destroyAllWindows()