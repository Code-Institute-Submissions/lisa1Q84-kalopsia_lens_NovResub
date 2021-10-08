from django.contrib import admin

from .models import BlogPost


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'date',
    )


admin.site.register(BlogPost, PostAdmin)