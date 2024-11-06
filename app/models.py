from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.product.name} ({self.quantity})'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order {self.id} by {self.user.username}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


# models.py
from django.db import models
from django.db import models
from django.core.validators import RegexValidator


from django.db import models
from django.core.validators import RegexValidator

class Payment(models.Model):
    PAYMENT_CHOICES = [
        ('credit_card', 'Credit Card'),
        ('debit_card', 'Debit Card'),
        ('paypal', 'PayPal')
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    payment_type = models.CharField(max_length=20, choices=PAYMENT_CHOICES)

    card_number = models.CharField(
        max_length=16,
        validators=[RegexValidator(regex=r'^\d{16}$', message='Card number must be 16 digits')]
    )
    expiry_date = models.CharField(max_length=7)  # format: YYYY-MM

    cvv = models.CharField(
        max_length=4,
        validators=[RegexValidator(regex=r'^\d{3,4}$', message='CVV must be 3 or 4 digits')]
    )

    def __str__(self):
        return f"{self.name} - {self.payment_type}"
