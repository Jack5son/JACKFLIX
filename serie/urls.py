from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.cadastro, name='serie_list'),
    path('delete/<id>',views.delete, name='delete'),
    path('update/<id>',views.update, name='update'),

]