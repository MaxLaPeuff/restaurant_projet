# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('menu/', views.menu, name='menu'),
    path('commander/',views.commander,name="commander"),
    path('confirmation/',views.confirmation,name="confirmation")
]
