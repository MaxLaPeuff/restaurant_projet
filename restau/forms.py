from django import forms
from.models import Commande

class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = ['nom', 'numero_telephone', 'adresse_email',
                  'adresse', 'menu_commande', 'nombre_de_plats']