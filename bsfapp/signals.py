from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile

def user_profile(sender, instance, created, **kwargs):
    if created:
        try:
            Profile.objects.create(user=instance, 
                first_name = instance.first_name, 
                last_name = instance.last_name, 
                email_address = instance.email)
            print("Profile created")
        except Exception:
            pass

post_save.connect(user_profile, sender=User)