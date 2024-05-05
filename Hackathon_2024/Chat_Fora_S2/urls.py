from django.contrib import admin
from django.urls import path
from .views import conversation_list,conversation_detail,messagerie


urlpatterns = [
    # path('admin/',  admin.site.urls),
    path('', conversation_list, name = 'conversations'),
    path('messagerie', messagerie, name = 'messagerie'),
    path('conversations/<int:conversation_id>/', conversation_detail, name='conversation_detail'),

]
