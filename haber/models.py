from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Kategori(models.Model):
    title=models.CharField(("Haber Kategori"), max_length=50)
    
    def __str__(self) -> str:
        return self.title



class Haber(models.Model):
    title=models.CharField(("Haber Başlık"), max_length=200)
    
    haberText=models.TextField(("Haber İçeriği"))
    haberText2=models.TextField(("Haber İçeriği2"))
    haberText3=models.TextField(("Haber İçeriği3"))
    haberResim=models.ImageField(("Haber Resmi"), upload_to=None, height_field=None, width_field=None, max_length=None)
    haberResim2=models.ImageField(("Haber Resmi2"), upload_to=None, height_field=None, width_field=None, max_length=None)
    haberResim3=models.ImageField(("Haber Resmi3"), upload_to=None, height_field=None, width_field=None, max_length=None)
    haberZamani=models.DateField(("Haber Paylaşım Zamanı"), auto_now=False, auto_now_add=True)
    haberSaati=models.TimeField(("haber saat"), auto_now=False, auto_now_add=False ,null=True,blank=True)
    haberSehir=models.CharField(("Haberin Şehiri"), max_length=50)
    haberKategori=models.ForeignKey(Kategori, verbose_name=("Haber Kategori"), on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self) -> str:
        return self.title
    
class Biyografi(models.Model):
    isim = models.CharField(("Ünlü İsmi"), max_length=50)
    resim = models.ImageField(("Ünlü Resim"), upload_to=None, height_field=None, width_field=None, max_length=None)
    dogumTarihi = models.DateField(("Doğum Tarihi"), auto_now=False, auto_now_add=False)
    dogumYeri = models.CharField(("Doğum Yeri"), max_length=50)
    meslek = models.CharField(("Meslek"), max_length=50)
    biyografi = RichTextField()
    unluKategori = models.ForeignKey(Kategori, verbose_name=("Ünlü Kategori"), on_delete=models.CASCADE,null=True,blank=True)
   
   
    def __str__(self) -> str:
        return self.isim

