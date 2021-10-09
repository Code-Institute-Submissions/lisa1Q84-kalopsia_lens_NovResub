from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from decimal import Decimal


def bag_contents(request):

    bag_items = []
    bag_total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            bag_total += item_data * product.price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for variation, quantity in item_data['variation_dict'].items():
                variation_object = Variation.objects.get(name__icontains=variation)
                bag_total += quantity * product.price
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'variation': variation,
                })

        if bag_total < settings.FREE_DELIVERY_MIN:
            delivery_charge = Decimal(settings.DELIVERY_CHARGE)
            free_delivery_delta = settings.FREE_DELIVERY_MIN - bag_total
        else:
            delivery_charge = 0
            free_delivery_delta = 0

        bag_grand_total = delivery_charge + bag_total

        context = {
            'bag_items': bag_items,
            'product_count': product_count,
            'bag_total': bag_total,
            'free_delivery_delta': free_delivery_delta,
            'free_delivery_min': settings.FREE_DELIVERY_MIN,
            'bag_grand_total': bag_grand_total,
            'delivery_charge': delivery_charge,
            }

        return context
