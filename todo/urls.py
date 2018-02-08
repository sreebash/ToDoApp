
from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('add/', views.addTodo, name='add'),
    path('complete/<todo_id>', views.todoComplete, name='complete'),
    path('deletecomplete/', views.deleteCompleted, name='deletecomplete'),
    path('deleteall/', views.deleteAll, name='deleteall'),
]
