import cv2 

image = cv2.imread("parmakizi.jpg",0)

#simple Thresholding
ret,thresh1 = cv2.threshold(image,160,255,cv2.THRESH_BINARY)

#adaptive thresholding
thresh2 = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
"""
* image: Eşikleme işleminin uygulanacağı giriş görüntüdür.
* 255: Maksimum piksel değeri. Eşikleme sonucunda beyaz olarak işaretlenen piksellerin değerini temsil eder.
* cv2.ADAPTIVE_THRESH_MEAN_C: Adaptif eşikleme yöntemini belirler. Bu durumda "ortalama (mean) tabanlı" adaptif 
eşikleme yöntemi kullanılır. Bu yöntem, her piksel için adaptif bir eşik değeri hesaplar ve pikselin çevresindeki 
bölgeye dayanır.
* cv2.THRESH_BINARY: Eşikleme türünü belirler. Bu durumda, piksel değeri eşik değerinin altında kalan pikseller siyah, 
üstünde kalanlar beyaz olarak işaretlenir.
* 11: Eşikleme işlemi sırasında her pikselin etrafındaki bölgenin boyutunu belirler. Burada 11, bölgenin boyutunu 
belirten bir parametredir.
* 2: Ortalama eşikleme yönteminde hesaplanan eşik değeri üzerine eklenen veya çıkarılan bir sabit değeri temsil eder. 
Bu değer, hesaplanan eşik değerini ayarlamak için kullanılır.
"""

thresh3 = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
"""
* cv2.ADAPTIVE_THRESH_GAUSSIAN_C: Adaptif eşikleme yöntemini belirler. Bu durumda "Gaussian ortalama 
(Gaussian mean) tabanlı" adaptif eşikleme yöntemi kullanılır.
"""
cv2.imshow("Orjinal",image)
cv2.imshow("simple Thresholding",thresh1)
cv2.imshow("adaptive thresholding1",thresh2)
cv2.imshow("adaptive thresholding2",thresh3)
cv2.waitKey()
cv2.destroyAllWindows()

"""
cv2.ADAPTIVE_THRESH_MEAN_C düşük frekanslı bileşenlere vurgu yapar ve sonuç daha pürüzsüzdür. 
cv2.ADAPTIVE_THRESH_GAUSSIAN_C ise daha keskin konturlar ve ayrıntılar yakalar.
"""