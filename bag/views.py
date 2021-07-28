from django.shortcuts import render

"""a view to return the shopping bag page"""


def view_bag(request):
    return render(request, 'bag/bag.html')


"""a view to add items to the shopping bag"""


def add_to_bag(request, item_id):
    quantity = int(request.POST.get('quantity'))
    variation = request.POST.get('variation')

    bag = request.session.get('bag', {})

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
    return render(request, 'bag/bag.html')
