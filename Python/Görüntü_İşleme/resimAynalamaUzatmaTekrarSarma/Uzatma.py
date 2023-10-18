import cv2
import numpy as np

resim = cv2.imread("resim.jpg")

uzatılanResim = cv2.copyMakeBorder(resim,120,120,120,120,cv2.BORDER_REPLICATE) 
#Çekilecek resim ve boyutlandırması ve o resme yapılacak ne yapılacak ise o fonk yazılır.

cv2.imwrite("Uzatma_Denzel.jpg",uzatılanResim)
cv2.imshow("Denzel", uzatılanResim)
cv2.waitKey()
cv2.destroyAllWindows()