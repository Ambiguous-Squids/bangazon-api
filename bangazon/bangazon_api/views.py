from django.shortcuts import render
from rest_framework import viewsets
from bangazon_api.models import Product, Customer
from bangazon_api.serializers import ProductSerializer, CustomerSerializer



class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed.
    @itsdanirenae
    """
    queryset = Product.objects.all().order_by('-name')
    serializer_class = ProductSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Customers to be viewed or edited.
    -@mccordgh
    """

    queryset = Customer.objects.all().order_by('-last_name')
    serializer_class = CustomerSerializer
