from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('results/<str:id>/', views.results, name='results'),
]
