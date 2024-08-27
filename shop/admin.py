from django.contrib import admin
from .models import Category,Product,Shipment,Order,Payment,Cart


# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Shipment)
admin.site.register(Order)
admin.site.register(Payment)