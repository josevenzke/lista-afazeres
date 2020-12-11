from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name='list'),
    path("atualizar/<str:pk>", views.updateTask, name="atualizar"),
    path("deletar/<str:pk>", views.deleteTask, name="deletar")
]
