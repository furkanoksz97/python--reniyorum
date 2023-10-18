import cv2
import numpy as np

kamera = cv2.VideoCapture(0) # kamera modülü parametre 0 =>pc kendi. 1 =>usb tanımlı olan kamera. 2 =>tanımlanan videodan görüntü alır

while True:
    ret,goruntu = kamera.read() # ret = kameranın çalışması için oluşturulan değişken goruntu = belirlenen sürede görüntü almak için olan değişken

    cv2.imshow("Kamera",goruntu)

    if cv2.waitKey(30) & 0xFF == ord("q"): # 30ms sürede görüntü al    0xFF == ord("q") q tuşuna basıldığında çık
        break

kamera.release()#kamera okumaktan çık

cv2.destroyAllWindows()
























