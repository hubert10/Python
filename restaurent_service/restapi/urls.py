
from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('restapi/(?P<version>(v1|v2))/', include('restaurent.urls'))
]