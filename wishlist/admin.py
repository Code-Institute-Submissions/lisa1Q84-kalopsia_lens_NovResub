# Register your models here.
from django.contrib import admin
from wishlist.models import Wishlist, WishlistItem

admin.site.register(Wishlist)
admin.site.register(WishlistItem)
