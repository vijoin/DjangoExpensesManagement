from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=120)
    picture = models.ImageField(upload_to='products/pictures')

    def __str__(self):
        return f"{self.name}"