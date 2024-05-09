from django import forms
from .models import Conversation,Message,ConversationOO

class ConversationForm(forms.ModelForm):
    class Meta:
        model = Conversation
        fields = ['titre','participants']
        
class ConversationFormOO(forms.ModelForm):
    class Meta:
        model = ConversationOO
        fields = ['titre','Username']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['titre'].widget.attrs['placeholder'] = "Titre de la conversation"
        self.fields['Username'].widget.attrs['placeholder'] = "Nom d'un participant"
        
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']
        
    
        