from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)


"""a view to return the shopping bag page"""


def view_bag(request):
    return render(request, 'bag/bag.html')


"""a view to add items to the shopping bag"""


def add_to_bag(request, item_id):
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
            else:
                bag[item_id]['variation_dict'][variation] = quantity
        else:
            bag[item_id] = {'variation_dict': {variation: quantity}}
    else:

        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)


"""a view to UPDATE items quantity in the shopping bag"""


def update_bag(request, item_id):
    quantity = int(request.POST.get('quantity'))
    variation = request.POST.get('variation')

    bag = request.session.get('bag', {})

    if 'variation' in request.POST:
        variation = request.POST['variation']
    bag = request.session.get('bag', {})

    if variation:
        if quantity > 0:
            bag[item_id]['variation_dict'][variation] = quantity
        else:
            del bag[item_id]['variation_dict'][variation]
    else:

        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop[item_id]

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


"""a view to REMOVE an item in the shopping bag"""


def remove_from_bag(request, item_id):

    try:
        if 'variation' in request.POST:
            variation = request.POST['variation']
        bag = request.session.get('bag', {})

        if variation:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
        else:
            bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)
        
    except Exception as e:
        return HttpResponse(status=500)

