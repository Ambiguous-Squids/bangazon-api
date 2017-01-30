from django.db import models

class Customer(models.Model):
	"""
	The Customers table maintains relevant information for a customer

	@asimonia

	"""
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
	"""
	The Product Types table maintains the product types or 'categories' of products

	@asimonia

	"""
	category = models.CharField(max_length=50)

	class Meta:
		verbose_name_plural = 'ProductTypes'

	def __str__(self):
		return str(self.category)

class PaymentType(models.Model):
	"""
	The Payment Types table maintains the different payment options associated with a customer

	@asimonia & @nchemsak

	"""
	NONE = ''
	VISA = 'VISA'
	MASTERCARD = 'MasterCard'
	AMERICANEXPRESS = 'American Express'


	PAYMENT_TYPE_NAME_CHOICES = (
		(NONE, ''),
		(VISA, 'VISA'),
		(MASTERCARD, 'MasterCard'),
		(AMERICANEXPRESS, 'American Express'),

	)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	payment_type_name = models.CharField(max_length=16, choices=PAYMENT_TYPE_NAME_CHOICES, default=NONE)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	account = models.CharField(max_length=16, unique=True)
	expiration_date = models.DateField()
	ccv = models.CharField(max_length=3)



	class Meta:
		verbose_name_plural = 'PaymentTypes'

	def __str__(self):
		return '{} - {}'.format(self.payment_type_name, self.account)


class Product(models.Model):
	"""
	The Products table maintains the information related to individual products

	@asimonia

	"""
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	description = models.TextField(max_length=4000)
	price = models.DecimalField(max_digits=15, decimal_places=2)
	quantity = models.PositiveIntegerField(default=1)


	class Meta:
		verbose_name_plural = 'Products'

	def __str__(self):
		return str(self.name)

class Order(models.Model):
	"""
	The Orders table maintains information related to the products a customer wants to buy.

	@asimonia

	"""
	active = models.BooleanField(default=True)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE, blank = True, null = True)
	products = models.ManyToManyField(Product)


	class Meta:
		verbose_name_plural = 'Orders'

	def __str__(self):
		return 'Customer {} account is active? {}'.format(self.customer, self.active)











