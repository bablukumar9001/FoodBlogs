from ast import Param
from datetime import datetime
from multiprocessing import context
from django.shortcuts import render,HttpResponse
from blogs.models import Contact
from django.contrib import messages 

# Create your views here.
def index(request):
    
     Param={ 
          "variable1":"here is abahy kumar ",
          "variable2":"here is rahul kumar "
     }

     return render (request, 'index.html',Param)  
    

def about(request):
     return render (request, 'about.html')  


def services(request):
     return render (request, 'service.html')  


def contact(request):
     if request.method=="POST":
         name=request.POST.get('name')
         email=request.POST.get('email')
         phone=request.POST.get('phone')
         desc=request.POST.get('desc')
         contact=Contact(name=name,email=email,phone=phone, desc=desc)
         contact.save()
         messages.success( request,"Your form has been submit!")
     return render (request, 'contact.html')  



