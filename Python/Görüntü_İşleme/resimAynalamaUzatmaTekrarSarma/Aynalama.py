import cv2
import numpy as np

resim = cv2.imread("resim.jpg")

aynalananResim = cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_REFLECT)
#Çekilecek resim ve boyutlandırması ve o resme yapılacak ne yapılacak ise o fonk yazılır.

cv2.imwrite("Aynalama_Denzel.jpg",aynalananResim)
cv2.imshow("Denzel", aynalananResim)
cv2.waitKey()
cv2.destroyAllWindows()
