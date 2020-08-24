from django.contrib import admin
from .models import Article, Teacher, Student, Sinif, Kitap, Etkinlik, Author, Entry, TaggedItem, Model1, Model2
from .forms import ArticleForm
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

from django.contrib.admin import AdminSite

class MyAdminSite(AdminSite):
	site_header = 'Monty Python administration'
admin_site = MyAdminSite(name='myadmin')


class EtkinlikAdmin(admin.ModelAdmin):
	#autocomplete_fields = ['ogretmen']
	def save_model(self, request, obj, form, change):
		obj.ogretmen = Teacher.objects.first()
		print("CHANGEEEEEEEEEEEEEEEEEEEEEE")
		print(change)
		super().save_model(request, obj, form, change)

class TeacherAdmin(admin.ModelAdmin):
	ordering = ['isim']
	search_fields = ['isim']
	
class StudentAdmin(admin.ModelAdmin):
	raw_id_fields = ('teacher',)
	readonly_fields = ('bireysel_odulu',)
	search_fields = ['isim']

class SinifAdmin(admin.ModelAdmin):
	pass
	

	
class KitapAdmin(admin.ModelAdmin):
	
	def save_model(self, request, obj, form, change):
		obj.user = request.user
		super().save_model(request, obj, form, change)

#def make_published(modeladmin, request, queryset):
#	print("")
#	print(modeladmin)
#	print("")
#	print(request)
#	print("")
#	print(queryset)
#	print("")
#	queryset.update(status='p')
#	modeladmin.message_user(request, "elemanlar başarıyla published yapıldı")
#make_published.short_description = "Seçilen elemanları status'lerini 'published' yap"

def export_as_json(modeladmin, request, queryset):
	response = HttpResponse(content_type="application/json")
	serializers.serialize("json", queryset, stream=response)
	return response

def upper1_case_name(obj):
	return ("%s %s" % (obj.name, obj.status)).upper()
upper1_case_name.short_description = 'Name'

class ArticleAdmin(admin.ModelAdmin):
	date_hierarchy = 'publishing_date'
	list_display = ['name', 'status', upper1_case_name, 'author_first_name', "full_name"]
	list_display_links = ['status',]
	actions = ['make_published']
	actions_on_bottom = True
	list_editable = ['name']
	#list_filter = ["user__username", ('user__is_staff', admin.BooleanFieldListFilter),('user', admin.RelatedOnlyFieldListFilter),]
	prepopulated_fields = {"slug": ("name",)}
	#ordering = ['-publishing_date']
	#actions_selection_counter = False
	#exclude = ('status',)
	#fields = (('status', 'name'), 'publishing_date')
	#fieldsets = (
	#	(None, {
	#		'fields': ('status', 'name'),
	#		'description': "Merhaba"
	#	}),
	#	('Advanced options', {
	#		'classes': ('collapse',),
	#		'fields': ('publishing_date',),
	#	}),
	#)
	#form = ArticleFormdef save_model(self, request, obj, form, change):
	
	#def get_form(self, request, obj=None, **kwargs):
	#	if request.user.is_superuser:
	#		kwargs['form'] = ArticleForm
	#	return super().get_form(request, obj, **kwargs)
	def get_changelist_form(self, request, **kwargs):
		return ArticleForm
	
	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		print("DB FIELDDD")
		print(db_field)
		if db_field.name == "user":
			kwargs["queryset"] = User.objects.filter(username="sahinturk")
		return super().formfield_for_foreignkey(db_field, request, **kwargs)
		
	
	def save_model(self, request, obj, form, change):
		print("")
		print(self.get_urls())
		obj.ogretmen = Teacher.objects.first()
		print("CHANGEEEEEEEEEEEEEEEEEEEEEE")
		print(change)
		super().save_model(request, obj, form, change)
	
	
	
	def save_formset(self, request, form, formset, change):
		print("")
		print("")
		print(form)
		print("")
		print("")
		print(formset)
		instances = formset.save(commit=False)
		for obj in formset.deleted_objects:
			obj.delete()
		for instance in instances:
			instance.user = request.user
			instance.save()
		formset.save_m2m()
	
	def author_first_name(self, obj):
		return obj.name
	author_first_name.admin_order_field = 'publishing_date'

	
	def make_published(self, request, queryset):
		print("")
		print(self)
		print("")
		print(request)
		print("")
		print(queryset)
		print("")
		queryset.update(status='p')
		self.message_user(request, "elemanlar başarıyla published yapıldı")
		response = HttpResponse(content_type="application/json")
		serializers.serialize("json", queryset, stream=response)
		return response
	make_published.short_description = "Seçilen elemanları status'lerini 'published' yap"


from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import gettext_lazy as _
# Define a new FlatPageAdmin
class FlatPageAdmin(FlatPageAdmin):
	fieldsets = (
		(None, {'fields': ('url', 'title', 'content', 'sites')}),
		(_('Advanced options'), {
			'classes': ('collapse', ),
			'fields': (
			'enable_comments',
			'registration_required',
			'template_name',
		),
		}),
	)	
	

class Model2Admin(admin.ModelAdmin):
	list_display = ["isim","number",]
	list_editable = ["number"]
	
	
	
	
	
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
admin.site.register(TaggedItem)
admin.site.register(Article, ArticleAdmin)
#admin.site.add_action(export_as_json, "json gönder")
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Sinif, SinifAdmin)
admin.site.register(Etkinlik, EtkinlikAdmin)
admin.site.register(Kitap, KitapAdmin)
#admin.site.register(Author, AuthorAdmin)
#admin_site.register(Article, ArticleAdmin)
admin.site.register(Model1)
admin.site.register(Model2, Model2Admin)
admin.site.register(Author)
admin.site.register(Entry)
#admin.site.register(Book, BookAdmin)
#admin.site.disable_action('delete_selected')