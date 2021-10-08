from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    article = models.TextField(default=None, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title
