from django.contrib import admin
from django.urls import path, include
from .views import (Note_List, Note_Create, Note_Delete, Note_Update, Note_View)
from . import views

urlpatterns = [
    path('', Note_List.as_view(), name='view'),
    path('create', Note_Create.as_view(), name='create'),
    path('view/<pk>', Note_View.as_view(), name='view'),
    path('update/<pk>', Note_Update.as_view(), name='update'),
    path('delete/<pk>', Note_Delete.as_view(), name='delete'),
]
