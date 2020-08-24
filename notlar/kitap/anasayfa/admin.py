from django.contrib import admin

from .models import Genel

class GenelAdmin(admin.ModelAdmin):
    list_display = ['başlık', 'image',]
    prepopulated_fields = {'slug': ('başlık',)}


admin.site.register(Genel, GenelAdmin)
