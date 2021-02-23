from django.urls import path
from shoppinglist.views import ShoppingListList, ShoppingListDetail

urlpatterns = [
    path('', ShoppingListList, name='shoppinglist_list'),
    path('<int:shoppinglist_id>/', ShoppingListDetail, name='shoppinglist_items'),
]