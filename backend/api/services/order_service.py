from api.models import Order, OrderItem, Product


def create_order_with_items(validated_data):
    """
    Crée une commande, calcule le total, ajuste le stock.
    """
    items_data = validated_data.pop('items')
    order = Order.objects.create(**validated_data)

    total = 0
    for item_data in items_data:
        product = item_data['product']
        quantity = item_data['quantity']
        price = product.price

        # Crée l'item de commande
        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=quantity,
            price=price
        )

        # Ajuste le stock produit
        product.stock -= quantity
        product.save()

        # Calcule le total
        total += quantity * price

    order.total = total
    order.save()

    return order
