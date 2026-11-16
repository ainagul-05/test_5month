from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField(read_only=True)
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = [
            'author',
            'created_at',
            'updated_at',
            'comments_count'
        ]

    def get_comments_count(self, obj):
        return obj.comments.count()
class CommentSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = [
            'author',
            'post',
            'created_at',
            'updated_at'
        ]