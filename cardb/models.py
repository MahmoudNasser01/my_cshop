from django.core.validators import MinValueValidator
from django.db import models
from django.utils.text import slugify
from users.models import User, WorkshopMore, DriverMore, SellerMore
from django_resized import ResizedImageField
from django.utils.timezone import now

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
    year = models.ForeignKey(carmodel, on_delete=models.CASCADE)
    price = models.IntegerField()
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
    user_specific_id = models.CharField(max_length=50, unique=True)
    image = ResizedImageField(scale=0.5, quality=75,upload_to='products_gallery/',blank=True,null=True)

    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.ForeignKey(carmodel, on_delete=models.CASCADE)

    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):

            # إنشاء مُعرف فريد باستخدام مُعرف المستخدم وعدد المنتجات له
        self.user_specific_id = f"{str(self.user)[-4:]}-{self.created_at}"
        self.user = self.section.user

            # Generate the slug based on the product name
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)




    def __str__(self):
        return self.name



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


    delivery_type = models.CharField(max_length=20, choices=DELIVERY_TYPES)


    address = models.CharField(max_length=50)


    workshop = models.ForeignKey(WorkshopMore, on_delete=models.CASCADE)
    selermore = models.ForeignKey(SellerMore, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    phone=models.CharField(max_length=12,blank=True,null=True)

    orders = models.ManyToManyField('Order', related_name='deliveries')

    order_bollen = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.address}'s {self.delivery_type} Delivery"

    def save(self, *args, **kwargs):
        # Calculate total price based on associated orders
        total_price = sum(order.total_price for order in self.orders.all())

        # Update total_price field
        self.total_price = total_price
        if not self.phone:
            self.phone = self.selermore.phone
        super().save(*args, **kwargs)


class add_delvery(models.Model):

    STATUS_CHOICES = [
        ('active', 'active'),
        ('pending', 'pending'),
        ('rejected', 'rejected'),
        ('completed', 'completed'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')  # Default to 'موجل'
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)

