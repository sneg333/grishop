from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('contact/', views.contact, name='contact'),
    path('prodall/', views.prodall, name='prodall'),
    path('dostiopl/', views.dostiopl, name='dostiopl'),
    path('<slug:slug>/', views.catigory_ditail, name='catigory_ditail'),
    path('prodall/<slug:slug>/', views.pod_category_ditail, name='pod_category_ditail'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),

]
