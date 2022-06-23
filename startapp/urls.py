from django.urls import path
from startapp import views

urlpatterns = [
    path('', views.startapp, name='index'),
]