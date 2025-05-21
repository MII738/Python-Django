from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^departments$', views.departmentApi),
    re_path(r'^department/(?P<id>[0-9]+)$', views.departmentApi),
]
