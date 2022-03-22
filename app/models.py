from django.db import models

# Create your models here.

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    contact_no =models.CharField(max_length=100, null=True)
    pincode = models.IntegerField()

    def __str__(self):
        return self.first_name

 
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True)
    unit_price = models.FloatField(null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, null=True, on_delete = models.SET_NULL)
    product_id = models.ForeignKey(Product, null=True, on_delete = models.SET_NULL)
    quantity = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    total_price = models.FloatField(null=True)
    unit_price = models.FloatField(null=True)
    
    # def __str__(self):
    #     return self.
    



