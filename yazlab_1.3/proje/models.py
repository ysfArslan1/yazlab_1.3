from django.db import models
from django.urls import reverse


class Proje(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,verbose_name="yazar")
    isim = models.TextField()
    soy_isim = models.TextField()
    ogrenci_no = models.TextField()
    ogrenim_tur = models.TextField()
    ders_adi = models.TextField()
    proje_ozeti = models.TextField()
    proje_teslim_tarih = models.TextField()
    donem = models.TextField()
    proje_baslıgı = models.TextField()
    anahtar_kelimeler = models.TextField()
    danisman_bilgileri = models.TextField()
    juri_bilgileri = models.TextField()
    pdf = models.FileField(null=False, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('proje:index')


    

    def save(self, *args, **kwargs):
        #self.slug = self.get_unique_slug()
        return super(Proje, self).save(*args, **kwargs)


