from  . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home' ),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('category/<int:category_id>', views.post_by_category, name='post_by_category'),
    path('<slug:slug>/', views.blog, name='single_blog'),
    path('blog/search', views.search, name='search'),
]