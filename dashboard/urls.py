from django.urls import path
from . import views
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/categories/', views.categories, name='categories'),
    path('dashboard/add_category', views.add_category, name='add_category'),
    path('dashboard/edit_category/<int:pk>', views.edit_category, name='edit_category'),
    path('dashboard/delete_category/<int:pk>', views.delete_category, name='delete_category'),
    path('dashboard/posts/', views.posts, name='posts'),
    path('dashboard/add_post', views.add_post, name='add_post'),

]