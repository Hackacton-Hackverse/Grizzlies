from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Conversation, Message
from .forms import ConversationForm,MessageForm

# Create your views here.
@login_required
def conversation_list(request):
    conversations = Conversation.objects.filter(participants=request.user)
    return render(request, 'Chat_Fora_S2/Acceuil.html', {'conversations': conversations})


@login_required
def conversation_detail(request, conversation_id):
    conversation = Conversation.objects.get(id=conversation_id)
    messages = Message.objects.filter(conversation=conversation)
    return render(request, 'Chat_Fora_S2/conversation_detail.html', {'conversation': conversation, 'messages': messages})

def messagerie(request,conversation_id):
    conversation = Conversation.objects.get(id=conversation_id)
    messages = Message.objects.filter(conversation=conversation)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
           
            message = Message.objects.create(conversation = conversation,user = request.user,content = content)
            
            return redirect('messagerie',conversation_id)
    else :
        form = MessageForm()
    
    return render(request, 'Chat_Fora_S2/messagerie.html', {'form': form ,'conversation':conversation ,'messages': messages})

def create_conversation(request):
    if request.method == 'POST':
        form = ConversationForm(request.POST)
        if form.is_valid():
            conversation = form.save()
            
            return redirect('messagerie',conversation.id)
    else :
        form = ConversationForm()
    
    return render(request, 'Chat_Fora_S2/create_conversation.html' ,{'form':form})

def start_conversation(request,other_user_id):
    #Verification si l'utilisateur est authentifié
    if request.user.is_authenticated:
        #Obtenir l'utilisateur actuel et l'utilisateur cible
        current_user = request.user
        other_user = User.objects.get(id=other_user_id)
        
        #Creation d'une nouvelle instance de modele Conversation
        conversation = Conversation.objects.create()
        
        #Ajout des participants a la conversation 
        conversation.participants.add(current_user,other_user)
        
        #Redirection de l'utilisateur vers la page de messagerie
        return redirect('conversation_detail',conversation.id)
    else:
        return redirect('login')
    
def send_message(request,conversation_id):
    conversation = Conversation.objects.get(id=conversation_id)
    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
           
            message = Message.objects.create(conversation = conversation,user = request.user,content = content)
            
            return redirect('conversation_detail',conversation_id)
    else :
        form = MessageForm()
    
    return render(request, 'Chat_Fora_S2/envoyer_message.html', {'form': form ,'conversation':conversation})