from django import forms
from django import forms
from .models import Profile
from functools import partial

DateInput = partial(forms.DateInput, {'class': 'datepicker'})

#create a contact form
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email_address', 'level', 'department', 'unit', 'area', 'address', 'phone_number', 'birthday', 'avatar')        
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email_address': forms.EmailInput(attrs={'class': 'form-control'}),
            'level': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'birthday': DateInput()
        }