from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Conversation, Message,ConversationOO
from .forms import ConversationForm,MessageForm,ConversationFormOO

# Create your views here.
def index(request):
    return render(request, 'Chat_Fora_S2/RegisterChat.html')
@login_required
def conversation_list(request):
    conversations = Conversation.objects.filter(participants = request.user)
    # conversations.delete()
    return render(request, 'Chat_Fora_S2/Acceuil.html', {'conversations': conversations})


@login_required
def conversation_detail(request, conversation_id):
    conversation = Conversation.objects.get(id=conversation_id)
    messages = Message.objects.filter(conversation=conversation)
    return render(request, 'Chat_Fora_S2/conversation_detail.html', {'conversation': conversation, 'messages': messages})

def messagerie(request,conversation_id):
    conversation = Conversation.objects.get(id=conversation_id)
    messages = Message.objects.filter(conversation=conversation)
    # messages.delete()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
           
            message = Message.objects.create(conversation = conversation,user = request.user,content = content)
            
    else :
        form = MessageForm()
    
    return render(request, 'Chat_Fora_S2/messagerie.html', {'form': form ,'conversation':conversation ,'messages': messages ,'user':request.user})

def create_conversation(request):
    conversations = Conversation.objects.filter(participants = request.user)
    users = User.objects.all()
    if request.method == 'POST':
        form = ConversationFormOO(request.POST)
        if form.is_valid():
            titre = form.cleaned_data['titre']
            current_user = request.user
            if User.objects.filter(username=form.cleaned_data['Username']).exists() == True:
                other_user = User.objects.get(username=form.cleaned_data['Username'])
                
                return redirect('start_conversation',titre,other_user)
            else:
                return render(request, 'Chat_Fora_S2/erreur_user.html')
        
    else :
        form = ConversationFormOO()
        return render(request, 'Chat_Fora_S2/create_conversation.html' ,{'form':form ,'users':users})
     
    return render(request, 'Chat_Fora_S2/Acceuil.html', {'conversations': conversations})

def start_conversation(request,titre,other_user_name):
    #Verification si l'utilisateur est authentifié
    if request.user.is_authenticated:
        #Obtenir l'utilisateur actuel et l'utilisateur cible
        current_user = request.user
        
        other_user = User.objects.get(username=other_user_name)
            
            #Creation d'une nouvelle instance de modele Conversation
        conversation = Conversation.objects.create(titre=titre)
            
            #Ajout des participants a la conversation 
        conversation.participants.add(current_user,other_user)
            
            #Redirection de l'utilisateur vers la page de messagerie
        return redirect('messagerie',conversation.id)
    
    else:
        return redirect('login')
    
    return redirect('Acceuil')

def add_participant(request,other_user_name):
    #Obtenir l'utilisateur actuel et l'utilisateur cible
    current_user = request.user
    conversation = Conversation.objects.filter(participants = request.user)
    if User.objects.filter(username=other_user_name).exists() == True:
        other_user = User.objects.get(username=other_user_name)
        conversation.participants.add(other_user)
    else:
        return render(request, 'Chat_Fora_S2/erreur_user.html')
    
    
    return render(request,'Chat_Fora_S2/add_part.html')
