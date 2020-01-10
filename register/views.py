from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import auth
import time
from .forms import UserForm
from .models import user

# Create your views here.
def register(req):
    try:
        if(req.method == 'POST'):
            form=UserForm(req.POST , req.FILES)
            if form.is_valid():
                form.save()
                return redirect('/validation')
                #return HttpResponse('<script>alert("Registration Successful....Now you can login.");</script>')
        else:
            form = UserForm()
        return render(req,'register.html',{'form' : form})
    except:
        return render(req,'register.html')

def validation(req):
    return HttpResponse('<h1>Registration Successfull</h1><div class="card-footer"><a class="btn btn-primary"  href="../">Log in instead<i  aria-hidden="true"></i></a></div>')