from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from .models import JobOffer,JobPost
from .forms import JobForm,PostForm
from django.urls import reverse
  

#Gestion des APIs
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import JobOfferSerializer

class CreerJobOfferAPIView(APIView):
    def post(self, request):
        serializer = JobOfferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    
# coté admin
from django.contrib.auth.decorators import login_required,user_passes_test

def est_administrateur(user):
    return user.is_superuser

# Create your views here.

def index(request):
    return render(request, 'Get_A_Job/index.html')
    
def job_list(request):
    jobs = JobOffer.objects.all()
    
    return render(request, 'Get_A_Job/job_list.html', {'jobs': jobs})

@login_required
@user_passes_test(est_administrateur)
def create_job(request):
    if request.method == 'POST':
           form = JobForm(request.POST)
           if form.is_valid():
               form.save()
           return redirect('/')
    else:
           form = JobForm()
           
    return render(request, 'Get_A_Job/create_job.html',{'form': form})

@login_required
@user_passes_test(est_administrateur)
def update_job(request,job_titre):
    job = JobOffer.objects.get(titre= job_titre)
    if request.method == 'POST':
        form = JobForm(request.POST,instance = job)
        if form.is_valid():
            #Recuperation des infos du form
               titre = form.cleaned_data['titre']
               nom_entreprise = form.cleaned_data['nom_entreprise']
               lieu = form.cleaned_data['lieu']
               description = form.cleaned_data['description']
               deja_pris = form.cleaned_data['deja_pris']
               email = form.cleaned_data['email']
               remuneration = form.cleaned_data['remuneration']
               profile = form.cleaned_data['profile']
            #    Suppression de l'ancien
               get_object_or_404(JobOffer,titre = job.titre).delete()
              
               job = JobOffer(titre=titre,nom_entreprise=nom_entreprise,email=email,lieu=lieu,deja_pris=deja_pris,description=description,remuneration=remuneration,profile=profile)
               
               job.save()
               return redirect('job-list')
    else:
        form = JobForm(instance = job)
        return render(request, 'Get_A_Job/update_job.html', {'form': form , 'job': job})
   

@user_passes_test(est_administrateur)
@login_required
def delete_job(request, job_titre):
    job = get_object_or_404(JobOffer,titre=job_titre)
    if request.method == 'POST':
        #Suppression si la confirmation est recue
        job.delete()
        return HttpResponseRedirect(reverse('job-list')) #Rediriger vers l'acceuil
    return render(request, 'Get_A_Job/delete_job.html', {'job':job})


def postuler_job(request,job_id):
    
    if request.method == 'POST':
        print('oui')
        # Formulaire de candidature
        form = PostForm(request.POST)
        if form.is_valid():
            form.save(using='users')
            # Récupération des données du formulaire
            nom = request.POST.get('nom')
            email = request.POST.get('email')
            cv = request.POST.get('cv')
            
            # Envoyer l'email à l'entreprise
            sujet_entreprise = 'Nouvelle candidature reçue'
            message_entreprise = f'Une nouvelle candidature a été soumis.\n\n Nom:{nom}\nE-mail:{email}\n CV : {cv}'
            send_mail(sujet_entreprise,message_entreprise,settings.EMAIL_HOST_USER,[settings.SUPERUSER_EMAIL])
            
            # Envoyer un message de réception au postulant
            
            sujet_utilisateur = 'Confirmation de candidature'
            message_utilisateur = 'Merci d\'avoir postulé à notre offre. Nous vous contacterons bientot.'
            send_mail(sujet_utilisateur,message_utilisateur,settings.EMAIL_HOST_USER,[email])
            
        return JsonResponse({'message':'Candidature envoyée avec succès !!'})
    else:
        print('non')
        offre = get_object_or_404(JobOffer, id = job_id)
        form = PostForm()
    posts = JobPost.objects.all() 
    return render(request, 'Get_A_Job/job_post.html',{'form': form,'posts':posts,'offre': offre})

def Action_admin(request):
    return render(request, 'Get_A_Job/admin.html')

def select_offre(request,objet):
    offres =JobOffer.objects.all()
    return render(request, 'Get_A_Job/select_offre.html', {'offres':offres, 'objet':objet})

def handler(request):
    return render(request, 'Get_A_Job/erreur_admin.html')