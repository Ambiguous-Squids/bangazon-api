from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from bangazon_api.models import Customer, Product, PaymentType, ProductType, Order

# Define an inline admin descriptor for Customer model
# which acts a bit like a singleton

class CustomerInline(admin.StackedInline):
	model = Customer
	can_delete = False
	verbose_name_plural = 'customers'


class UserAdmin(BaseUserAdmin):
	inlines = (CustomerInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Customer)
admin.site.register(ProductType)
admin.site.register(PaymentType)
admin.site.register(Order)
admin.site.register(Product)




