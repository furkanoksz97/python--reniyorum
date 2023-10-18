import cv2
import numpy as np

kamera = cv2.VideoCapture(0)

while True:
    ret,goruntu = kamera.read()

    cv2.rectangle(goruntu,(250,250),(500,400),(0,0,255),3)
    cv2.line(goruntu,(0,0),(480,640),(0,255,0),3)
    cv2.circle(goruntu,(50,50),50,(0,255,0),3)
    cv2.putText(goruntu,"DenemeText",(200,100),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),3)

    cv2.imshow("Canli Goruntu",goruntu)

    if cv2.waitKey(25) & 0xFF == ord("q"):
        break
print(goruntu.shape)
kamera.release()
cv2.destroyAllWindows()