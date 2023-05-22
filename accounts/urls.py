from django.urls import path
from accounts.views import *
# from products.views import 
# app_name = 'accounts'
urlpatterns = [
   path('login/' , login_page , name="login" ),
   path('register/' , register_page , name="register"),
   path('activate/<email_token>/' , activate_email , name="activate_email"),
   path('cart/',cart,name = "cart"),
   path('add-to-cart/<uid>/',add_to_cart,name = "add_to_cart"),
   path('remove-cart/<cart_item_uid>/',remove_cart,name = "remove_cart"),
   path('remove-coupon/<uid>/',remove_coupon,name = "remove_coupon"),
   path('success/',success,name="success")
]
