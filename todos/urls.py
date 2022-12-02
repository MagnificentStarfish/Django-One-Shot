from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from todos.views import Todo_List_List

urlpatterns = [
    path("", Todo_List_List, name="Todo_List"),
]
