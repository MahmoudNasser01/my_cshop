from django.contrib import admin

# Register your model here.

from .models import CountryCar, CompanyCar, CarName, \
    carmodel, Sections, Products, Order, Delivery

admin.site.register(CountryCar)
admin.site.register(CompanyCar)
admin.site.register(CarName)
admin.site.register(carmodel)


# for products
admin.site.register(Sections)
admin.site.register(Products)
admin.site.register(Order)
