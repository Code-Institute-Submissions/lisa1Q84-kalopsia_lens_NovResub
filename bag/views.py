from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from products.models import Product, Variation
from django.contrib import messages



def view_bag(request):
    """ a view to return the shopping bag page"""
    return render(request, 'bag/bag.html')

    """ a view to add items to the shopping bag"""

def add_to_bag(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    for item in request.POST:
        key = item
        val = request.POST[key]
    if 'type' in request.POST:
        type = request.POST['type']
        print(type)
    if 'duration' in request.POST:
        duration = request.POST['duration']
        print(duration)
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return HttpResponseRedirect(reverse("view_bag"))
