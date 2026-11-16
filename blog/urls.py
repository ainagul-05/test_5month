from django.urls import path
from .views import PostListCreateAPIView, PostDetailAPIView, CommentListCreateAPIView, CommentDetailAPIView

urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailAPIView.as_view(), name='post-detail'),
    path('posts/<int:post_id>/comments/', CommentListCreateAPIView.as_view(), name='comment-list-create'),
    path('posts/<int:post_id>/comments/<int:pk>/', CommentDetailAPIView.as_view(), name='comment-detail'),
]

