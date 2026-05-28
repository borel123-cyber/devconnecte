from django.shortcuts import render, redirect
from .models import Profil
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profil
from .forms import ProfilForm
from django.contrib import messages
from .forms import ProfilForm, CompetenceForm
from .models import Profil, Competence, NiveauCompetence
from django.db import IntegrityError

#cette fonction affiche la liste des developpeurs qui sont sur le site web avec un systeme de pagination
def liste_developpeurs(request):
    profils_list = Profil.objects.all().order_by('-date_creation')
    paginator = Paginator(profils_list, 10)  # 10 par page
    page_number = request.GET.get('page')
    profils = paginator.get_page(page_number)
    return render(request, 'developers/list.html', {'profils': profils})



@login_required
def home(request):
    return render(request, 'developers/home.html')

#vue pour rediriger la connexion
def google_login(request):
    return redirect('/accounts/google/login/')


@login_required
def modifier_profil(request):
    # Récupère ou crée le profil de l'utilisateur connecté
    profil, created = Profil.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfilForm(request.POST, request.FILES, instance=profil)
        if form.is_valid():
            form.save()
            return redirect('detail_profil', pk=profil.pk)
    else:
        form = ProfilForm(instance=profil)

    return render(request, 'developers/profil_form.html', {
        'form': form,
        'profil': profil
    })
    
@login_required
def gerer_competences(request):
    profil = Profil.objects.get_or_create(user=request.user)[0]
    competences = NiveauCompetence.objects.filter(profil=profil).select_related('competence')

    if request.method == 'POST':
        form = CompetenceForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['competence'].strip().lower()
            # Récupère ou crée la compétence (insensible à la casse)
            competence_obj, _ = Competence.objects.get_or_create(nom__iexact=nom, defaults={'nom': nom})
            niveau = form.cleaned_data['niveau']
            
            # Vérifie que la compétence n'est pas déjà associée
            if not NiveauCompetence.objects.filter(profil=profil, competence=competence_obj).exists():
                NiveauCompetence.objects.create(profil=profil, competence=competence_obj, niveau=niveau)
                messages.success(request, f"Compétence '{competence_obj.nom}' ajoutée.")
            else:
                messages.error(request, "Vous avez déjà cette compétence.")
            return redirect('gerer_competences')
    else:
        form = CompetenceForm()
    
    return render(request, 'developers/competences.html', {
        'form': form,
        'competences': competences
    })

@login_required
def retirer_competence(request, competence_id):
    profil = Profil.objects.get_or_create(user=request.user)[0]
    competence = get_object_or_404(Competence, id=competence_id)
    NiveauCompetence.objects.filter(profil=profil, competence=competence).delete()
    messages.success(request, f"Compétence '{competence.nom}' retirée.")
    return redirect('gerer_competences')
    
    
def liste_developpeurs(request):
    profils_list = Profil.objects.all().order_by('-date_creation')\
        .prefetch_related('competences__competence')  # Optimisation N+1
    paginator = Paginator(profils_list, 10)
    page_number = request.GET.get('page')
    profils = paginator.get_page(page_number)
    return render(request, 'developers/list.html', {'profils': profils})

def detail_profil(request, pk):
    profil = get_object_or_404(
        Profil.objects.prefetch_related('competences__competence'),
        pk=pk
    )
    return render(request, 'developers/detail.html', {'profil': profil})
