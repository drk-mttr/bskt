from django.shortcuts import render
from shoppinglist.models import ShoppingList, Item

# Create your views here.

def ShoppingListList(request):
    lists = ShoppingList.objects.all()
    return render(request, 'shoppinglist/shoppinglist_list.html', {'lists': lists})

def ShoppingListDetail(request, shoppinglist_id):
    list = ShoppingList.objects.get(pk=shoppinglist_id)
    items = list.items.all()
    return render(request, 'shoppinglist/shoppinglist_detail.html', {'items': items, 'list': list})