import cv2

image = cv2.imread("parmakizi.jpg",0)

#simple
ret,thresh = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
#otsu
ret1,thresh1 = cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow("orjinal",image)
cv2.imshow("simple",thresh)
cv2.imshow("otsu",thresh1)


cv2.waitKey()
cv2.destroyAllWindows()
