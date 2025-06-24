from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.cadastro, name='filme_list'),
    path('delete/<id>',views.delete, name='delete'),
    path('update/<id>',views.update, name='update'),
]