from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Thread, Post, Category
from common.serializers import LocalDateTimeField


User = get_user_model()


class CategoryListSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    thread_count = serializers.IntegerField()
    post_count = serializers.IntegerField()
    latest = LocalDateTimeField(format="%-I:%M%p %m/%d/%Y")

    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'thread_count', 'latest', 'post_count')


class CategoryDetailSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Category
        fields = ('id', 'name', 'description')


class ThreadListSerializer(serializers.ModelSerializer):
    post_count = serializers.IntegerField()
    latest = LocalDateTimeField(format="%-I:%M%p %m/%d/%Y")
    created_date = LocalDateTimeField(format="%-I:%M%p %m/%d/%Y")
    author = serializers.StringRelatedField()

    class Meta:
        model = Thread
        fields = ('id', 'subject', 'category', 'post_count', 'latest', 'author', 'created_date')


class ThreadCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Thread
        fields = ('subject', 'category', 'author')


class PostSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    author = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = ('id', 'author', 'created_date', 'text',
            'last_edited_date', 'thread',)

