from django.urls import path
from . import views

app_name = 'feed'

urlpatterns = [
    path('', views.feed, name='feed'),
    path('post/', views.post_message, name='post_message'),
    path('comment/<int:message_id>/', views.post_comment, name='post_comment'),
    path('delete/<int:message_id>/', views.delete_message, name='delete_message'),
    path('like/<int:message_id>/', views.like_message, name='like_message'),
    path('like/comment/<int:comment_id>/', views.like_comment, name='like_comment'),
]
