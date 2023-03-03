from rest_framework import serializers

from .models import Product, SupermarketProduct


class ProductCustomSerializer(serializers.ModelSerializer):
    supermarkets = serializers.SerializerMethodField()
    last_edit = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id_product', 'product', 'description', 'last_edit', 'supermarkets')

    def get_supermarkets(self, product):
        supermarkets_product = SupermarketProduct.objects.filter(product=product.id_product)
        supermarkets: list = []

        for supermarket_product in supermarkets_product:
            price_supermarket: dict = {}
            price_supermarket['supermarket'] = supermarket_product.supermarket.id_supermarket
            price_supermarket['measurement'] = supermarket_product.measurement.measurement
            price_supermarket['price'] = supermarket_product.last_price
            price_supermarket['amount'] = supermarket_product.amount
            supermarkets.append(price_supermarket)
        return supermarkets

    def get_last_edit(self, product):
        import datetime
        audit_time: datetime.datetime = product.audit_time
        return int(audit_time.timestamp())
