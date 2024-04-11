from django.shortcuts import render,HttpResponse
from datetime import datetime
from p.models import Contact

# Create your views here.
# def index(request):
#     context={
#         'variable':"mahak is great"
#     }
#     return render(request,'index.html',context)


def index(request):
     if request.method=="POST":
         name=request.POST.get('name')
         phone=request.POST.get('phone')
         email=request.POST.get('email')
         desc=request.POST.get('desc')
         contact= Contact(name=name,phone=phone,email=email,desc=desc,date=datetime.today())
         contact.save()
     return render(request,'index.html')
     #return HttpResponse("this is a contact page")
   