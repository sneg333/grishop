from django.urls import path, re_path
from . import views

app_name = 'order'
urlpatterns = [
    path('create/', views.order_create),
]