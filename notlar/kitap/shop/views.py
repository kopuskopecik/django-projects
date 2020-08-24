from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm


def product_list(request):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    context = {
        'categories': categories,
        'products': products
    }
    return render(request, 'shop/product/list.html', context)
	
def category_product_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    categories = Category.objects.all().exclude(slug = category_slug)

    context = {
        'category': category,
        'products': products,
		'categories': categories
    }
    return render(request, 'shop/product/category_detail.html', context)



def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'form': cart_product_form
    }
    return render(request, 'shop/product/detail.html', context)

