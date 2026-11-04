from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('about/contacts/', views.contacts, name='contacts'),
    path('about/how-to-find/', views.how_to_find, name='how_to_find'),
    path('catalog/', views.catalog, name='catalog'),
    path('resources/', views.resources, name='resources'),
]
