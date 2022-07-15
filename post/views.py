from django.contrib.auth.models import Group
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from rest_framework import permissions, viewsets

from post.models import Media, Post
from post.serializers import MediaSerializer, PostSerializer


class MediaViewSet(viewsets.ModelViewSet):
    """
    API endpoint for media files information
    """

    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint for posts
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
