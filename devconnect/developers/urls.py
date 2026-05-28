from django.urls import path
from . import views
# ajout de l'url de redirection vers allauth
from django.urls import path, include
from allauth.socialaccount.views import signup

urlpatterns = [
    path('', views.liste_developpeurs, name='liste_developpeurs'),
    path('profil/<int:pk>/', views.detail_profil, name='detail_profil'),
    path('home/', views.home, name='home'),
    path('google/login/', views.google_login, name='google_login'),
    path('profil/modifier/', views.modifier_profil, name='modifier_profil'),
    path('competences/', views.gerer_competences, name='gerer_competences'),
    path('competences/retirer/<int:competence_id>/', views.retirer_competence, name='retirer_competence'),
]