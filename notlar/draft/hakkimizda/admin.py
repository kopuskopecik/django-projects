from django.contrib import admin
from .models import Iletisim

class IletisimAdmin(admin.ModelAdmin):
	
    list_display = ["isim", "email", "content"]
    search_fields = ["isim", "email", "content"]	
    
    class Meta:
        model = Iletisim

admin.site.register(Iletisim, IletisimAdmin)
