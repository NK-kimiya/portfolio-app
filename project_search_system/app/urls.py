from django.urls import path
from .views import hello_world,search_view

urlpatterns = [
    path('', hello_world),
    path('search/', search_view, name='search'),
]