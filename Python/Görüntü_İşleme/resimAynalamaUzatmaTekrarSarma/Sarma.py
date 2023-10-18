import cv2
import numpy as np

resim = cv2.imread("resim.jpg")

sarilanResim = cv2.copyMakeBorder(resim,20,20,20,20,cv2.BORDER_CONSTANT,value=(0,0,255)) 
#Çekilecek resim ve boyutlandırması ve o resme yapılacak ne yapılacak ise o fonk yazılır.

cv2.imwrite("Cerceveli_Denzel.jpg",sarilanResim)
cv2.imshow("Denzel", sarilanResim)
cv2.waitKey()
cv2.destroyAllWindows()