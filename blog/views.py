from django.shortcuts import render

from rest_framework import generics 
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly


class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [ IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]


class CommentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post_id=post_id)

    def perform_create(self, serializer):
        from django.shortcuts import get_object_or_404

        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        serializer.save(author=self.request.user, post=post)

class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
        serializer_class = CommentSerializer
        permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

        def get_queryset(self):
             return Comment.objects.filter(post_id=self.kwargs['post_id'])

        
