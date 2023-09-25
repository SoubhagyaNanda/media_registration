from django.shortcuts import render
from app.models import *
from app.forms import *
from django.core.mail import send_mail
from django.http import *
# Create your views here.

def Registration(request):
    UFO= UserForm()
    PFO= ProfileForm()
    d={'UFO':UFO,'PFO':PFO}

    if request.method=='POST' and request.FILES:
        UFDO= UserForm(request.POST)
        PFDO= ProfileForm(request.POST, request.FILES)

        if UFDO.is_valid() and PFDO.is_valid():
            MUFDO= UFDO.save(commit=False)
            MUFDO.set_password(UFDO.cleaned_data['password'])
            MUFDO.save()

            MUFDK=PFDO.save(commit=False)
            THVO= MUFDK.username=MUFDO
            THVO.save()

            send_mail('Registration',
                      'Congratulation... Successfully mail was send to the user mail id',
                      'soubhagyaranjannanda360@gmail.com',
                      [MUFDO.email],
                      fail_silently= False)
            return HttpResponse('Successfull...')
        
    return render(request,'registration.html',context=d)