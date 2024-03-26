from django.contrib import admin

# Register your model here.
from .models import User, Driver, DriverMore, Seller, Workshop,WorkshopMore, Customer,SellerMore

admin.site.register(User)
admin.site.register(Driver)
admin.site.register(Seller)
admin.site.register(Workshop)
admin.site.register(WorkshopMore)
admin.site.register(DriverMore)
admin.site.register(SellerMore)
admin.site.register(Customer)