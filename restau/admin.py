from django.contrib import admin
from.models import Repas,Commande
# Register your models here.

class RepasAdmin(admin.ModelAdmin):
    list_display = ("name","prix","slug","description")

class CommandeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'numero_telephone', 'adresse_email', 'adresse', 'menu_commande', 'nombre_de_plats')

admin.site.register(Repas,RepasAdmin)
admin.site.register(Commande,CommandeAdmin)