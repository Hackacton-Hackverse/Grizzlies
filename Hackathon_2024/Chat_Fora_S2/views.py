from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Conversation, Message

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

def messagerie(request):
    return render(request, 'Chat_Fora_S2/messagerie.html')