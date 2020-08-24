from django.contrib import admin
from .models import Lesson

class LessonAdmin(admin.ModelAdmin):
	
    #list_display = ["headline", "number", "filtre1", "filtre2", "publishing_date","slug"]
    list_display = ["headline", "number", "descriptions", "anahtar"]
    search_fields = ["headline", "content"]
    #list_editable = ["number", "filtre1", "filtre2"]	
    list_editable = ["number", "descriptions", "anahtar"]	    
    class Meta:
        model = Lesson

admin.site.register(Lesson, LessonAdmin)
