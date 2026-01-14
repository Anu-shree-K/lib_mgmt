# books/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                 # library/
    path('members/', views.member_list, name='member_list'),
    path('categories/', views.category_list, name='category_list'),
]
