from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing),  # IP주소 /
    path('Ear/', views.Ear)  # IP주소 / about_me/
]