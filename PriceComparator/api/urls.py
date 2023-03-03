from django.urls import path, include
from rest_framework import routers

from api import views

router_v1 = routers.DefaultRouter()
router_v1.register(r'products', views.ProductCustomViewSet, basename='products')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
