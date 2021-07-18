from django.conf import settings


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0

    grand_total = total
    context = {
        bag_items,
        total,
        product_count,
        grand_total,
    }

    return context
