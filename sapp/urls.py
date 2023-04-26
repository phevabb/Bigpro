from django.urls import path
from . import views
urlpatterns = [
    path('', views.firsturl, name='firsturl'),

path('one/', views.secondurl, name='secondurl'),




]