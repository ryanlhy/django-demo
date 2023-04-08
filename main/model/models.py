from django.db import models

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=50)
    income = models.BigIntegerField()
    testing = models.CharField(max_length=50, default='testing')

class CardSets(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=50, null=True)
    series = models.CharField(max_length=50, null=True)
    printed_total = models.IntegerField(null=True)
    total = models.IntegerField(null=True)
    unlimited_legality = models.CharField(max_length=50, null=True)
    ptcgo_code = models.CharField(max_length=20, null=True)
    release_date = models.DateField(null=True)
    updated_at = models.DateTimeField(null=True)
    symbol_image_url = models.CharField(max_length=200, null=True)
    logo_image_url = models.CharField(max_length=200, null=True)

class TestTable(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    uid = models.CharField(max_length=100)
    signup_date = models.DateTimeField(auto_now_add=True)
    signin_date = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='carts')
    total = models.DecimalField(max_digits=10, decimal_places=2)
    last_updated = models.DateTimeField(auto_now=True)
    notes = models.TextField(blank=True)

class CartDetails(models.Model):
    id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_details')
    ebay_item_number = models.CharField(max_length=100)
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=100)
    pokemon_id = models.CharField(max_length=15)
    grade = models.CharField(max_length=20)
    date_added = models.DateTimeField(auto_now_add=True)

class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    order_details = models.TextField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)

class OrderDetails(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name='order_details')
    ebay_item_number = models.CharField(max_length=100)
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=100)
    pokemon_id = models.CharField(max_length=15)
    grade = models.CharField(max_length=20)
    date_added = models.DateTimeField(auto_now_add=True)