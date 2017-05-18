import datetime

from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.views.generic import ListView

from product.models import Category, Product


# /products/
class CategoriesList(ListView):
    queryset = Category
    template_name = 'product/categories_list.html'  # name of template

    def get_context_data(self, **kwargs):
        message = ''  # info message
        # Call the base implementation first to get a context
        context = super(CategoriesList, self).get_context_data(**kwargs)
        if not self.queryset:
            message = 'No categories.'
        context['categories'] = self.queryset
        context['message'] = message
        return context


# /products/<category_slug>/
class CategoryDetail(DetailView):
    model = Category
    template_name = 'product/products_list.html'
    slug_url_kwarg = 'category_slug'

    def get_context_data(self, **kwargs):
        message = ''
        context = super(CategoryDetail, self).get_context_data(**kwargs)
        category = get_object_or_404(Category, slug=self.kwargs['category_slug'])  # get category by slug
        products = category.product_set.all()  # get all products of the category
        if not products:
            message = 'No products.'
        context['products'] = products
        context['message'] = message
        return context


# /products/<category_slug>/<product_slug>/
class ProductDetail(DetailView):
    model = Product
    template_name = 'product/product_detail.html'
    slug_url_kwarg = 'product_slug'

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        category = get_object_or_404(Category, slug=self.kwargs['category_slug'])
        try:
            product = category.product_set.get(request=self.kwargs['product_slug'])
        except Product.DoesNotExist:  # return 404 error if object not found
            raise Http404
        context['product'] = product
        return context


# /products/last/
class Last24List(ListView):
    model = Product
    template_name = 'product/last_24_hours.html'  # name of template

    def get_context_data(self, **kwargs):
        message = ''
        context = super(Last24List, self).get_context_data(**kwargs)

        date_past = datetime.datetime.now() - datetime.timedelta(
            hours=24)  # get products that created later than 24 hours ago
        products = Product.objects.filter(created_at__gte=date_past).order_by('-created_at')  # sorting by date created
        if not products:
            message = 'No products.'

        context['message'] = message
        context['products'] = products
        return context
