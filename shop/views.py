from django.shortcuts import render, get_object_or_404
from .models import Category, Product, HomeSlides
from cart.cart import Cart


#Index
def index(request):
    cart = Cart(request)
    products = Product.objects.all()
    slides = HomeSlides.objects.all()
    sales = products.filter(is_on_sale=True)
    bestsellers = products.filter(is_best_seller=True)
    return render(request, 'shop/index.html', {'cart':cart, 'slides':slides, 'sales':sales, 'bestsellers': bestsellers})

#List of available products, optional category filter
def product_list(request, category_slug=None):
    cart = Cart(request)
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,'shop/catalog/grid.html', {'category': category, 'cart':cart, 'categories': categories, 'products':products, })


#Single product view
def product_detail(request, id, slug):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    products = Product.objects.all()
    category = product.category
    prods = products.filter(category=category)
    sales = products.filter(is_on_sale=True)
    bestsellers = products.filter(is_best_seller=True)
    return render(request, 'shop/catalog/detail.html', {'products':products, 'cart':cart, 'product': product, 'prods':prods, 'sales':sales, 'bestsellers':bestsellers })

#About Us
def about(request):
    cart = Cart(request)
    context={'cart':cart}
    return render(request, 'shop/about.html', context)

#Contact
def contact(request):
    cart = Cart(request)
    context={'cart':cart}
    return render(request, 'shop/contact.html', context)
