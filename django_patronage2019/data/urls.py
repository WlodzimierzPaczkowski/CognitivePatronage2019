from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    # /data/ strona z wyświetleniem tabeli i chart ów
    path('', views.index, name='index'),

]