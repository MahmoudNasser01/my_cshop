from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.gis.db import models as geomodels
# Create your model here.
from django.utils.text import slugify
from users.models import User


class MyModel(models.Model):
    id = models.AutoField(primary_key=True)


class CountryCar(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=2)
    def __str__(self):
        return self.name

# create company car one-to many conutrycar
class CompanyCar(models.Model):
    name = models.CharField(max_length=100)
    countrycar = models.ForeignKey(CountryCar, on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class carmodel(models.Model):
    year = models.IntegerField()
    manufacturer = models.ForeignKey(CompanyCar, on_delete=models.CASCADE)



# create car name one-to-many companycar
class CarName(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    companycar = models.ForeignKey(CompanyCar, on_delete=models.CASCADE)
    year=models.ForeignKey(carmodel,on_delete=models.CASCADE)
    price=models.IntegerField()
    color = models.CharField(max_length=50)
    fuel_type = models.CharField(max_length=50)
    def __str__(self):
        return self.name



# in this i will create Sections and Products for work shop
class Sections(models.Model):
    countrycar = models.ForeignKey(CountryCar, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Products(models.Model):
    section = models.ForeignKey(Sections, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.ForeignKey(carmodel, on_delete=models.CASCADE)

    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):

        self.user = self.section.user
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name

#create order

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])  # Add quantity field
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        # Calculate total price before saving the order

        self.total_price = self.product.price * self.quantity

        super().save(*args, **kwargs)



    def __str__(self):
        return self.product.name

class Delivery(models.Model):
    DELIVERY_TYPES = [
        ('fast', 'Fast'),
        ('economical', 'Economical'),
    ]
    STATUS_CHOICES = [
        ('active', 'active'),
        ('pending', 'pending'),
        ('rejected', 'rejected'),
        ('completed', 'completed'),
    ]

    delivery_type = models.CharField(max_length=20, choices=DELIVERY_TYPES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')  # Default to 'موجل'


    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    location = geomodels.PointField(null=True,)
    orders = models.ManyToManyField('Order', related_name='deliveries')
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    order_bollen=models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.phone)
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.name}'s {self.delivery_type} Delivery"


class add_delvery(models.Model):
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)

