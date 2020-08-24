from django.contrib import admin
from .models import Lesson, Topic

class LessonAdmin(admin.ModelAdmin):
	
    list_display = ["headline", "number", "filtre1", "filtre2", "baslık", "aktif","publishing_date","slug"]
    search_fields = ["headline", "content"]
    list_editable = ["number", "filtre1", "filtre2", "aktif"]	
    
    class Meta:
        model = Lesson

class TopicAdmin(admin.ModelAdmin):
	
    list_display = ["baslik_adi", "slug", "modul_mu", "icon_name", "sıra", "aktif"]
    list_editable = ["slug", "modul_mu", "icon_name", "sıra", "aktif"]	
    
    class Meta:
        model = Topic

admin.site.register(Lesson, LessonAdmin)
admin.site.register(Topic, TopicAdmin)