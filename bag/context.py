from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product, Variation
from decimal import Decimal


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    print(bag)

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for variation, quantity in item_data['variation_dict'].items():
                print(variation)
                variation_object = Variation.objects.get(name__icontains=variation)
                total += quantity * variation_object.price
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'variation': variation_object,
                })

    grand_total = total
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return context
