from django.urls import path
from .views import (
    index, themes,
    pupils, homework,
    point_for_month
)

urlpatterns = [
    path('', index, name='index'),
    path('themes/', themes, name='themes'),
    path('homework/', homework, name='homework'),
    path('pupils/', pupils, name='pupils'),
    path('pupils/<int:pk>/', point_for_month, name='points')
]