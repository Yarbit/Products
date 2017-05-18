from django.conf.urls import url, include
from django.contrib import admin

from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from Products.views import PageNotFound, ServerError
from . import views

handler404 = PageNotFound.as_view()
handler505 = ServerError.as_view()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^accounts/logout/$', auth_views.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'^accounts/register/$', views.Register.as_view(), name='register'),
    url(r'^$', TemplateView.as_view(template_name = 'index.html'), name='index'),
    url(r'^products/', include('product.urls')),
]
