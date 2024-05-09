from django.contrib import admin
from django.urls import path
from .views import conversation_list,conversation_detail,messagerie,create_conversation,start_conversation,index,add_participant


urlpatterns = [
    path('',index),
    path('Acceuil', conversation_list, name = 'Acceuil'),
    path('messagerie/<int:conversation_id>/', messagerie, name = 'messagerie'),
    path('conversations/<int:conversation_id>/', conversation_detail, name='conversation_detail'),
    path('create', create_conversation, name = 'create'),
    path('start/<str:titre>/<str:other_user_name>',start_conversation ,name = 'start_conversation'),
    path('add/<str:other_user_name>',add_participant)
]
