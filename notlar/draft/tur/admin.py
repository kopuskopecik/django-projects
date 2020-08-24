from django.contrib import admin
from .models import Dersler

class DerslerAdmin(admin.ModelAdmin):
	
    list_display = ["headline", "number", "filtre1", "filtre2", "publishing_date"]
    search_fields = ["headline", "content"]
    list_editable = ["number", "filtre1", "filtre2"]	
    
    class Meta:
        model = Dersler

admin.site.register(Dersler, DerslerAdmin)
