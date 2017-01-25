from django.shortcuts import render
from bangazon_api.models import PaymentType, Customer, Order, Product, ProductType
from bangazon_api.serializers import PaymentTypeSerializer, CustomerSerializer, OrderSerializer, ProductSerializer, ProductTypeSerializer
from rest_framework import viewsets


class PaymentTypeViewSet(viewsets.ModelViewSet):
    """
    Creates PaymentType View
    @nchemsak
    """
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeSerializer


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


class OrderViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows Orders to be viewed or edited.
	-@asimonia
	"""

	queryset = Order.objects.all().order_by('-customer')
	serializer_class = OrderSerializer

class ProductTypeViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows Product Types to be viewed or edited.
    @rtwhitfield84

    """

    queryset = ProductType.objects.all().order_by('-category')
    serializer_class = ProductTypeSerializer
