"""
web URL Configuration
"""
from django.urls import re_path, include
from django.contrib import admin
from . import views


urlpatterns = [
    re_path(r'^$', views.index_redirect, name='index_redirect'),
    re_path(r'^crud/', include('crud.urls')),
    re_path(r'^admin/', admin.site.urls),
]
