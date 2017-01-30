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



