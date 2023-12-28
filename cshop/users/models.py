from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


# Create your model here.
class User(AbstractUser, PermissionsMixin):
    class Types(models.TextChoices):
        SELLER = "SELLER", "Seller"
        WORKSOHP = "WORKSHOP", "Workshop"

        DRIVER = "DRIVER", "Driver"
        ADMIN = "ADMIN", "ADMIN"

    base_type = Types.ADMIN

    # What type of user are we?
    type = models.CharField(
        _("Type"), max_length=50, choices=Types.choices, default=base_type, null=True, blank=True
    )

    # Name of User
    name = models.CharField(_("Name of User"), blank=True, max_length=255)

    # Phone number field with validation
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Please enter a valid phone number")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, unique=True)

    USERNAME_FIELD = 'phone_number'
    EMAIL_FIELD = 'phone_number'  # Set EMAIL_FIELD to the same as USERNAME_FIELD

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    def save(self, *args, **kwargs):
        if not self.pk:
            self.set_password(self.password)
        if not self.id:
            self.type = self.base_type

        return super().save(*args, **kwargs)

class SELLERMANGER(models.Manager):
    def normalize_email(self, email):
        """
        Normalize the email address by lowercasing the domain part of it.
        """
        email = email or ''
        try:
            email_name, domain_part = email.strip().rsplit('@', 1)
        except ValueError:
            pass
        else:
            email = '@'.join([email_name, domain_part.lower()])
        return email

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.SELLER)

class DriverManager(models.Manager):
    def normalize_email(self, email):
        """
        Normalize the email address by lowercasing the domain part of it.
        """
        email = email or ''
        try:
            email_name, domain_part = email.strip().rsplit('@', 1)
        except ValueError:
            pass
        else:
            email = '@'.join([email_name, domain_part.lower()])
        return email

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.DRIVER)

class WORKSOHPManager(models.Manager):
    def normalize_email(self, email):
        """
        Normalize the email address by lowercasing the domain part of it.
        """
        email = email or ''
        try:
            email_name, domain_part = email.strip().rsplit('@', 1)
        except ValueError:
            pass
        else:
            email = '@'.join([email_name, domain_part.lower()])
        return email

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.WORKSOHP)

class COUSTEMManager(models.Manager):
    def normalize_email(self, email):
        """
        Normalize the email address by lowercasing the domain part of it.
        """
        email = email or ''
        try:
            email_name, domain_part = email.strip().rsplit('@', 1)
        except ValueError:
            pass
        else:
            email = '@'.join([email_name, domain_part.lower()])
        return email

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.ADMIN)



# in this we cearte more
# user type just driver

class DriverMore(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=11)
    address=models.CharField(max_length=100)

class SellerMore(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    phone=models.IntegerField()
    address=models.CharField(max_length=100)
    car=models.CharField(max_length=100)

class WorkshopMore(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    phone=models.IntegerField()
    address=models.CharField(max_length=100)
    cartypes=models.CharField(max_length=100)




class Driver(User):

    base_type = User.Types.DRIVER
    objects = DriverManager()



    @property
    def more(self):
        return self.DriverMore

    class Meta:
        proxy = True


    def accelerate(self):
        return "Go faster"


class Seller(User):
    base_type = User.Types.SELLER
    objects = SELLERMANGER()

    @property
    def more(self):
        return self.SellerMore

    class Meta:
        proxy = True

    def accelerate(self):
        return "Go faster"
class Workshop(User):
    base_type = User.Types.WORKSOHP
    objects = WORKSOHPManager()



    class Meta:
        proxy = True

    def accelerate(self):
        return "Go faster"
class Customer(User):
    base_type = User.Types.ADMIN
    objects = COUSTEMManager()


    class Meta:
        proxy = True

    def accelerate(self):
        return "Go faster"