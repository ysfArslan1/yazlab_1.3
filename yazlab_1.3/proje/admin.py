
# Register your models here.
from django.contrib import admin
from .models import Proje # veya from post.models import Post
#from .models import  Proje 
"""

class ProjeAdmin(admin.ModelAdmin):
    list_display = ['proje_baslıgı', 'isim', 'donem']
    list_display_links = ['isim']
    list_filter = ['isim']
    search_fields = ['proje_baslıgı', 'isim']
    list_editable = ['proje_baslıgı']

    class Meta:
        model = Proje

 
"""


admin.site.register(Proje)

