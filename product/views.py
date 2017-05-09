import datetime

from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from product.models import Category, Product


# /products/
def categories_list(request):
    message = ''  # information message
    categories = Category.objects.all()
    if not categories:
        message = 'No categories.'
    return render(request, 'product/categories_list.html', locals())


# /products/<category_slug>/
def category_detail(request, category_slug):
    message = ''
    category = get_object_or_404(Category, slug=category_slug)
    products = category.product_set.all()
    if not products:
        message = 'No products.'
    return render(request, 'product/products_list.html', {'products': products, 'message': message})


# /products/<category_slug>/<product_slug>/
def product_detail(request, category_slug, product_slug):
    category = get_object_or_404(Category, slug=category_slug)
    try:
        product = category.product_set.get(slug=product_slug)
    except Product.DoesNotExist:  # return 404 error if object not found
        raise Http404
    return render(request, 'product/product_detail.html', {'product': product})


# /products/last/
@login_required
def last_24_hours(request):
    message = ''
    date_past = datetime.datetime.now() - datetime.timedelta(hours=24)
    # get products that created later than 24 hours ago
    products = Product.objects.filter(created_at__gte=date_past).order_by('-created_at')
    if not products:
        message = 'No products.'
    return render(request, 'product/last_24_hours.html', {'products': products, 'message': message})
