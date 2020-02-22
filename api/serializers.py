from rest_framework import serializers
from structure.models import Employee
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField


class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class CustomEmployeeSerializers(serializers.Serializer):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    first_name = serializers.CharField(max_length=50)
    second_name = serializers.CharField(max_length=50)
    address = serializers.CharField(max_length=255)
    nic_number = serializers.CharField(max_length=12)
    mobile_number = PhoneNumberField()
    email = serializers.EmailField()
    nationality = CountryField()
    date_of_birth = serializers.DateField
    sex = serializers.CharField(max_length=6)
    emergency_contact = PhoneNumberField()
    designation = serializers.CharField(max_length=100)
    department = serializers.CharField(max_length=100)
    epf_etf_number = serializers.CharField(max_length=10)
    date = serializers.DateField()
    photo = serializers.ImageField()