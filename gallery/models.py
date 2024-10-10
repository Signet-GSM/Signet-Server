from django.db import models


class Gallery(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    view = models.IntegerField(default=0)
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
