from django.db import models

# Create your models here.

class ShoppingList(models.Model):
    name = models.CharField(max_length=30)
    last_modified_date = models.DateField(auto_now=True)
    created_date = models.DateField(auto_now_add=True)
    items = models.ManyToManyField('Item', blank=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

