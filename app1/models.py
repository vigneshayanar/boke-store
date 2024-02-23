from django.db import models
import datetime
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    frist_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email_id=models.EmailField(max_length=100)
    phone_no=models.CharField(max_length=10)
    password=models.CharField(max_length=100)

    def __str__(self):
        return f'{self.frist_name} {self.last_name}'
    
class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.DecimalField(default=0,max_digits=10, decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    description=models.CharField(max_length=250,default='',blank=True,null=True)
    image=models.ImageField(upload_to='uploads/product/')
    is_sale=models.BooleanField(default=False)
    sale_price=models.DecimalField(default=0,max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey(Category,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    address=models.CharField(max_length=100,default='',blank=True)
    phone=models.CharField(max_length=10)
    date=models.DateField(default=datetime.datetime.today)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.product

