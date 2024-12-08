from rest_framework import serializers
from polling.models import Poll



# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ['id', 'name', 'description']

# class PostSerializer(serializers.ModelSerializer):
#     categories = CategorySerializer(many=True, read_only=True)  # Nested categories

#     class Meta:
#         model = Post
#         fields = ['id', 'title', 'text', 'author', 'created_date', 'published_date', 'categories']


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ['title', 'text', 'score']