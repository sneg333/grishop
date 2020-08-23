from django.urls import path, re_path
from .views import item_list

app_name = 'order'

urlpatterns = [

    path('orderitem/', item_list, name='item-list'),
]