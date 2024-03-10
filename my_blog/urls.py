from django.urls import path
from my_blog import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:post_id>/', views.post_detail, name='post'),
    path('create_post/', views.create_post, name='create_post'),
    path('tags/<tag_slug>', views.posts_by_tag, name='posts_by_tag'),
    path('by_author/<int:author_id>', views.posts_by_author, name='posts_by_author'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),

]
