from rest_framework import serializers
from bangazon_api.models import Customer

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    """
    Hyperlinked Serializer for the Customer Model.
    -Matthew McCord
    """
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'account_created',
            'address_1', 'address_2', 'city', 'state', 'zip_code', 'email')