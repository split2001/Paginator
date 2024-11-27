from rest_framework import serializers
from task1.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'content')  # указываем поля, которые будем парсить
