from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('users/', views.users, name='users'),
    path('projects/', views.projects, name='projects'),
    path('create_project/', views.create_project, name='create_project'),
    path('expenses/', views.expenses, name='expenses'),
    path('create_expense/', views.create_expense, name='create_expense'),
    path('create_user/', views.create_user, name='create_user'),
    
]
