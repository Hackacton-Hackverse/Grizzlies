from django.contrib import admin
from django.urls import path
from .views import conversation_list,conversation_detail,messagerie,create_conversation,start_conversation,send_message


urlpatterns = [
    path('', conversation_list, name = 'conversations'),
    path('messagerie/<int:conversation_id>/', messagerie, name = 'messagerie'),
    path('conversations/<int:conversation_id>/', conversation_detail, name='conversation_detail'),
    path('create', create_conversation),
    path('start/<int:other_user_id>/',start_conversation ,name = 'start_conversation'),
    path('send/<int:conversation_id>/',send_message ,name = 'send_message'),
]
