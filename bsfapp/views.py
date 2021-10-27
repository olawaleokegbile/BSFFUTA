from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Profile
from .form import ProfileForm
from datetime import date

# Create your views here.
def index(request):
    profiles = Profile.objects.all()
    today = date.today()
    celebrants = []
    for i in profiles:
        if i.birthday == today:
            celebrants.append(i)
    context = {
        'profiles':profiles,
        'celebrants':celebrants,
    }
    return render(request, 'index.html', context)

# def login(request):
#     return render(request, 'login.html')

# def signup(request):
#     return render(request, 'signup.html')

def profile_form(request):
    profile = Profile.objects.get(user = request.user.id)
    submitted = False
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile) #Note that request.FILES is the second positional argument used to get the image upload on the profile update to be saved in the form
        if form.is_valid():
            submitted = True
            form.save()
            #return HttpResponseRedirect('/profile_form')
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

def search_members(request):
    if request.method == "POST":
        searched = request.POST['searched']
        if len(searched)>=3 and len(searched)<=5:
            searched = searched[:3]
        
        try:
            if searched=="":
                raise Exception("Empty string")
            if Profile.objects.filter(first_name__contains=searched):
                members = Profile.objects.filter(first_name__contains=searched)
            elif Profile.objects.filter(last_name__contains=searched):
                members = Profile.objects.filter(last_name__contains=searched)

            context = {
            'searched':searched,
            'members':members,
            }
            return render(request, 'search.html', context)
        except Exception:
            return render(request, 'search.html')
    else:
        return render(request, 'search.html')