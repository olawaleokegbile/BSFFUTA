from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField('First Name', max_length=100)
    last_name = models.CharField('Last Name', max_length=100)
    email_address = models.EmailField('Email Address', blank=True)
    level = models.CharField('Level', max_length=100)
    department = models.CharField('Department', max_length=100)
    address = models.CharField('Address', max_length=50)
    phone_number = models.CharField('Phone Number', max_length=25)


   

