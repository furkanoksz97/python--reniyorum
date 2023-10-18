"""
Yöntem gri seviye görüntüler üzerinde de çalışsa da genellikle siyah-beyaz (ikili) görüntüler üzerinde kullanılır. 
Morfolojik filtreler genelde iki temel işlemden türetilmiştir. Bunlar erosion (aşındırma, daraltma) ve dilation 
genişletme) işlemleridir.
"""
import cv2
import numpy as np

image = cv2.imread("image.png")

kernel = np.ones ((2,2),np.uint8) # Yapılandırma elemanı 5e5lik matris oluşturduk elemanları 1 olacak şekilde

dilation = cv2.dilate(image,kernel,iterations=1) 
# Dilation (Yayma – Genişletme) Morfolojik Operatör
# Fakat beyaz yerleri inceltmek yerine kalınlaştırır. Bunu “dilate()” fonksiyonu ile sağlar. 
# Bu fonksiyon parametre olarak; işlem yapılacak görüntü, görüntünün üzerinde hareket edecek kutucuk ve ”iterations” 
# değerini alır. Bu “iterations” değeri, görüntüye kaç kez genişleme uygulanacağını belirler.

erosion = cv2.erode(image,kernel,iterations=1)
# Bir görüntü üzerindeki parlak bölgeleri küçülten veya azaltan bir morfolojik işlemdir. 
# Bu işlem, gürültü temizleme, nesne ayırma ve kontur algılama gibi görüntü işleme uygulamalarında kullanılır.

opening = cv2.morphologyEx(image,cv2.MORPH_OPEN,kernel)
# Gürültü Temizleme: Açma işlemi, görüntüdeki küçük gürültü noktalarını veya delikleri temizlemek için kullanılır. 
# Özellikle, nesnelerin etrafındaki gürültüyü azaltmak için etkilidir.

#Nesne Ayrımı: Nesneler arasındaki boşlukları açarak nesneleri ayırmak için kullanılabilir. Açma işlemi, 
#nesnelerin birbirine bağlı olabileceği durumlarda, bu nesneleri birbirinden ayırmanıza yardımcı olur.

closing = cv2.morphologyEx(image,cv2.MORPH_CLOSE,kernel)
#Nesneleri Birleştirme: Kapanma işlemi, nesnelerin birbirine yakın olan bölgelerini birleştirmek için kullanılır. 
#Bu işlem, nesneler arasındaki küçük boşlukları doldurur ve nesneleri daha büyük bir bütün haline getirir.

#Gürültü Temizleme: Görüntülerdeki küçük gürültü noktalarını veya delikleri kapatmak için de kullanılabilir. 
#Özellikle, nesnelerin etrafındaki gürültüyü azaltmak için etkilidir.

gradyan = cv2.morphologyEx(image,cv2.MORPH_GRADIENT,kernel)
#Kenar Tespiti: Gradyan işlemi, nesnelerin kenarlarını tespit etmek için kullanılır. İşlem sonucunda, nesnelerin kenarları 
#vurgulanır ve bu kenarlar görüntüde belirginleşir.

#Kontur Algılama: Konturlar, nesnelerin dış hatlarıdır, ve gradyan işlemi konturları belirlemek için kullanılır. 
#Bu, nesnelerin şeklini ve konumunu tespit etmek için önemlidir

tophat = cv2.morphologyEx(image,cv2.MORPH_TOPHAT,kernel)
#Işık Miktarının Farkı: Tophat işlemi, bir görüntüdeki parlaklık veya ışık miktarındaki farkları belirler.
#Bu, özellikle arka plana göre daha karanlık veya daha parlak nesneleri tespit etmek için kullanılır.

#Nesne Algılama: Tophat işlemi, görüntüdeki nesnelerin belirgin özelliklerini vurgular. 
#Bu, nesneleri tespit etmek veya nesne sınırlarını belirlemek için kullanışlıdır.

#Gürültü Temizleme: Görüntülerdeki küçük gürültü noktalarını veya delikleri temizlemek için de kullanılabilir.
#Özellikle nesnelerin etrafındaki gürültüyü azaltmak için etkilidir.

blackhat = cv2.morphologyEx(image,cv2.MORPH_BLACKHAT,kernel)
#Işık Miktarının Farkı: Blackhat işlemi, bir görüntüdeki parlaklık veya ışık miktarındaki farkları belirler. 
#Bu işlem, özellikle arka plana göre daha karanlık veya daha parlak nesneleri tespit etmek için kullanılır.

#Nesne Algılama: Blackhat işlemi, görüntüdeki nesnelerin belirgin özelliklerini vurgular. 
#Bu, nesneleri tespit etmek veya nesne sınırlarını belirlemek için kullanışlıdır.

#Kontrast Artırma: Blackhat işlemi, nesnelerin arka plana veya ortama göre kontrastını artırabilir. 
#Bu sayede nesneler daha belirgin hale gelir ve algılama işlemi daha iyi hale gelir.

cv2.imshow("Orjinal",image)
cv2.imshow("dilation",dilation)
cv2.imshow("erosion",erosion)
cv2.imshow("opening",opening)
cv2.imshow("closing",closing)
cv2.imshow("gradyan",gradyan)
cv2.imshow("tophat",tophat)
cv2.imshow("blackhat",blackhat)

cv2.waitKey()
cv2.destroyAllWindows()
