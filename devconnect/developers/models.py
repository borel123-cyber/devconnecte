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