from django.shortcuts import render
from bangazon_api import serializers, models
from rest_framework import viewsets
from django.contrib.auth.models import User


class PaymentTypeViewSet(viewsets.ModelViewSet):
    """
    Creates PaymentType View
    @nchemsak
    """
    queryset = models.PaymentType.objects.all()
    serializer_class = serializers.PaymentTypeSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed.
    @itsdanirenae
    """
    queryset = models.Product.objects.all().order_by('-name')
    serializer_class = serializers.ProductSerializer

    
class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Customers to be viewed or edited.
    -@mccordgh
    """
    queryset = models.Customer.objects.all().order_by('-last_name')

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return serializers.UserStaffSerializer
        return serializers.UserSerializer    


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Orders to be viewed or edited.
    -@asimonia
    """

    queryset = models.Order.objects.all().order_by('-customer')
    serializer_class = serializers.OrderSerializer

class ProductTypeViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows Product Types to be viewed or edited.
    @rtwhitfield84

    """

    queryset = models.ProductType.objects.all().order_by('-category')
    serializer_class = serializers.ProductTypeSerializer