from django.urls import path
from . import views

#UrlConf module
urlpatterns = [
    path('hello/', views.say_hello)
]