from django.urls import path
from .views import create_job, job_list


urlpatterns = [
    path('jobs/', job_list, name='job_list'),
    path('jobs/create/', create_job, name='create_job'),
]