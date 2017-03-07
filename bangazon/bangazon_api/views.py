from django.contrib.auth.models import User
from django.shortcuts import render
from bangazon_api import serializers, models
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect, Http404
# from django.core import serializers
import json



class UserViewSet(viewsets.ModelViewSet):
    """
    Creates StaffView
    @asimonia
    """
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return serializers.UserSerializer
        return serializers.RestrictedUserSerializer 


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
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer


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

class LoginView(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class=serializers.LoginSerializer
    queryset=User.objects.all()

    error_messages = {
        'invalid': "Invalid username or password",
        'disabled': "Sorry, this account is suspended",
    }

    def _error_response(self, message_key):
        data = {
            'success': False,
            'message': self.error_messages[message_key],
            'user_id': None,
        }

    def post(self,request):
        req_body = json.loads(request.body.decode())
        username = req_body['username']
        password = req_body['password']
        print(username, password)
        user = authenticate(username=username, password=password)

        success = False
        if user is not None:
            if user.is_active:
                login(request, user)
                success=True

        data = json.dumps({"success":success})
        return HttpResponse(data, content_type='application/json')