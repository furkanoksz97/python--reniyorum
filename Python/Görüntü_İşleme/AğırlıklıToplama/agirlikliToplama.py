import  cv2
import  numpy as np

resim1 = cv2.imread("image.jpg")
resim2 = cv2.imread("image2.jpg")

print(resim1[80,150])
print(resim2[150,250])

cv2.imshow("Resim1",resim1)
cv2.imshow("Resim2",resim2)

print(resim1[80,150]+resim2[150,250])

cv2.waitKey()
cv2.destroyAllWindows()

# Toplama 255 i geçiyorsa 0 dan tekrar başlar.  2 + 255 = 1