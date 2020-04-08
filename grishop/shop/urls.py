
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^dostiopl/$', views.dostiopl, name='dostiopl'),
    url(r'^(?P<slug>[-\w]+)/$', views.catigory_ditail, name='catigory_ditail'),
    url(r'^rf/(?P<slug>[-\w]+)/$', views.pod_category_ditail, name='pod_category_ditail'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),

]