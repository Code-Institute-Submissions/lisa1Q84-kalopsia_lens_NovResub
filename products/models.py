from django.db import models

# Create your models here.


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class VariationManager(models.Manager):
    def all(self):
        return super(VariationManager, self).filter(active=True)

    def types(self):
        return self.all().filter(category='type')

    def durations(self):
        return self.all().filter(category='duration')


VAR_CATEGORIES = (
    ('type', 'type'),
    ('duration', 'duration')
)


class Variation(models.Model):
    category = models.CharField(max_length=120, choices=VAR_CATEGORIES, default='type')
    image = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    active = models.BooleanField(default=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    objects = VariationManager()

    def __str__(self):
        return self.name
