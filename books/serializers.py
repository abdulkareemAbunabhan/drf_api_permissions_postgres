from rest_framework import serializers
from .models import Book, NewBooksInMarkets

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields = ('id', 'owner', 'name', 'desc', 'created_at', 'updated_at')

class NewBooksInMarketsSerializer(serializers.ModelSerializer):
    class Meta:
        model=NewBooksInMarkets
        fields = ('title', 'desc')