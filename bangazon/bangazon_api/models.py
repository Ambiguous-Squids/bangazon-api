from django.db import models

class Customer(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	account_created = models.DateField()
	address_1 = models.CharField(max_length=128)
	address_2 = models.CharField(max_length=128)
	city = models.CharField(max_length=20)
	state = models.CharField(max_length=20)
	zip_code = models.CharField(max_length=10)
	email = models.EmailField(max_length=128, unique=True)

	class Meta:
		verbose_name_plural = 'Customers'

	def __str__(self):
		return '{} {}'.format(self.first_name, self.last_name)

class ProductType(models.Model):
	category = models.CharField(max_length=50)

	class Meta:
		verbose_name_plural = 'ProductTypes'

	def __str__(self):
		return self.category

class PaymentType(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	account = models.CharField(max_length=16, unique=True)
	expiration_date = models.DateField()
	ccv = models.CharField(max_length=3)

	class Meta:
		verbose_name_plural = 'PaymentTypes'

	def __str__(self):
		return self.account

class Order(models.Model):
	active = models.BooleanField()
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural = 'Orders'

	def __str__(self):
		return '{}: {}'.format(self.active, self.customer)

class Product(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
	order = models.ForeignKey(Order, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=50)
	price = models.DecimalField(max_digits=7, decimal_places=2)

	class Meta:
		verbose_name_plural = 'Products'

	def __str__(self):
		return self.name
