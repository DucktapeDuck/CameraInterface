from . import views
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.index, name='index'),
    path('livefeed/', views.livefeed, name='livefeed'),
]