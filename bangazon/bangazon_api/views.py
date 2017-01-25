from django.shortcuts import render
from rest_framework import viewsets
from bangazon_api.models import Product
from bangazon_api.serializers import ProductSerializer



class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed.
    @itsdanirenae
    """
    queryset = Product.objects.all().order_by('-name')
    serializer_class = ProductSerializer