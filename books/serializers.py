from rest_framework import serializers

from .models import Book, Category


class CategorySerializer(serializers.ModelSerializer):
    model = Category
    fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    # seller = serializers.ReadOnlyField(source='User.username')
    # seller_id = serializers.ReadOnlyField(source='seller.id')
    cover = serializers.ImageField(required=False)
    # category = CategorySerializer(source='category_set', many=True)

    class Meta:
        model = Book
        # fields = ["category", "title", "description", "cover", "writer", "price", "rate", "seller", "boutique"]
        fields = "__all__"

