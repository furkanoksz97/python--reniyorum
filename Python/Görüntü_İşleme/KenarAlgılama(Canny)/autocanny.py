import cv2
import numpy as np

image = cv2.imread("thor.jpg")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)

def autoCanny(blur,sigma=0.33):
    median = np.median(blur)
    lower = int(max(0,(1.0-sigma)*median))
    upper = int(min(255,(1.0+sigma)*median))
    canny = cv2.Canny(blur,lower,upper)
    return canny
"""
median değişkeni:
görüntünün üzerinde Gauss filtresi uygulanarak bulanıklaştırılmış hali (genellikle "blur" olarak adlandırılır) 
üzerinde median (ortanca) değerini hesaplar. Ortanca değeri hesaplamak, görüntünün genel parlaklık seviyesini 
temsil eder.

sigma: otomatik olarak yapılandırılmak istenen Canny kenar algılama işlemi için bir parametre olarak kullanılır. 
Varsayılan olarak 0.33 olarak ayarlanır, ancak bu değeri gerektiğinde değiştirebilirsiniz.

lower ve upper değişkenleri: Canny kenar algılama için alt ve üst eşik değerlerini hesaplar. 
Bu eşik değerleri, görüntüdeki kenarları tespit etmek için kullanılır.

Hesaplanan lower ve upper eşik değerleri kullanılarak, cv2.Canny işlevi çağrılır ve bu eşik değerleri ile kenar 
tespiti işlemi gerçekleştirilir.

Son olarak, bu kenar tespiti sonucu, canny adlı bir görüntü olarak döndürülür.
"""
wide = cv2.Canny(blur,10,220)
tight = cv2.Canny(blur,200,230)
auto = autoCanny(blur)


cv2.imshow("blurred image",blur)
#cv2.imshow("canny image",auto)
#cv2.imshow("wide image",wide)
#cv2.imshow("tight image",tight)
cv2.imshow("edges",np.hstack([wide,tight,auto]))
"""
cv2.imshow("edges", ...) işlevi, görüntüyü ekranda göstermek için kullanılır. 
"edges" adında bir pencere başlığı belirler ve ardından görüntüyü bu pencerede görüntüler.

np.hstack([wide, tight, auto]): Bu kısım, üç farklı kenar tespiti sonucunu yatay olarak birleştirmek için kullanılır. 
wide, tight ve auto, önceki kod parçacığında oluşturulan kenar tespiti sonuçlarıdır.

Sonuç olarak, bu kod satırı, farklı eşik değerleri ve kenar tespiti parametreleri kullanılarak elde edilen 
üç farklı kenar tespiti sonucunu aynı pencerede yatay olarak yan yana görüntüler. Bu, farklı eşikleme seviyeleri 
kullanarak kenar algılama sonuçlarını karşılaştırmak ve doğru eşik değerlerini seçmek için kullanışlı bir görsel araçtır.
"""
cv2.waitKey()
cv2.destroyAllWindows()

