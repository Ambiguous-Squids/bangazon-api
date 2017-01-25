from rest_framework import serializers
from bangazon_api.models import PaymentType, Order, ProductType, Product, Customer


class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):

    """
    Creates PaymentType Serializer
    @rtwhitfield84

    """

    class Meta:
        model = PaymentType
        fields = ('customer', 'first_name', 'last_name', 'account', 'expiration_date', 'ccv')

class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):

    """
    Creates ProductType Serializer
    @rtwhitfield84

    """

    class Meta:
        model = ProductType
        fields = ('category')

class OrderSerializer(serializers.HyperlinkedModelSerializer):

    """
    Creates Order Serializer
    @rtwhitfield84

    """

    class Meta:
      model = Order
      fields = ('active', 'customer', 'payment_type')



class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """
    Hyperlinked Serializer for the Product Model.
    @itsdanirenae
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


