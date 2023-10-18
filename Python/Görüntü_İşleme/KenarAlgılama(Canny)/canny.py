import cv2
import numpy as np

image = cv2.imread("thor.jpg")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)
"""
gray: Gri tonlamalı (grayscale) bir görüntüdür. Gri tonlamalı görüntüler, renk bilgisini içermez ve yalnızca 
parlaklık bilgisini içerir.

(5, 5): Filtrin çekirdek (kernel) boyutunu belirtir. Bu, her bir yönde (yatay ve dikey) 5 piksel uzunluğunda 
bir Gauss filtresi çekirdeğinin kullanılacağı anlamına gelir. Bu çekirdek boyutu, filtreleme işleminin ne kadar
yumuşak veya keskin olacağını belirler. Daha büyük çekirdekler, daha fazla bulanıklık sağlar.

0: X ve Y yönlerindeki standart sapmayı belirtir. Standart sapma, Gauss filtresinin dağılımını kontrol eder ve ne 
kadar yayıldığını belirler. 0, otomatik olarak hesaplanmasını sağlar ve yayılmanın görüntüye uygun şekilde 
ayarlanmasını sağlar.
"""

canny = cv2.Canny(blur,100,200)
"""
blur: Kenar tespiti işlemi, daha önce bir Gauss bulanıklaştırma işlemine tabi tutulmuş olan bu bulanık 
(blur) görüntü üzerinde gerçekleştirilir. Bu bulanıklaştırma, görüntüdeki gürültüyü azaltmak ve daha iyi kenarlar 
elde etmek için uygulanır.

100: Alt eşik değeri olarak bilinir. Bu değer, kenar olarak kabul edilecek piksellerin gri ton değerlerinin bu alt 
eşik değerinden büyük olması gerektiğini belirtir.

200: Üst eşik değeri olarak bilinir. Bu değer, kenar olarak kabul edilecek piksellerin gri ton değerlerinin bu üst 
eşik değerinden büyük olması gerektiğini belirtir.

cv2.Canny işlevi, bu parametrelerle belirtilen eşik değerleri arasındaki gri ton değerlerine sahip pikselleri 
kenar olarak işaretler. Yani, belirtilen eşik değerlerine göre gri ton değeri aralığı dışındaki pikseller siyah,
aralığa dahil olanlar ise beyaz olarak işaretlenir. Bu işlem sonucunda, görüntünün kenarlarını temsil eden bir 
siyah-beyaz görüntü oluşturulur.

Sonuç olarak, bu kod satırı, Gauss bulanıklaştırılmış bir görüntü üzerinde Canny kenar algılama yöntemini uygular 
ve kenarları tespit eder. Bu işlem, görüntü işleme uygulamalarında nesne algılama, kontur tespiti ve diğer görevler 
için sıkça kullanılır.
"""

cv2.imshow("blurred image",blur)
cv2.imshow("canny image",canny)



cv2.waitKey()
cv2.destroyAllWindows()







