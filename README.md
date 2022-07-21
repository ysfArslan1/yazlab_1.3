# Yazlab1 3. Proje    

# Web Uygulaması 

# Özet
Proje kullanıcının pdf dosyalarını yükleyebildiği ve bu yüklenen dökümanlardan temel bilgilerin çıkarılıp sorgulanabildiği bir web uygulamasıdır. Uygulama Python dili nde Django frameworkü kullanılarak geliştirilmiştir.Dokümanda projenin tanımı, çözüme yönelik yapılan araştırmalar, kullanılan fonksiyonlar, proje bitimindeki deneysel sonuçlar ve kod bilgisi gibi programın oluşumunu açıklayan başlıklara yer verilmiştir. Doküman sonunda projeyi hazırlarken kullandığımız kaynaklar bulunmaktadır.
# Giriş
Projede amaç kullanıcıların giriş yapıp pdf yüklemesi yapması sağlayarak pdften bilgi çekmeyi gerçekleştirmektir.Projede öncelikle kullanıcıya giriş yaptırılır.Giriş işleminden sonra kullanıcı isteğe bağlı olarak isterse önceden atılmış olan pdf’lerin çıktılarını kontrol edebilir ya da yeni bir pdf yükleyerek o pdf’in bilgilerini database’e kaydettirebilir.


# Genel Yapı

# Modeller:
# Accounts: 
Kullanıcıların giriş yapabilme,kaydolabilme ve çıkış yapabilmeleri için gerekli olan veritabanı işlemleri ve html bağlantılarını sağlayan bir modeldir.
# views.py: 
Kullanıcıların giriş,kayıt ve çıkış için kullandığı fonksiyonlar bulunur. urls.py: kullanılan fonksiyonlar için url tanımlaması yapılır.
# forms.py:
Yapılan işlemler için gerekli form ekranları için fonksiyonlar tutulur.

# Proje:

Tutulmak istenen pdflerinin işlemlerinin yapıldığı ve web sayfaları için kullanılan fonksiyonları bulunduğu modeldir.
models.py:Pdf’ten alınan bilgilerin tutulması için gereken veritabanı modeli ve fonksiyonları tutulur.

## views.py:
Model için kullanılan fonksiyonlar bulunur. urls.py:kullanılan fonksiyonlar için url tanımlaması yapılır. forms.py:Pdf’in yüklenmesi için form yapısı tutulur.
# Blog : 
Projede kullanılan modelleri bir arada kullanılmasını sağlayan fonksiyonların ve classların bulunduğu modeldir.
## settings.py:
Django’nu genel işleyişi için gereken ayarlar burada yapılır. 
urls.py:Projenin ana url’leri burada yazılır.

## PdfDonusturucu.py:
Bu class’ta alınan pdf’in metin işleme işlemleri burada yapılır. Templates:Web sayfaları için kullanılan .html uzantılı dosyalar burada tutulur.

# Temel Bilgiler
Proje geliştirmede:
Programlama dili olarak “Python” kullanılmıştır.
Program geliştirme ortamı olarak “Visual Studio Code” kullanılmıştır.

# Yapılan Araştırmalar:
Başlangıçta Web kodlaması konusunda zorlandık.Araştırmalarımız doğrultusunda Python dilinde geliştirilmiş Django framework’ünü uygun bulduk.Bu doğrultuda internet üzerinden okuduğumuz birkaç makale ve websitesiyle bu işe başladık.
Django ile web kısmınında ilerledikten sonra proje isterlerinden olan pdf ile metin işleme konusunda sıkıntı yaşadık.Bu doğrultuda pdfminer kütüphanesi yardımıyla metinden gerekli olan bilgileri çektik.

# Kazanımlar:
Bu araştırmalarımız doğrultusunda bir web proglamanın nasıl daha iyi gerçeklenebileceği ve uygulamanın arkasındaki veritabanı işlemlerinin nasıl yapıldığı konusunda kendimi geliştirmiş olduk.

# Akış Şeması:

![image](https://user-images.githubusercontent.com/58952369/180186469-e840e858-15c9-43f4-9e11-9d3a65e4b7a8.png)

Deneysel Sonuçlar ve Ekran Görüntüleri

![image](https://user-images.githubusercontent.com/58952369/180186522-15275788-495a-4ec7-b60a-5fdf655af1d7.png)


![image](https://user-images.githubusercontent.com/58952369/180186555-faaae661-2b78-40c8-a0e8-6a7ed0492f87.png)


![image](https://user-images.githubusercontent.com/58952369/180186571-cdc5ed74-a059-4813-a541-b833d2fc3190.png)


![image](https://user-images.githubusercontent.com/58952369/180186608-27b3036b-f22b-466d-bfae-feb40c417dd5.png)


![image](https://user-images.githubusercontent.com/58952369/180186646-6ec8f378-8c34-4e58-a75f-5fb3083acce1.png)


![image](https://user-images.githubusercontent.com/58952369/180186686-69bba0c9-8919-4ace-93f7-e918fe395aa1.png)





# Kaynakça 
https://www.geeksforgeeks.org 

https://stackoverflow.com 

https://github.com 

https://tutorial.djangogirls.org/tr/ 

https://www.djangoproject.com 

https://www.youtube.com
