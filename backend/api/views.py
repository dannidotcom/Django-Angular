from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Customer, Product, Order, Payment
from .serializers import (
    CustomerSerializer, ProductSerializer,
    OrderSerializer, PaymentSerializer
)

class HelloAPIView(APIView):
    def get(self, request):
        return Response({"message": "DRF is working!"})

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().prefetch_related('items__product')
    serializer_class = OrderSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all().select_related('order')
    serializer_class = PaymentSerializer
