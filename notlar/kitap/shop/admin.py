from django.contrib import admin
from .models import Category, Product

class ProductInline(admin.StackedInline):
	model = Product

class CategoryAdmin(admin.ModelAdmin):
	inlines = [
		ProductInline,
		]
		
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ('name',)}
	list_filter = ['name', ]





class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available']
    list_filter = ['available']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

