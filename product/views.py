from rest_framework import generics
from .models import Category, Product, Review
from .serializers import (CategorySerializer, ProductSerializer, ReviewSerializer, ProductReviewsSerializer)
from django.db.models import Avg, Count

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    def get_queryset(self):
        return Category.objects.annotate(
            products_count=Count('products'))

class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'


class ReviewListAPIView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetailAPIView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'
    
class ProductReviewsAPIView(generics.ListAPIView):
    serializer_class = ProductReviewsSerializer
    def get_queryset(self):
        return Product.objects.annotate(
            rating=Avg('reviews__stars')
        ).prefetch_related('reviews')