from django.db import models
from category.models import Category
from user.models import CustomUser


class Item(models.Model):
    OWNERSHIP_CHOICES = [
        ('Sole Owner', 'Sole Owner'),
        ('Joint Owner', 'Joint Owner'),
        ('Other', 'Other'),
    ]

    DISPOSITION_CHOICES = [
        ('Keep', 'Keep'),
        ('Sell', 'Sell'),
        ('Donate', 'Donate'),
        ('Other', 'Other'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    sentimental_value = models.PositiveIntegerField(choices=[(i, str(i)) for i
                                                             in range(1, 6)])
    monetary_value = models.DecimalField(max_digits=10, decimal_places=2)
    ownership_status = models.CharField(max_length=20,
                                        choices=OWNERSHIP_CHOICES)
    location = models.CharField(max_length=100)
    desired_disposition = models.CharField(max_length=50,
                                           choices=DISPOSITION_CHOICES)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                             related_name='items')

    def __str__(self):
        return self.name


class ItemImage(models.Model):
    item = models.ForeignKey(Item, related_name='images',
                             on_delete=models.CASCADE)
    image = models.ImageField(upload_to='item_images/')

    def __str__(self):
        return f"Image for {self.item.name}"
