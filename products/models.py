from django.db import models

# model for product 
class product(models.Model):
    live=1
    delete=0
    delete_choices=((live,'Live'),(delete,'Delete' ))
    title =models.CharField(max_length=200)
    price=models.FloatField()
    description=models.TextField()
    image=models.ImageField(upload_to='media/')
    priority=models.IntegerField(default=0)
    delete_status=models.IntegerField(choices=delete_choices,default=live)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


