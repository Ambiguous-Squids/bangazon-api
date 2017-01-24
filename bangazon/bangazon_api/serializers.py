from rest_framework import serializers
from bangazon_api.models import PaymentType, Order, ProductType


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
