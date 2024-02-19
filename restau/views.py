from django.shortcuts import render
from .models import Repas, Commande

def accueil(request):
    return render(request, 'restau/index.html')

def menu(request):
    repas = Repas.objects.all()
    return render(request, 'restau/menu.html', {'repas': repas})

def confirmation(request):
    return render(request,'restau/confirmation.html')

def commander(request):
    repas_dispo=Repas.objects.all()
    if request.method=="POST":
        nom=request.POST.get('nom')
        numero_telephone=request.POST.get('numero_telephone')
        adresse_email=request.POST.get('adresse_email')
        adresse=request.POST.get('adresse')
        menu_commande=request.POST.get('menu_commande')
        nombre_de_plats=request.POST.get('nombre_de_plats')
        newCommande=Commande.objects.create(nom=nom,numero_telephone=numero_telephone,adresse_email=adresse_email,adresse=adresse,menu_commande=menu_commande,nombre_de_plats=nombre_de_plats)
        newCommande.save()

    return render(request, 'restau/index.html')