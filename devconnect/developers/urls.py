from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_developpeurs, name='liste_developpeurs'),
    path('profil/<int:pk>/', views.detail_profil, name='detail_profil'),
    
]