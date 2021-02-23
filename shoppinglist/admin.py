from django.contrib import admin
from shoppinglist.models import ShoppingList, Item

# Register your models here.

@admin.register(ShoppingList)
class ShoppingListAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_date', 'last_modified_date']

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'description']