from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class customer(models.Model):
    live=1
    delete=0
    delete_choices=((live,'Live'),(delete,'Delete' ))
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=15)
    address=models.TextField()
    user=models.OneToOneField(User ,on_delete=models.CASCADE,related_name='cutomer_profile')
    delete =models.IntegerField(choices=delete_choices,default=live)    
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
