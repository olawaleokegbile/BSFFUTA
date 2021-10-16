from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Contact
from .form import ContactForm

# Create your views here.
def index(request):
    contacts = Contact.objects.all()
    return render(request, 'index.html', {'contacts': contacts})

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def contact_form(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contact_form?submitted=True')
    else:
        form = ContactForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'form.html', {'form': form, 'submitted': submitted})

def base(request):
    return render(request, 'base.html')