from django.contrib import admin
from django.urls import path
from .views import conversation_list,conversation_detail,messagerie,create_conversation,start_conversation,add_participant

app_name = 'Chat_Fora_S2'
urlpatterns = [
    path('', conversation_list, name = 'Acceuil'),
    path('Acceuil', conversation_list, name = 'Acceuil'),
    path('messagerie/<int:conversation_id>/', messagerie, name = 'messagerie'),
    path('conversations/<int:conversation_id>/', conversation_detail, name='conversation_detail'),
    path('create', create_conversation, name = 'create'),
    path('start/<str:titre>/<str:other_user_name>',start_conversation ,name = 'start_conversation'),
    path('add/<int:conversation_id>/<str:other_user_name>',add_participant)
]
