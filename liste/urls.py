from django.conf.urls import url
from django.contrib import admin
from . import views

from django.urls import path

urlpatterns = [
  url(r'^$', views.home, name='home'),
  path('add_todo/', views.add_todo),
  path('delete_todo/<int:todo_id>/', views.delete_todo),
  path('<int:todo_id>/', views.detail_todo, name='detail'),
  path('modify_todo/<int:todo_id>/', views.modify_todo, name='modify'),
]