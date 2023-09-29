from django.contrib import admin
from .models import Product,Stock,StockIn,StockOut,Payment_confirmation,CustomUser

# Register your models here.
admin.site.register(Product)
admin.site.register(Stock)
admin.site.register(StockIn)
admin.site.register(StockOut)
admin.site.register(Payment_confirmation)
admin.site.register(CustomUser)