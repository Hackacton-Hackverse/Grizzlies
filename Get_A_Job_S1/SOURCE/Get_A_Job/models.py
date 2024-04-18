from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
"""
class CustomUser(AbstractUser):
     is_admin = models.BooleanField(default=False)
    
     def __str__(self):
         return self.username
"""    
class JobOffer(models.Model):
    """gestion des offres d'emploi

    """
    titre = models.CharField(max_length=100)
    nom_entreprise = models.CharField(max_length=100)
    lieu = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    deja_pris = models.BooleanField(default=False)
    email = models.EmailField(max_length=100)
    remuneration = models.TextField(max_length=150)
    profile = models.TextField(max_length=150)
    
    
    def __str__(self):
        return self.titre
    
        
class JobPost(models.Model):
    """Gestion de l'envoie des candidatures 

    """
    nom = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    cv = models.FileField()
    
    def __str__(self):
        return self.nom
    
    """ class Meta:
        using = 'Candidatures_db'"""