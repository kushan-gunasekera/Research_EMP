from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField


# Create your models here.
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    nic_number = models.CharField(max_length=12)
    mobile_number = PhoneNumberField()
    email = models.EmailField()
    nationality = CountryField()
    date_of_birth = models.DateField()
    sex = models.CharField(max_length=6)
    emergency_contact = PhoneNumberField()
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    epf_etf_number = models.CharField(max_length=10)
    date = models.DateField()
    photo = models.ImageField(upload_to=None)
