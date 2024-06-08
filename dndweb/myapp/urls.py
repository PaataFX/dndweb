from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('armor/', views.armor_list, name='armor_list'),
    path('character/', views.characters, name='characters'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('profile/', views.userProfile, name='profile'),
    path('profile/update/', views.update_profile, name='profile_update'),  # Correct view function name
    path('characters/', views.character_list, name='character_list'),
    path('characters/<int:character_id>/', views.character_detail, name='character_detail'),
    path('create_character/', views.create_character, name='create_character'),
    path('character/<int:character_id>/', views.character_detail, name='character_detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
