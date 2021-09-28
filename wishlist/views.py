from django.shortcuts import render, redirect, reverse, HttpResponse, get_list_or_404, get_object_or_404

from .models import Product, UserProfile, Wishlist, WishlistItem

from django.contrib.auth.decorators import login_required

from django.utils import timezone

from django.contrib import messages


@login_required
def wishlist(request):
    """ A view to show an existing wishlist """
    items = []
    user = get_object_or_404(UserProfile, user=request.user)
    wishlist = Wishlist.objects.get_or_create(user=user)
    wishlist_user = wishlist[0]
    existingWishlist = WishlistItem.objects.filter(wishlist=wishlist_user).exists()

    if existingWishlist:
        user_wishlist = get_list_or_404(WishlistItem, wishlist=wishlist_user)
        for obj in user_wishlist:
            product = get_object_or_404(Product, name=obj)
            items.append(product)
        context = {
            'wishlist': True,
            'products': items
        }
        messages.info(request, 'The item was added to your wishlist')
        return render(request, 'wishlist/wishlist.html', context)

    else:
        context = {
            'wishlist': False,
        }
        return render(request, 'wishlist/wishlist.html', context)

