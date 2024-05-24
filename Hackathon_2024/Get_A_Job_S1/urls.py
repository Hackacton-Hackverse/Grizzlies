from django.contrib import admin
from django.urls import path
from .views import job_list,create_job,update_job,postuler_job,delete_job,Action_admin,select_offre,handler,job_detail,chat


app_name = 'Get_A_Job_S1'
urlpatterns = [
    path('',job_list, name = 'job-list'),
    path('job_detail-<int:job_id>/', job_detail, name = 'job-detail'),
    path('chat-<int:job_id>/',chat,name = 'chat'),
    path('Action-admin/',Action_admin),
    path('accounts/login/',handler),
    path('update-<str:job_titre>',update_job, name = 'update-job'),
    path('delete-<str:job_titre>/',delete_job, name = 'delete-job'),
    path('postuler-<int:job_id>/',postuler_job, name = 'postuler-job'),
    path('select_offre-<str:objet>/',select_offre),
    path('create/', create_job, name='create-job1'),
    
]
