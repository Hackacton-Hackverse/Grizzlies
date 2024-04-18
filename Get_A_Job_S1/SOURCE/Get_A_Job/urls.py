from django.contrib import admin
from django.urls import path,include
from .views import index,job_list,create_job,update_job,postuler_job,delete_job,Action_admin,select_offre,handler

from .views import CreerJobOfferAPIView


urlpatterns = [
    path('admin/',  admin.site.urls),
    path('', index, name = 'index'),
    path('list/',job_list, name = 'job-list'),
    path('Action-admin/',Action_admin),
    path('accounts/login/',handler),
    path('update-<str:job_titre>/',update_job, name = 'update-job'),
    path('delete-<str:job_titre>/',delete_job, name = 'delete-job'),
    path('postuler-<int:job_id>/',postuler_job, name = 'postuler-job'),
    path('select_offre-<str:objet>/',select_offre),
    path('create/', create_job, name='create-job1'),
    path('offres/',CreerJobOfferAPIView.as_view(), name='creer_offre')
]
