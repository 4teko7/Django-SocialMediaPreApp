from django.conf.urls import url
from django.contrib import admin
from todo.todoViews import *
app_name = "todoRoutes"
urlpatterns = [
    url("addtodo/",addTodo,name = "addtodo"),

]