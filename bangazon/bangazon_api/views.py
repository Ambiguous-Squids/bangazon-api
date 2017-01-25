from django.shortcuts import render
from rest_framework import viewsets
from bangazon_api.models import Customer, Order
from bangazon_api.serializers import CustomerSerializer, OrderSerializer


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