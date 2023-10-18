import cv2
import numpy as np

resim = cv2.imread("resim.jpg")

tekrarlananResim = cv2.copyMakeBorder(resim,200,200,200,200,cv2.BORDER_WRAP) 
#Çekilecek resim ve boyutlandırması ve o resme yapılacak ne yapılacak ise o fonk yazılır.

cv2.imwrite("Tekrarlanan_Denzel.jpg",tekrarlananResim)
cv2.imshow("Denzel", tekrarlananResim)
cv2.waitKey()
cv2.destroyAllWindows()