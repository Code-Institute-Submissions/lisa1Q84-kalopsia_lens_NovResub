from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages
from products.models import Product


"""a view to return the shopping bag page"""


def view_bag(request):
    return render(request, 'bag/bag.html')


"""a view to add items to the shopping bag"""


def add_to_bag(request, item_id):
    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    variation = request.POST.get('variation')
    redirect_url = request.POST.get('redirect_url')

    if 'variation' in request.POST:
        variation = request.POST['variation']

    bag = request.session.get('bag', {})

    if variation:
        if item_id in list(bag.keys()):
            if variation in bag[item_id]['variation_dict'].keys():
                bag[item_id]['variation_dict'][variation] += quantity
                messages.success(
                    request, f'updated the quantity of {variation}{product.name} to {bag[item_id]["variation_dict"][variation]}!')

            else:
                bag[item_id]['variation_dict'][variation] = quantity
                messages.success(request, f'added variation {variation.upper()}{product.name} to your bag!')

        else:
            bag[item_id] = {'variation_dict': {variation: quantity}}
            messages.success(request, f'added {variation.upper()}{product.name} to your bag!')

    else:

        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'updated {product.name} quantity to {bag[item_id]}!')

        else:
            bag[item_id] = quantity
            messages.success(request, f'added {product.name} to your bag!')

    request.session['bag'] = bag
    return redirect(redirect_url)


"""a view to UPDATE items quantity in the shopping bag"""


def update_bag(request, item_id):
    quantity = int(request.POST.get('quantity'))
    variation = request.POST.get('variation')
    product = get_object_or_404(Product, pk=item_id)

    bag = request.session.get('bag', {})

    if 'variation' in request.POST:
        variation = request.POST['variation']
    bag = request.session.get('bag', {})

    if variation:
        if quantity > 0:
            bag[item_id]['variation_dict'][variation] = quantity
            messages.success(request, f'updated quantity of {variation} to {bag[item_id]["variation_dict"][variation]}!')

        else:
            del bag[item_id]['variation_dict'][variation]
            messages.success(
                request, f'removed {variation.upper()}{product.name} from your bag!')

    else:

        if quantity > 0:
            bag[item_id] = quantity
            messages.success(
                request, f'updated quantity of {product.name} to {bag[item_id]}!')

        else:
            bag.pop[item_id]
            messages.success(
                request, f'updated quantity of {product.name} to to {bag[item_id]}')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


"""a view to REMOVE an item in the shopping bag"""


def remove_from_bag(request, item_id):

    product = get_object_or_404(Product, pk=item_id)

    try:
        if 'variation' in request.POST:
            variation = request.POST['variation']
        bag = request.session.get('bag', {})

        if variation:
            del bag[item_id]['variation.dict'][variation]
            messages.success(request, f'removed {variation.upper()}{product.name} from your bag!')
            if not bag[item_id]['variation.dict']:
                bag.pop(item_id)
                messages.success(request, f'removed {variation.upper()}{product.name} from your bag!')
        else:
            bag.pop(item_id)
            messages.success(
                request, f'removed {product.name} from your bag!')

        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'error removing item: {e}')
        return HttpResponse(status=500)
