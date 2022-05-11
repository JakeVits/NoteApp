from django.contrib import admin
from django.urls import path, include
from note import views
from . import views

app_name = 'note'

urlpatterns = [
    path('', views.NoteListView.as_view(), name='list-note'),
    path('registration/', views.RegView.as_view(), name='registration'),
    path('create-note/', views.NoteCreateView.as_view(), name='create-note'),
    # path('view-note/<pk>/', views.NoteDetailView.as_view(), name='view-note'),
    path('update-note/<pk>/', views.NoteUpdateView.as_view(), name='update-note'),
    path('delete-note/<pk>/', views.NoteDeleteView.as_view(), name='delete-note'),
]
