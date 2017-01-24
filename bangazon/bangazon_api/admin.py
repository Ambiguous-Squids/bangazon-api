from django.contrib import admin
from bangazon_api.models import Customer, Product, PaymentType, ProductType, Order

admin.site.register(Customer)
admin.site.register(ProductType)
admin.site.register(PaymentType)
admin.site.register(Order)
admin.site.register(Product)




