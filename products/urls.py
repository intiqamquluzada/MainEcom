from django.urls import path
from .views import *
app_name = 'products'

urlpatterns = [
    path('list/', product_list_view, name='list'),
    path('create/', product_create_view, name='create'),
]
