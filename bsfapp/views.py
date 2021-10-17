from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Profile
from .form import ProfileForm

# Create your views here.
def index(request):
    profiles = Profile.objects.all()
    return render(request, 'index.html', {'profiles': profiles})

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def profile_form(request):
    profile = Profile.objects.get(user = request.user.id)
    submitted = False
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contact_form?submitted=True')
    else:
        form = ProfileForm
        if 'submitted' in request.GET:
            submitted = True

    context = {
        'profile':profile,
        'form':form,
        'submitted': submitted,
    }
    return render(request, 'profile.html', context)

def base(request):
    return render(request, 'base.html')