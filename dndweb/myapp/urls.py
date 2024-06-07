from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('armor/', views.armor_list, name='armor_list'),
    path('characters/', views.characters, name='characters'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('profile/', views.userProfile, name='profile'),
    path('profile/update/', views.update_profile, name='profile_update'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)