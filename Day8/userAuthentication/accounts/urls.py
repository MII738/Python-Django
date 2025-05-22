from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('shopping/', views.shopping_view, name='shopping'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
