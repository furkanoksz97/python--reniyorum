import cv2
import numpy as np

resim = cv2.imread("images.jpg")

kesit = resim[50:150,50:100]  # 50:150 => y  50:100 => x

kesit[:,:,0] = 255
cv2.imshow("kesit alani",kesit)
cv2.imshow("Resim",resim)
cv2.waitKey()
cv2.destroyAllWindows()
