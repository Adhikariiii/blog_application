from django.urls import path
from . import views
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/categories/', views.categories, name='categories'),
    path('dashboard/add_category', views.add_category, name='add_category'),
]