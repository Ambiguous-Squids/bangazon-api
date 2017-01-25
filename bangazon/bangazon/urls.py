
from django.conf.urls import url, include
from django.contrib import admin
from bangazon_api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)



urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

