from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_account, name='account'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
]
