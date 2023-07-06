from django.shortcuts import render
from rest_framework import generics
from .models import Book, NewBooksInMarkets 
from .serializers import BookSerializer, NewBooksInMarketsSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from django.http import HttpResponse

# Create your views here.

# ListAPIView
class BooksList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# RetrieveAPIView RetrieveUpdateAPIView
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsOwnerOrReadOnly]

# ListAPIView
class NewBooksInMarketsList(generics.ListCreateAPIView):
    queryset = NewBooksInMarkets.objects.all()
    serializer_class = NewBooksInMarketsSerializer
    permission_classes = [AllowAny]

# RetrieveAPIView RetrieveUpdateAPIView
class NewBooksInMarketDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewBooksInMarkets.objects.all()
    serializer_class = NewBooksInMarketsSerializer
    permission_classes = [AllowAny]

def HomeView(request):
    return HttpResponse("Welcome to the Reading List RESTful API!")    