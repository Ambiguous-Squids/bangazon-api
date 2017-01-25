from django.shortcuts import render
from bangazon_api.models import PaymentType, Customer, Order
from bangazon_api.serializers import PaymentTypeSerializer, CustomerSerializer, OrderSerializer
from rest_framework import viewsets


# Create your views here.
class PaymentTypeViewSet(viewsets.ModelViewSet):
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeSerializer

    """
    Creates PaymentType View
    @nchemsak
    """

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
