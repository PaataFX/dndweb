from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('armor/', views.armor_list, name='armor_list'),
    path('characters/', views.characters, name='characters'),
    path('login/', views.login, name='login'),
    # Add more paths as needed...
]
