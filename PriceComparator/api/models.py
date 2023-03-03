from django.contrib.auth.models import User
from django.db import models


class Supermarket(models.Model):
    id_supermarket = models.AutoField(primary_key=True)
    supermarket = models.CharField(max_length=50, null=False)
    location = models.CharField(max_length=50, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    audit_time = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['supermarket', 'location'], name='unique Supermarket')
        ]

    def __str__(self):
        return f'{self.supermarket} ({self.location})'


class ProductMeasurement(models.Model):
    id_product_measurement = models.AutoField(primary_key=True)
    measurement = models.CharField(max_length=8, null=False)
    description = models.CharField(max_length=50, null=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['measurement'], name='unique ProductMeasurement')
        ]

    def __str__(self):
        return f'[{self.measurement}] {self.description}'


class Product(models.Model):
    id_product = models.AutoField(primary_key=True)
    product = models.CharField(max_length=100, null=False)
    description = models.TextField(default=None, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    added_time = models.DateTimeField(auto_now_add=True)
    audit_time = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['product'], name='unique Product')
        ]

    def __str__(self):
        return f'{self.product}'


class SupermarketProduct(models.Model):
    id_supermarket_product = models.AutoField(primary_key=True)
    supermarket = models.ForeignKey(Supermarket, on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    measurement = models.ForeignKey(ProductMeasurement, on_delete=models.CASCADE, null=False)
    amount = models.FloatField(null=False)
    last_price = models.FloatField(null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    audit_time = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['supermarket', 'product'], name='unique SupermarketProduct')
        ]

    def __str__(self):
        return f'[{self.supermarket.supermarket}] {self.product.product}'


class SupermarketProductRegistry(models.Model):
    id_supermarket_product_registry = models.AutoField(primary_key=True)
    supermarket_product = models.ForeignKey(SupermarketProduct, on_delete=models.CASCADE, null=False)
    price = models.FloatField(null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    audit_time = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['supermarket_product', 'price'], name='unique SupermarketProductRegistry')
        ]

    def __str__(self):
        date: str = self.audit_time.strftime("%d/%m/%Y")
        return f'{self.supermarket_product} {date}'
