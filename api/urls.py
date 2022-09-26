from django.urls import path
from api import views

urlpatterns = [
    path('resume/', views.resume_list, name='resume'),
    path('resume/<int:pk>/', views.resume_detail, name='details'),
]