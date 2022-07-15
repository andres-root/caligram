from django.contrib.auth.models import Group, User
from rest_framework import serializers

from post.models import Media, Post


class MediaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Media
        fields = '_all_'


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = '_all_'
