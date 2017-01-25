from django.shortcuts import render
from bangazon_api.models import PaymentType
from bangazon_api.serializers import PaymentTypeSerializer
from rest_framework import viewsets

# Create your views here.
class PaymentTypeViewSet(viewsets.ModelViewSet):
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeSerializer

    """
    Creates PaymentType View
    @nchemsak

    """
