from django.urls import path
from seller.views import index

urlpatterns = [
   path('' , index , name="ind" ),
  
]
