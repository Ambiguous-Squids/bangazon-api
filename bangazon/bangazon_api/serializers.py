from django.contrib.auth.models import User
from rest_framework import serializers
from bangazon_api import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Creates a Staff Serializer
    @asimonia
    """
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'groups',
                  'is_staff', 'is_active', 'is_superuser', 'last_login',
                  'date_joined',)

class RestrictedUserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Hyperlinked Serializer for the Customer Model.
    @mccordgh
    """
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', )

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    """
    Hyperlinked Serializer for the Customer Model.
    @mccordgh
    """
    class Meta:
        model = models.Customer
        fields = '__all__'

class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):

    """
    Creates PaymentType Serializer
    @rtwhitfield84

    """
    class Meta:
        model = models.PaymentType
        fields = ('customer', 'payment_type_name', 'first_name', 'last_name', 'account',
                  'expiration_date', 'ccv',)

class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):

    """
    Creates ProductType Serializer
    @rtwhitfield84

    """

    class Meta:
        model = models.ProductType
        fields = ('category', )

class OrderSerializer(serializers.HyperlinkedModelSerializer):

    """
    Creates Order Serializer
    @rtwhitfield84

    """

    class Meta:
      model = models.Order
      fields = ('active', 'customer', 'payment_type', 'products', )

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """
    Hyperlinked Serializer for the Product Model.
    @itsdanirenae
    """
    class Meta:
        model = models.Product
        fields = ('customer', 'product_type', 'name', 'description', 'price', 'quantity', )






