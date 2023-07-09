from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from base.models import BaseModel


class Seller(BaseModel):
    # id = models.AutoField()
    seller = models.OneToOneField(User, on_delete=models.CASCADE, related_name="seller")
    is_verified = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.seller)