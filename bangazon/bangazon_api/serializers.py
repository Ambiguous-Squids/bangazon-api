from bangazon_api.models import Customer, ProductType, PaymentType, Order, Product
from rest_framework import serializers


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('customer', 'product_type', 'order', 'name', 'description', 'price' )

