from django.db import models
from django.contrib.auth.models import User

class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)#chaque profil correspond exactement a un utilisateur
    bio = models.TextField(blank=True)
    site_web = models.URLField(blank=True)
    photo = models.ImageField(upload_to='profils/', blank=True)
    disponible = models.BooleanField(default=False)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
class Competence(models.Model):
    nom = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nom


class NiveauCompetence(models.Model):
    NIVEAUX = [
        ('DEBUTANT', 'Débutant'),
        ('INTERMEDIAIRE', 'Intermédiaire'),
        ('AVANCE', 'Avancé'),
    ]
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name='competences')
    competence = models.ForeignKey(Competence, on_delete=models.CASCADE)
    niveau = models.CharField(max_length=20, choices=NIVEAUX, default='DEBUTANT')

    class Meta:
        unique_together = ['profil', 'competence']  # Un même développeur ne peut pas ajouter deux fois la même compétence

    def __str__(self):
        return f"{self.profil.user.username} - {self.competence.nom} ({self.get_niveau_display()})"