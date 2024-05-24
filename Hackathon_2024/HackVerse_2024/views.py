from django.shortcuts import render,redirect
from Get_A_Job_S1.forms import MyForm
from Get_A_Job_S1.models import MyModel
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model,login
from django.shortcuts import render, redirect
from Get_A_Job_S1.forms import UserRegistrationForm

@login_required
def index(request):
    user = User.objects.all()
    return render(request, 'HackVerse_2024/index.html',{'user':user})


def register(request):
    if request.method == 'POST':
           form = MyForm(request.POST)
           if form.is_valid():
               #Verifie si l'utilisateur est deja inscit
               if MyModel.objects.filter(matricule=form.cleaned_data['matricule'],
                                         nom = form.cleaned_data['nom'],
                                         classe = form.cleaned_data['classe'],
                                         password = form.cleaned_data['password']).exists() == False:
                    form.save()
           return redirect('/index')
            
    else:
           form = MyForm()
           
    return render(request, 'HackVerse_2024/RegisterChat.html',{'form': form})
    
    

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Crée un nouvel utilisateur dans la base de données
            
            login(request,user)
            return redirect('http://127.0.0.1:8000/index') 
    else:
        form = UserRegistrationForm()
    return render(request, 'HackVerse_2024/RegisterChat.html', {'form': form})

def ogin(request):
    
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # verification sil'utilisateur est deja enregistrer
            
            if User.objects.filter(username = form.cleaned_data['nom'] ).exists() == True:
                
                login(request,User.objects.get(username = form.cleaned_data['nom'] )) #il se connecte
                return redirect('http://127.0.0.1:8000/index') 
            else :
                return redirect('Chat_Fora_S2/erreur_user.html')
    else:
        
        form = MyForm()
    return render(request, 'HackVerse_2024/login.html', {'form': form})