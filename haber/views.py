from django.shortcuts import render
from.models import *
# Create your views here.

# !index 
def index(request):
    haber=Haber.objects.all().order_by('-id')[:11]
    kategori=Kategori.objects.all()
    spor=Haber.objects.filter(haberKategori=2).order_by('-id')[:2]
    ekonomi=Haber.objects.filter(haberKategori=3).order_by('-id')[:2]
    magazin=Haber.objects.filter(haberKategori=4).order_by('-id')[:2]
    dünya=Haber.objects.filter(haberKategori=5).order_by('-id')[:2]
    teknoloji=Haber.objects.filter(haberKategori=6).order_by('-id')[:2]
    oyun=Haber.objects.filter(haberKategori=7).order_by('-id')[:2]
    sondakika = Haber.objects.filter(haberKategori = 1).order_by('-id')[:1]
    
    context={
        'haber':haber,
        'kategori':kategori,
        'ekonomi':ekonomi,
        'magazin':magazin,
        'dünya':dünya,
        'teknoloji':teknoloji,
        'oyun':oyun,
        'spor':spor,
        'sondakika': sondakika
        
    }
    return render(request,'index.html',context)

#!detay
def detay(request, id):
    haber=Haber.objects.get(id=id)
    haber2 = Haber.objects.all().order_by('?')[:5]
    kategori=Kategori.objects.all()
    context={
        'haber':haber,
        'kategori':kategori,
        'haber2': haber2
    }
    return render(request,'detay.html',context)

#! Son Dakika
def sondakika(request):
    sondakika=Haber.objects.filter(haberKategori=1).order_by('-id')
    haber2 = Haber.objects.all().order_by('?')[:5]
    context={
        'sondakika':sondakika,
        'haber2': haber2
    }
    return render(request,'sondakika.html',context)
    
#! Spor
def spor(request):
    spor=Haber.objects.filter(haberKategori=2).order_by('-id')
    context={
        'spor':spor
    }
    return render(request,'spor.html',context)

#! Ekonomi
def ekonomi(request):
    ekonomi=Haber.objects.filter(haberKategori=3).order_by('-id')
    ekonomiMarquee=Haber.objects.filter(haberKategori=3).order_by('-id')[:1]
    
    context = {
        'ekonomi':ekonomi,
        'ekonomiMarquee':ekonomiMarquee
    }
    
    return render(request,'ekonomi.html', context)

#! Magazin
def magazin(request):
    unlu = Biyografi.objects.all()
    magazin=Haber.objects.filter(haberKategori=4).order_by('-id')
    magazinMarquee=Haber.objects.filter(haberKategori=4).order_by('-id')[:1]
    
    context = {
        'unlu' : unlu,
        'magazin':magazin,
        'magazinMarquee':magazinMarquee
    }
    return render(request,'magazin.html', context)

#! Dünya
def dunya(request):
    dünya=Haber.objects.filter(haberKategori=5).order_by('-id')
    
    context = {
        'dünya': dünya
    }
    return render(request,'dünya.html', context)

#! Teknoloji
def teknoloji(request):
    teknoloji=Haber.objects.filter(haberKategori=6).order_by('-id')
    teknolojiMarquee=Haber.objects.filter(haberKategori=6).order_by('-id')[:1]
    
    context = {
        'teknoloji': teknoloji,
        'teknolojiMarquee': teknolojiMarquee
    }
    return render(request,'teknoloji.html', context)

#! Oyun
def oyun(request):
    oyun=Haber.objects.filter(haberKategori=7).order_by('-id')
    espor=Haber.objects.filter(haberKategori=7).order_by('-id')[:1]
    biyografi = Biyografi.objects.all()
    
    context = {
        'oyun': oyun,
        'espor': espor,
        'biyografi':biyografi,
    }
    return render(request,'oyun.html',context)

#! Profil
def profil(request,id):
    biyografi=Biyografi.objects.get(id=id)
    unluKategori = Biyografi.objects.all()
    
    
    context = {
        'biyografi' : biyografi,
        'unluKategori':unluKategori,
    }
    
    
    return render(request,'profil.html',context)
    
#! İletişim
def iletisim(request):
    return render(request, 'iletisim.html')