from django import forms
from .models import JobOffer,JobPost,MyModel
from django.contrib.auth.models import User

class JobForm(forms.ModelForm):
   class Meta:
        model = JobOffer
        fields = ['titre','nom_entreprise','nom','lieu','email','description','remuneration','profile','deja_pris']
    
   def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['titre'].widget.attrs['placeholder'] = "Titre de l'offre"
        self.fields['nom_entreprise'].widget.attrs['placeholder'] = "Nom de l'entreprise"
        self.fields['nom'].widget.attrs['placeholder'] = "Username"

        self.fields['lieu'].widget.attrs['placeholder'] = "Lieu"
        self.fields['description'].widget.attrs['placeholder'] = "Description de l'offre"
        self.fields['email'].widget.attrs['placeholder'] = "Adresse Email de l'entreprise"
        self.fields['remuneration'].widget.attrs['placeholder'] = "remuneration de l'employé"
        self.fields['profile'].widget.attrs['placeholder'] = "Profil recherché"
        
class PostForm(forms.ModelForm):
     class Meta:
          model = JobPost
          fields = ['nom','email','cv']
          
     def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nom'].widget.attrs['placeholder'] = "Votre Nom"
        self.fields['email'].widget.attrs['placeholder'] = "Votre adresse Email "
        self.fields['cv'].widget.attrs['accept'] = ".pdf"
     
class MyForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['nom','email','password']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nom'].widget.attrs['placeholder'] = "Votre Nom"
        self.fields['email'].widget.attrs['placeholder'] = "Votre adresse email"
        # self.fields['matricule'].widget.attrs['placeholder'] = "Votre matricule"
        self.fields['password'].widget.attrs['placeholder'] = "Votre mot de passe"
        
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    # Ajoutez des champs supplémentaires si nécessaire

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2','email']