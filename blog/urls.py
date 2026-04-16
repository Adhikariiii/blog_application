from  . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home' ),
    path('category/<int:category_id>', views.post_by_category, name='post_by_category')
]