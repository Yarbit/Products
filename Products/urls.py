
from django.conf.urls import url, include
from django.contrib import admin

from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^accounts/logout/$', auth_views.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'^accounts/register/$', views.register, name='register'),
    url(r'^$', views.index, name='index'),
    url(r'^products/', include('product.urls')),
]
