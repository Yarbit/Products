from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.categories_list, name='categories_list'),
    url(r'^last/$', views.last_24_hours, name='last_24_hours'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.category_detail, name='category_detail'),
    url(r'^(?P<category_slug>[-\w]+)/(?P<product_slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]
