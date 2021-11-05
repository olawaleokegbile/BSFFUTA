from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):

    # No_Unit = 'No Unit'
    # Bible_Study_Unit = 'Bible Study Unit'
    # Welfare_Unit = 'Welfare Unit'
    # Evangelism_Unit = 'Evangelism Unit'
    # Publicity_Unit = 'Publicity Unit'
    # Organizing_Unit = 'Organizing Unit'
    # Ushering_Unit = 'Ushering Unit'
    # Choir_Unit = 'Choir Unit'
    # Academic_Unit = 'Academic Unit'
    # Drama_Unit = 'Drama Unit'
    # Prayer_Unit = 'Prayer Unit'

    UNIT_CHOICES = [
        ('No Unit', 'No Unit'),
        ('Bible Study Unit', 'Bible Study Unit'),
        ('Welfare Unit', 'Welfare Unit'),
        ('Evangelism Unit', 'Evangelism Unit'),
        ('Publicity Unit', 'Publicity Unit'),
        ('Organizing Unit', 'Organizing Unit'),
        ('Ushering Unit', 'Ushering Unit'),
        ('Choir Unit', 'Choir Unit'),
        ('Academic Unit', 'Academic Unit'),
        ('Drama Unit', 'Drama Unit'),
        ('Prayer Unit', 'Prayer Unit')
    ]

    AREA_CHOICES = [
        ('Apatapiti', 'Apatapiti'),
        ('West Gate', 'West Gate'),
        ('Stateline', 'Stateline'),
        ('Akindeko', 'Akindeko'),
        ('Jibowu', 'Jibowu'),
        ('New Hostel male', 'New Hostel male'),
        ('New Hostel female', 'New Hostel female'),
        ('Road Block', 'Road Block'),
        ('Secretariat Area', 'Secretariat Area'),
        ('North Gate', 'North Gate'),
        ('Zion-Alejolowo', 'Zion-Alejolowo'),
        ('Jadesola', 'Jadesola'),
        ('Adeniyi', 'Adeniyi'),
        ('Abiola', 'Abiola'),
        ('WESCO area', 'WESCO area'),
        ('FUTASCOOPS', 'FUTASCOOPS'),
        ('Akad', 'Akad'),
        ('BSF Auditorium area', 'BSF Auditorium area'),
        ('Cassava/Oritaobele area', 'Cassava/Oritaobele area'),
        ('Embassy', 'Embassy'),
        ('Aba Area', 'Aba Area'),
        ('Redemption Area', 'Redemption Area'),
        ('Other', 'Other')
    ]

    LEVEL_CHOICES = [
        ('100 Level', '100 Level',),
        ('200 Level', '200 Level'),
        ('Pre-degree/UABS', 'Pre-degree/UABS'),
        ('300 Level', '300 Level'),
        ('400 Level', '400 Level'),
        ('Final Year', 'Final Year'),
        ('Other', 'Other')
    ]

    GENDER_CHOICES = [
        ('male', 'male'),
        ('female', 'female'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField('First Name', max_length=100, null='False')
    last_name = models.CharField('Last Name', max_length=100, null='False')
    gender = models.CharField(max_length=50, choices= GENDER_CHOICES, default='NA', null='False')
    email_address = models.EmailField('Email Address', blank=True, unique=True)
    level = models.CharField(max_length=50, choices= LEVEL_CHOICES, default='Other', null='False')
    department = models.CharField('Department', max_length=100, null='False', default='NA')
    unit = models.CharField(max_length=50, choices= UNIT_CHOICES, default='No Unit', null='False')
    area = models.CharField(max_length=50, choices= AREA_CHOICES, default='Other', null='False')    
    address = models.CharField('Address', max_length=50, null='False', default='NA')
    phone_number = models.CharField('Phone Number', max_length=25, null='False', default='NA')
    birthday = models.DateField('Birthday', auto_now=False, auto_now_add=False, null='False', default='2000-01-01')
    avatar = models.ImageField(default='avatar.png', upload_to='avatars/')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


   

