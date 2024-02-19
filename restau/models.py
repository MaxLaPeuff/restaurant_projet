from django.db import models
# Create your models here.
class Repas(models.Model):
    name=models.CharField(max_length=255)
    prix=models.FloatField()
    slug=models.SlugField()
    description=models.TextField()
    image=models.ImageField(upload_to='media')

    def __int__(self):
        return self.name

class Commande(models.Model):
    nom = models.CharField(max_length=255)
    numero_telephone = models.CharField(max_length=15 )
    adresse_email = models.EmailField()
    adresse = models.TextField()
    menu_commande = models.CharField(max_length=255)
    nombre_de_plats = models.IntegerField()

    def __str__(self):
        return f"Commande de {self.nom}"
