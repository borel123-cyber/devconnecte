from django import forms
from .models import Profil

class ProfilForm(forms.ModelForm):
    class Meta:
        model = Profil
        fields = ['bio', 'site_web', 'photo', 'disponible']
        widgets = {
            'bio': forms.Textarea(attrs={
                'rows': 4,
                'class': 'w-full border rounded px-3 py-2',
                'placeholder': 'Parlez-nous de vous...'
            }),
            'site_web': forms.URLInput(attrs={
                'class': 'w-full border rounded px-3 py-2',
                'placeholder': 'https://votresite.com'
            }),
            'photo': forms.FileInput(attrs={
                'class': 'w-full border rounded px-3 py-2'
            }),
            'disponible': forms.CheckboxInput(attrs={
                'class': 'mr-2'
            }),
        }
        labels = {
            'bio': 'Biographie',
            'site_web': 'Site web',
            'photo': 'Photo de profil',
            'disponible': 'Disponible pour des missions',
        }
        
class CompetenceForm(forms.Form):
    NIVEAUX = [
        ('DEBUTANT', 'Débutant'),
        ('INTERMEDIAIRE', 'Intermédiaire'),
        ('AVANCE', 'Avancé'),
    ]
    competence = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'w-full border rounded px-3 py-2',
            'placeholder': 'ex: Python, React, Docker...'
        }),
        label='Compétence'
    )
    niveau = forms.ChoiceField(
        choices=NIVEAUX,
        widget=forms.Select(attrs={'class': 'w-full border rounded px-3 py-2'}),
        label='Niveau'
    )