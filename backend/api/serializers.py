from api.services.order_service import create_order_with_items
from rest_framework import serializers
from .models import Customer, Product, Order, OrderItem, Payment

# S: Chaque serializer a une seule responsabilité

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source='product', write_only=True
    )

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_id', 'quantity', 'price']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    customer = CustomerSerializer(read_only=True)
    customer_id = serializers.PrimaryKeyRelatedField(
        queryset=Customer.objects.all(), source='customer', write_only=True
    )

    class Meta:
        model = Order
        fields = ['id', 'customer', 'customer_id', 'date', 'status', 'total', 'items']

    def create(self, validated_data):
        return create_order_with_items(validated_data)


class PaymentSerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True)
    order_id = serializers.PrimaryKeyRelatedField(
        queryset=Order.objects.all(), source='order', write_only=True
    )

    class Meta:
        model = Payment
        fields = ['id', 'order', 'order_id', 'method', 'amount', 'status', 'date']
