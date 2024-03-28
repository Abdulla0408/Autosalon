from django.urls import path
from .views import all_posts, posts_by_category


urlpatterns = [
    path('', all_posts, name='index'),
    path('category/<int:category_id>/', posts_by_category, name='department'),
]