from rest_framework import serializers
from blogging.models import Post, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "description"]


class PostSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)  # Nested categories

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "text",
            "author",
            "created_date",
            "published_date",
            "categories",
        ]
