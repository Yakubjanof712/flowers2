from django.urls import path
from . import views
from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]

urlpatterns = [
    path('', views.home, name='home'),
    path('add_course/', views.add_course, name='add_course'),
    path('add_lesson/', views.add_lesson, name='add_lesson'),
    path('add_turlar/', views.add_turlar, name='add_turlar'),
    path('add_gullar/', views.add_gullar, name='add_gullar'),
]
def home(request):
    return render(request, 'main/home.html')
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
