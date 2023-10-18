import cv2

camera = cv2.VideoCapture(0)

width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH)) #kameranın boyutu
height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(width,height)

fourcc = cv2.VideoWriter_fourcc(*"MP4V") #format belirleme

writer = cv2.VideoWriter("kayit.mp4",fourcc,20,(width,height)) #dizin(yol), format, görüntü hızı, genişlik yükseklik


while True:
    ret,frame = camera.read() # ret = kameranın çalışması için oluşturulan değişken frame = belirlenen sürede görüntü almak için olan değişken
    writer.write(frame)
    cv2.imshow("Kamera Kayit Videosu",frame)

    if cv2.waitKey(25) & 0xFF == ord("q"): # 25ms sürede görüntü al    0xFF == ord("q") q tuşuna basıldığında çık
        break


camera.release()
writer.release()
cv2.destroyAllWindows()

"""
cv2.VideoCapture(0): Kamerayı başlatır. Kameranın cihazını belirtmek için 0 kullanılır, 
bu genellikle bilgisayarınızda varsayılan kamera anlamına gelir.

Kameranın genişliği ve yüksekliği alınır ve width ve height değişkenlerine atanır. 
Bu, kaydedilen video dosyasının boyutunu belirlemek için kullanılır.

fourcc = cv2.VideoWriter_fourcc(*"MP4V"): Kaydedilen video dosyasının formatını belirler. 
Bu örnekte, MP4V formatı kullanılır.

cv2.VideoWriter("kayit.mp4", fourcc, 20, (width, height)): Video kaydediciyi başlatır. "kayit.mp4" 
video dosyasının adını, fourcc formatı, 20 kare/saniye (FPS) hızını ve video çerçevesinin genişliğini 
ve yüksekliğini belirler.

Sonsuz bir döngü (while True) başlar:

camera.read(): Kameradan bir kare alır ve bu çerçeveyi frame değişkenine atar.
writer.write(frame): Aldığınız her kareyi video dosyasına yazmak için kullanılır.
cv2.imshow("Kamera Kayit Videosu", frame): Kameradan alınan kareyi bir pencerede gösterir.
Kullanıcı "q" tuşuna basarak döngüyü sonlandırabilir. cv2.waitKey(25) işlevi, her bir çerçeve arasındaki 
bekleme süresini ifade eder.

Döngü sona erdiğinde, kamera kaynağını serbest bırakmak ve video dosyasını kapatmak için camera.release() 
ve writer.release() kullanılır.

cv2.destroyAllWindows(): Tüm açık penceleri kapatır ve işlemi sonlandırır.

Bu kod, kameradan görüntü alarak ve bu görüntüyü belirlediğiniz bir video dosyasına kaydederek basit bir 
video kaydı işlemi yapar.
"""