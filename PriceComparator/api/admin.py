from django.contrib import admin

from api.models import Supermarket, ProductMeasurement, Product, SupermarketProduct, SupermarketProductRegistry

admin.site.register(Supermarket)
admin.site.register(ProductMeasurement)
admin.site.register(Product)
admin.site.register(SupermarketProduct)
admin.site.register(SupermarketProductRegistry)
