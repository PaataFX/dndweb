from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('armor/', views.armor_list, name='armor_list'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('profile/', views.userProfile, name='profile'),
    path('profile/update/', views.update_profile, name='profile_update'),  # Correct view function name
    path('characters/', views.character_list, name='characters'),
    path('create_character/', views.create_character, name='create_character'),
    path('races/', views.races_page, name='races_page'),
    path('races/<int:race_id>/', views.race_detail, name='race_detail'),
    path('classes/', views.classes_page, name='classes_page'),
    path('classes/<int:class_id>/', views.class_detail, name='class_detail'),
    path('spells/', views.spells_page, name='spells_page'),
    path('character/<int:character_id>/', views.character_detail, name='character_detail'),
    path('character/<int:character_id>/delete/', views.delete_character, name='character_delete'),
    path('<int:spell_id>/', views.spell_detail, name='spell_detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
