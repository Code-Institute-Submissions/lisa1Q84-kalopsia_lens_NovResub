# Generated by Django 3.2.5 on 2021-09-26 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_auto_20210926_0925'),
        ('products', '0006_remove_variation_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='has_variation',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.DeleteModel(
            name='Variation',
        ),
    ]