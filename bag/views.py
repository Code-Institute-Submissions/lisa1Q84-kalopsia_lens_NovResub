from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from products.models import Product, Variation
from django.contrib import messages


"""a view to return the shopping bag page"""


def view_bag(request):
    return render(request, 'bag/bag.html')


"""a view to add items to the shopping bag"""


def add_to_bag(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    for item in request.POST:
        key = item
        val = request.POST[key]
    if 'variation' in request.POST:
        variation = request.POST['variation']
        print(type)
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

     context = {
        'product': product,
        'variation': variation
    }

    request.session['bag'] = bag
    
    return render(request, 'bag/bag.html', context)