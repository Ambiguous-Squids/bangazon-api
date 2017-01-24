from bangazon_api.models import Customer, ProductType, PaymentType, Order, Product
from rest_framework import serializers


class ProductSerializer(serializers.HyperlinkedModelSerializer):
  """
    Hyperlinked Serializer for the Product Model.
    -Danielle Adkins
    """
    class Meta:
        model = Product
        fields = ('customer', 'product_type', 'order', 'name', 'description', 'price' )


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    """
    Hyperlinked Serializer for the Customer Model.
    -Matthew McCord
    """
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'account_created',
            'address_1', 'address_2', 'city', 'state', 'zip_code', 'email')

