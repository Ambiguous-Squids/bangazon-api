from django.conf.urls import url, include
from django.contrib import admin
from bangazon_api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'customers', views.CustomerViewSet)
router.register(r'orders', views.OrderViewSet)
router.register(r'payment_types', views.PaymentTypeViewSet)
router.register(r'product_types', views.ProductTypeViewSet)
# router.register(r'customers', views.UserViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]