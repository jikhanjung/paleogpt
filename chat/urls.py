from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('chat_index', views.chat_index, name='chat_index'),
    path('collection_tree', views.collection_tree, name='collection_tree'),
    path('item_list/<str:colkey>', views.item_list, name='item_list'),
    path('item_check/<str:itemkey>', views.item_check, name='item_check'),
]