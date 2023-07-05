from django.urls import path
from .views import BooksList, BookDetail, NewBooksInMarketsList, NewBooksInMarketDetail

urlpatterns = [
    path('', BooksList.as_view(), name='books_list'),
    path('<int:pk>/', BookDetail.as_view(), name='book_detail'),
    path('newinmarkets/', NewBooksInMarketsList.as_view(), name='NewBooksInMarkets_list'),
    path('newinmarkets/<int:pk>/', NewBooksInMarketDetail.as_view(), name='NewBooksInMarket_detail'),
]