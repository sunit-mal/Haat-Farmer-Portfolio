from django.db import models

class product(models.Model):
    productImg = models.ImageField(upload_to='Media')
    ImgTitel = models.CharField( max_length=50,default='')
    about = models.CharField( max_length=150,default='')
    userName = models.CharField( max_length=20)

class FarmarDetail(models.Model):
    userName = models.CharField(max_length=50,default='')
    number = models.IntegerField(max_length=10,default='')
    address = models.CharField(max_length=255,default='')

class PlaceOrder(models.Model):
    productTitle = models.CharField(max_length=150,default='')
    orderId = models.IntegerField(max_length=10,default='')
    FarmerUsername = models.CharField( max_length=255,default='')
    orderuser = models.CharField( max_length=255,default='')
    orderaddress = models.CharField( max_length=255,default='')
    number = models.IntegerField(max_length=10,default='')
    amount = models.CharField( max_length=255,default='')
