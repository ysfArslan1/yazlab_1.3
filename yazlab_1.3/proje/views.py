from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404
from .models import Proje
from .forms import ProjeForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from PdfDonusturucu import donustur



def proje_index(request):
    if request.user.id==1:
        proje_list = Proje.objects.all()
    else:
        proje_list = Proje.objects.filter(author_id=request.user.id)

    query = request.GET.get('q')
    if query:
      
            proje_list = proje_list.filter(
            Q(isim__icontains=query) |
            Q(ders_adi__icontains=query)|
            Q(proje_baslıgı__icontains=query) |
            Q(anahtar_kelimeler__icontains=query) |
            Q(donem__icontains=query) 

        ).distinct()
        

    paginator = Paginator(proje_list, 20)  # Show 5 contacts per page

    page = request.GET.get('page')
    try:
        projes = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        projes = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        projes = paginator.page(paginator.num_pages)
    
    return render(request, "proje/index.html", {'projes': projes})




def proje_create(request):
    
    if not request.user.is_authenticated:
        # Eğer kullanıcı giriş yapmamış ise hata sayfası gönder
        return Http404()

    form = ProjeForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        
        proje = form.save(commit=False)
        proje.user = request.user
        proje.author_id=request.user.id
        proje.save()
        list=donustur(proje.pdf.path)
        proje.isim=list[0]
        proje.soy_isim=list[1]
        proje.ogrenci_no=list[2]
        proje.ogrenim_tur=list[3]
        proje.ders_adi=list[4]
        proje.proje_ozeti=list[5]
        proje.proje_teslim_tarih=list[6]
        proje.donem=list[7]
        proje.proje_baslıgı=list[8]
        proje.anahtar_kelimeler=list[9]
        proje.danisman_bilgileri=list[10]
        proje.juri_bilgileri=list[11]

        proje.save()
        #print( donustur(post.image.path))
        messages.success(request, "Başarılı bir şekilde oluşturdunuz.", extra_tags='mesaj-basarili')
        return HttpResponseRedirect(proje.get_absolute_url())

    context = {
        'form': form
    }

    return render(request, "proje/form.html", context)



















