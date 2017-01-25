from django.shortcuts import render
from rest_framework import viewsets
from bangazon_api.models import Customer
from bangazon_api.serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Customers to be viewed or edited.
    -@mccordgh
    """

    queryset = Customer.objects.all().order_by('-last_name')
    serializer_class = CustomerSerializer