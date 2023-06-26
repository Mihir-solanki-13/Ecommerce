from django.urls import path
from accounts.views import *
from django.contrib.auth import views as auth_views
from accounts import views as user_views
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
   path('success/',success,name="success"),
   path('logout/', auth_views.LogoutView.as_view(template_name='accounts/register.html'), name='logout'),
   # path('profile/', user_views.profile, name='profile'),
   
]
