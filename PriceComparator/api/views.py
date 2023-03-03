from rest_framework import viewsets

from api.models import Product
from api.serializers import ProductCustomSerializer


class ProductCustomViewSet(viewsets.ReadOnlyModelViewSet):
    # Visualiza todos los productos del sistema acompañado del precio del producto
    queryset = Product.objects.all()
    serializer_class = ProductCustomSerializer
