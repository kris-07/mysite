from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import auth
import time
from register.models import user
# Create your views here.

def login(req):
    try:
        if(req.method=='POST'):
            email=req.POST["email"]
            password=req.POST["pass"]

            if(user.objects.filter(email=email).exists() ):
                if(user.objects.filter(password=password).exists()):

                    id=user.objects.get(email=email).id
                    id='/'+str(id)
                    return redirect((id))
            else:
                return render(req,'login.html')
    except:
        return render(req,'login.html')
    return render(req,'login.html')


def userinfo(req, id=None):

    #id = int(uid.id)
    return render(req,'userinfo.html',{'user' : user.objects.get(id=id)})