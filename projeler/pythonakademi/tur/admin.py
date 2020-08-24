from django.contrib import admin
from .models import Dersler, Baslik

class DerslerAdmin(admin.ModelAdmin):
	
    list_display = ["headline", "number", "filtre1", "baslık",'aktif', "filtre2", "publishing_date", ]
    search_fields = ["headline", "content"]
    list_editable = ["number", "filtre1", "baslık", "filtre2", "aktif"]	
    
    class Meta:
        model = Dersler

class BaslikAdmin(admin.ModelAdmin):
	
    list_display = ["baslik_adi", "slug", "modul_mu", "icon_name", "aktif"]
    list_editable = ["slug", "modul_mu", "icon_name", "aktif"]	
    
    class Meta:
        model = Baslik

admin.site.register(Dersler, DerslerAdmin)
admin.site.register(Baslik, BaslikAdmin)
