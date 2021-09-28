from django.db import models
from profiles.models import UserProfile
from products.models import Product


class Wishlist(models.Model):
    """ A model to make the connection between a bookmarked product and a user """
    user = models.OneToOneField(UserProfile, null=False, blank=False, on_delete=models.CASCADE, related_name='wishlist')

    

    def __str__(self):
        return f'Wishlist ({self.user})'


class WishlistItem(models.Model):
    """A many to many model to put products on the wishlist"""
    wishlist = models.ForeignKey(Wishlist, null=False, blank=False, on_delete=models.CASCADE, related_name='wishlist_items')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE, related_name='wishlist_products')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name