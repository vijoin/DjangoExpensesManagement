from django.contrib.auth.models import User
from django.db import models
from products.models import Product


class Expense(models.Model):
    date = models.DateField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses')
    product_id = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='expenses')
    amount = models.FloatField()

    def __str__(self):
        return f"{self.product_id} ({self.date.strftime('%d/%m/%Y')})"
