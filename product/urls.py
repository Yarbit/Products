from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    url(r'^$', views.CategoriesList.as_view(), name='categories_list'),
    url(r'^last/$', login_required(views.Last24List.as_view()), name='last_24_hours'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.CategoryDetail.as_view(), name='category_detail'),
    url(r'^(?P<category_slug>[-\w]+)/(?P<product_slug>[-\w]+)/$', views.ProductDetail.as_view(), name='product_detail'),
]
