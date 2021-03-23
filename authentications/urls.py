from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_view, name='register'),
    path('edit/register/', views.edit_register_view, name='edit_register'),
    path('change/password/', views.change_password_view, name='change_password'),
]