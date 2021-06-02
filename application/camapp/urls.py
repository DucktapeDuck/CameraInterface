from . import views
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.index, name='index'),
    # path('books/', views.BookListView.as_view(), name='books'),
    path('camera/', views.livefe, name='livefe'),
]