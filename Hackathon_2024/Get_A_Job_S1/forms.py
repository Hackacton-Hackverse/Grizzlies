from django import forms
from .models import JobOffer,JobPost

class JobForm(forms.ModelForm):
   class Meta:
        model = JobOffer
        fields = ['titre','nom_entreprise','lieu','email','description','remuneration','profile','deja_pris']
    
   def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['titre'].widget.attrs['placeholder'] = "Titre de l'offre"
        self.fields['nom_entreprise'].widget.attrs['placeholder'] = "Nom de l'entreprise"
        self.fields['lieu'].widget.attrs['placeholder'] = "Lieu"
        self.fields['description'].widget.attrs['placeholder'] = "Description de l'offre"
        self.fields['email'].widget.attrs['placeholder'] = "Adresse Email de l'entreprise"
        self.fields['remuneration'].widget.attrs['placeholder'] = "remuneration de l'employé"
        self.fields['profile'].widget.attrs['placeholder'] = "Profil recherché"
        
class PostForm(forms.ModelForm):
     class Meta:
          model = JobPost
          fields = ['nom','email','cv']
          using = 'users'
          
     def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nom'].widget.attrs['placeholder'] = "Votre Nom"
        self.fields['email'].widget.attrs['placeholder'] = "Votre adresse Email "
        self.fields['cv'].widget.attrs['accept'] = ".pdf"
        