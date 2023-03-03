from rest_framework import serializers

from .models import Product, SupermarketProduct


class ProductCustomSerializer(serializers.ModelSerializer):
    supermarkets = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id_product', 'product', 'description', 'supermarkets')

    def get_supermarkets(self, product):
        supermarkets_product = SupermarketProduct.objects.filter(product=product.id_product)
        supermarkets: list = []
        import datetime

        for supermarket_product in supermarkets_product:
            audit_time: datetime.datetime = supermarket_product.audit_time
            price_supermarket: dict = {}
            price_supermarket['supermarket'] = supermarket_product.supermarket.id_supermarket
            price_supermarket['measurement'] = supermarket_product.measurement.measurement
            price_supermarket['price'] = supermarket_product.last_price
            price_supermarket['amount'] = supermarket_product.amount
            price_supermarket['audit_time'] = int(audit_time.timestamp())
            supermarkets.append(price_supermarket)
        return supermarkets
