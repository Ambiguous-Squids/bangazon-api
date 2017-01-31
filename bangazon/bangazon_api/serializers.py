from django.contrib.auth.models import User
from rest_framework import serializers
from bangazon_api import models


class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):

    """
    Creates PaymentType Serializer
    @rtwhitfield84

    """

    class Meta:
        model = models.PaymentType
        fields = '__all__'

class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):

    """
    Creates ProductType Serializer
    @rtwhitfield84

    """

    class Meta:
        model = models.ProductType
        fields = '__all__'

class OrderSerializer(serializers.HyperlinkedModelSerializer):

    """
    Creates Order Serializer
    @rtwhitfield84

    """

    class Meta:
      model = models.Order
      fields = '__all__'



class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """
    Hyperlinked Serializer for the Product Model.
    @itsdanirenae
    """
    class Meta:
        model = models.Product
        fields = '__all__'

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    """
    Hyperlinked Serializer for the Customer Model.
    @mccordgh
    """
    class Meta:
        model = models.Customer
        fields = '__all__'

class UserStaffSerializer(serializers.HyperlinkedModelSerializer):
    """
    Create a serializer for users who are staff, and can see all fields
    @mccordgh
    """

    class Meta:
        model = models.Customer
        fields = ('first_name', 'last_name', 'account_created', 'address_1', 'address_2', 'city', 'state', 'zip_code', 'email')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Create a serializer for users who are not staff, and can only view first_name and last_name fields
    @mccordgh
    """
    # customer = CustomerSerializer(many=False, read_only=True)

    class Meta:
        model = models.Customer
        fields = ('first_name', 'last_name')