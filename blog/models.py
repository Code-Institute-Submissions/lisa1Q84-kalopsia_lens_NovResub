from django.db import models


class BlogPost(models.Model):
    """
    Model for a basic blog post with title, article and date
    """
    title = models.CharField(
        max_length=52,
        null=False,
        blank=False
    )

    article = models.TextField(
        max_length=450,
        null=False,
        blank=False
    )

    date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title