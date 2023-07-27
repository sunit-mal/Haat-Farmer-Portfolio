from django.contrib import admin
from .models import product,FarmarDetail,PlaceOrder

@admin.register(product)
class productAdmin(admin.ModelAdmin):
    list_display = ['id', 'productImg','userName','ImgTitel','about']
    
@admin.register(FarmarDetail)
class FarmarDetailAdmin(admin.ModelAdmin):
    list_display = ['id', 'userName','number','address'] 

@admin.register(PlaceOrder)
class PlaceOrderAdmin(admin.ModelAdmin):
    list_display = ['productTitle','orderId', 'FarmerUsername','orderuser','orderaddress','number','amount']
