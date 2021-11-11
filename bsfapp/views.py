from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Profile
from .form import ProfileForm
from datetime import date
from django.core.mail import send_mail, EmailMessage


# Create your views here.
def index(request):
    try:
        profile = Profile.objects.get(user = request.user.id)
        # profiles = Profile.objects.all()
        # today = date.today()
        # celebrants = []
        # for i in profiles:
        #     if i.birthday == today:
        #         celebrants.append(i)
        # context = {
        #     'profiles':profiles,
        #     'celebrants':celebrants,
        #     'profile':profile,
        # }
        # return render(request, 'index.html', context)
    except:
        return render(request, 'index.html')
    profiles = Profile.objects.all()
    today = date.today()
    celebrants = []
    for i in profiles:
        if i.birthday == today:
            celebrants.append(i)

    #This is birthday email section
    #This section allows for automatic sending of birthday messages to all members' emails and
    #the celebrant's email
    if celebrants:
        
        for j in celebrants:
            name = str(j.first_name)+" "+str(j.last_name)
            email = j.email_address
            phone = j.phone_number
            subject = 'CELEBRATE WITH '+str(name)
            celebrant_subject = 'HAPPY BIRTHDAY '+str(name)

            data = {'name':name, 'email':email, 'phone':phone, 'subject':subject, 'celebrant_subject':celebrant_subject}

            message = '''
                It's the birthday of a rare gem.
                The Joyous Family celebrates {} on this special day.

                Say a word of prayer for {} and ensure to send your wishes.
                
            '''.format(data['name'], data['name'])
            celebrant_message = '''
                Dear {},

                We celebrate you on this very special day and we pray that you continually abound in joy.
                Many happy returns



                Cheers!
                From the Joyous Family
            '''.format(data['name'])
            #send_mail(data['subject'], message, 'stemedgeinitiative@gmail.com', ['rasholajuwon@gmail.com'], fail_silently=False)
            msg = EmailMessage(data['subject'], message, to=[i.email_address for i in profiles])
            msg.send()
            celebrant_msg = EmailMessage(data['celebrant_subject'], celebrant_message, to=[data['email']])
            celebrant_msg.send()
    #Email section ended

    context = {
        'profiles':profiles,
        'celebrants':celebrants,
        'profile':profile,
    }
    return render(request, 'index.html', context)

# def login(request):
#     return render(request, 'login.html')

# def signup(request):
#     return render(request, 'signup.html')

def profile_form(request):
    # profile = Profile.objects.create(user=self.user, 
    #         first_name = self.user.first_name, 
    #         last_name = self.user.last_name, 
    #         email_address = self.user.email)
    try:
        profile = Profile.objects.get(user = request.user.id)
        submitted = False
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES, instance=profile) #Note that request.FILES is the second positional argument used to get the image upload on the profile update to be saved in the form
            if form.is_valid():
                submitted = True
                form.save()
                return HttpResponseRedirect('/my_profile')
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
    except Exception as e:
        return render(request, 'profile.html')

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

def members_list(request):
    if request.method == "POST":
        query = str(request.POST['query']).lower()
        
        try:
            if "100"in query:
                members = Profile.objects.filter(level__contains='1')
            elif "200" in query:
                members = Profile.objects.filter(level__contains='2')
            elif "300" in query:
                members = Profile.objects.filter(level__contains='3')
            elif "400" in query:
                members = Profile.objects.filter(level__contains='4')
            elif "500" in query:
                members = Profile.objects.filter(level__contains='Final')
            elif "bible" in query:
                members = Profile.objects.filter(unit__contains='Bible')
            elif "prayer" in query:
                members = Profile.objects.filter(unit__contains='Prayer')
            elif "publicity" in query:
                members = Profile.objects.filter(unit__contains='Publicity')
            elif "organizing" in query:
                members = Profile.objects.filter(unit__contains='Organizing')
            elif "ushering" in query:
                members = Profile.objects.filter(unit__contains='Ushering')
            elif "choir" in query:
                members = Profile.objects.filter(unit__contains='Choir')
            elif "academic" in query:
                members = Profile.objects.filter(unit__contains='Academic')
            elif "drama" in query:
                members = Profile.objects.filter(unit__contains='Drama')
            elif "welfare" in query:
                members = Profile.objects.filter(unit__contains='Welfare')
            elif "evangelism" in query:
                members = Profile.objects.filter(unit__contains='Evangelism')
            elif query=="female":
                members = Profile.objects.filter(gender__startswith='fe')
            elif query=="male":
                members = Profile.objects.filter(gender__startswith='ma') 
            elif "apatapiti" in query:
                members = Profile.objects.filter(area__contains='Apatapiti')
            elif "west" in query:
                members = Profile.objects.filter(area__contains='West')
            elif "stateline" in query:
                members = Profile.objects.filter(area__contains='Stateline')  
            elif "akindeko" in query:
                members = Profile.objects.filter(area__contains='Akindeko')
            elif "jibowu" in query:
                members = Profile.objects.filter(area__contains='Jibowu') 
            elif "male" in query:
                members = Profile.objects.filter(area__contains='New Hostel male') 
            elif "female" in query:
                members = Profile.objects.filter(area__contains='female') 
            elif "road" in query:
                members = Profile.objects.filter(area__contains='Road')
            elif "secretariat" in query:
                members = Profile.objects.filter(area__contains='Secretariat')
            elif "north" in query:
                members = Profile.objects.filter(area__contains='North')
            elif "zion" in query:
                members = Profile.objects.filter(area__contains='Zion')
            elif "jadesola" in query:
                members = Profile.objects.filter(area__contains='Jadesola')
            elif "adeniyi" in query:
                members = Profile.objects.filter(area__contains='Adeniyi')
            elif "abiola" in query:
                members = Profile.objects.filter(area__contains='Abiola')
            elif "wesco" in query:
                members = Profile.objects.filter(area__contains='WESCO')
            elif "futascoops" in query:
                members = Profile.objects.filter(area__contains='FUTASCOOPS')
            elif "akad" in query:
                members = Profile.objects.filter(area__contains='Akad')
            elif "auditorium" in query:
                members = Profile.objects.filter(area__contains='Auditorium')
            elif "cassava" in query:
                members = Profile.objects.filter(area__contains='Cassava')
            elif "oritaobele" in query:
                members = Profile.objects.filter(area__contains='Oritaobele')
            elif "embassy" in query:
                members = Profile.objects.filter(area__contains='Embassy')
            elif "aba" in query:
                members = Profile.objects.filter(area__contains='Aba')
            elif "redemption" in query:
                members = Profile.objects.filter(area__contains='Redemption')
            elif query=="":
                members = Profile.objects.all()
              
            else:
                raise Exception("Empty string")

            context = {
            'query':query,
            'members':members,
            }
            return render(request, 'members_list.html', context)
        except Exception:
            return render(request, 'members_list.html')
    else:
        query = ""
        return render(request, 'members_list.html', {'query':query,})
