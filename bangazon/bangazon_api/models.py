from django.db import models

class Customer(models.Model):
	"""Create Customers table for Bangazon API @asimonia"""
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	account_created = models.DateTimeField(auto_now_add=True)
	address_1 = models.CharField(max_length=128)
	address_2 = models.CharField(max_length=128, blank=True)
	city = models.CharField(max_length=20)
	state = models.CharField(max_length=20)
	zip_code = models.CharField(max_length=10)
	email = models.EmailField(max_length=128, unique=True)

	class Meta:
		verbose_name_plural = 'Customers'

	def __str__(self):
		return '{} {}'.format(self.first_name, self.last_name)

class ProductType(models.Model):
	"""Create Product Types table for Bagazon API @asimonia"""
	category = models.CharField(max_length=50)

	class Meta:
		verbose_name_plural = 'ProductTypes'

	def __str__(self):
		return str(self.category)

class PaymentType(models.Model):
	"""Create Payment Types table for Bangazon API @asimonia"""
	NONE = ''
	VISA = 'VISA'
	MASTERCARD = 'MasterCard'
	AMERICANEXPRESS = 'American Express'

	"""Payment type choices @nchemsak"""
	PAYMENT_TYPE_NAME_CHOICES = (
		(NONE, ''),
		(VISA, 'VISA'),
		(MASTERCARD, 'MasterCard'),
		(AMERICANEXPRESS, 'American Express'),

	)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	payment_type_name = models.CharField(max_length=16, choices=PAYMENT_TYPE_NAME_CHOICES, default=NONE)
	category = models.CharField(max_length=50)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	account = models.CharField(max_length=16, unique=True)
	expiration_date = models.DateField()
	ccv = models.CharField(max_length=3)



	class Meta:
		verbose_name_plural = 'PaymentTypes'

	def __str__(self):
		return '{} - {}'.format(self.payment_type_name, self.account)

class Order(models.Model):
	"""Create Orders table for Bangazon API @asimonia"""
	active = models.BooleanField(default=True)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural = 'Orders'

	def __str__(self):
		return 'Customer {} account is active? {}'.format(self.customer, self.active)

class Product(models.Model):
	"""Create Products table for Bangazon API @asimonia"""
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
	order = models.ForeignKey(Order, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=50)
	price = models.DecimalField(max_digits=15, decimal_places=2)

	class Meta:
		verbose_name_plural = 'Products'

	def __str__(self):
		return str(self.name)
