from django.db import models

# Create your models here.
class order(models.Model):
    live=1
    delete=0
    delete_choices=((live,'Live'),(delete,'Delete' ))
    cart_stage=0
    order_confirmed=1
    order_processed=2
    order_delivered=3
    order_rejected=4
    status_choice=((order_confirmed,'Order Confirmed'),(order_processed,'Order Processed'),(order_delivered,'Order Delivered'),(order_rejected,'Order Rejected' ))
    order_status=models.IntegerField(choices=status_choice,default=cart_stage) 


    owner=models.ForeignKey('customers.customer',on_delete=models.SET_NULL,related_name='cart_owner', null=True)
    delete_status=models.IntegerField(choices=delete_choices,default=live)    
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

 
    
class orderedItems(models.Model):
    product=models.ForeignKey('products.product',related_name='cart_product' ,on_delete=models.SET_NULL, null=True)
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(order,on_delete=models.CASCADE,related_name='added_items')
