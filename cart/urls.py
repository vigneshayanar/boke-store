from django.urls import path
from . import views

urlpatterns = [
    path('cart/',views.cart_sum,name='cart_sum'),
    path('add_cart/',views.cart_add,name='cart_add'),
    path('delete/',views.cart_update,name='cart_update'),
    path('update/ ',views.cart_delete,name='cart_delete'),
]