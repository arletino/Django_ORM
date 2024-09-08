from django.urls import path
from .views import total_in_db, total_in_template, total_in_view

urlpatterns = [
    path('db/', total_in_db, name='db'),
    path('view/', total_in_view, name='view'),
    path('template/', total_in_template, name='template')
]