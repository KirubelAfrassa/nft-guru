import random

from django.db import models

from ..users.models import User


class Layer(models.Model):
    layerName = models.TextField()


class Image(models.Model):
    imageName = models.TextField()
    rarity = models.FloatField(default=0.5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(
        User, related_name="user", on_delete=models.CASCADE, null=True, blank=True
    )
    layer = models.ForeignKey(
        Layer,
        related_name="images",
        on_delete=models.CASCADE,
        default=random.randint(0, 999),
    )

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return "%s: %s" % (self.layer.layerName, self.imageName)
