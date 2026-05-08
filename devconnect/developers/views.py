from django.shortcuts import render
from .models import Profil
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

#cette fonction affiche la liste des developpeurs qui sont sur le site web avec un systeme de pagination
def liste_developpeurs(request):
    profils_list = Profil.objects.all().order_by('-date_creation')
    paginator = Paginator(profils_list, 10)  # 10 par page
    page_number = request.GET.get('page')
    profils = paginator.get_page(page_number)
    return render(request, 'developers/list.html', {'profils': profils})


def detail_profil(request, pk):
    profil = get_object_or_404(Profil, pk=pk)
    return render(request, 'developers/detail.html', {'profil': profil})