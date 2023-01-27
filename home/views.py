from django.shortcuts import render,redirect
from . models import Contact, Product
from django.contrib import messages

# Create your views here.

def index(request):
    data = Product.objects.all()
    return render(request,'app/home.html',{'data':data})

def about(request):
    return render(request,'app/about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        if Contact.objects.filter(email=email).exists():
            messages.info (request,'Email Already Exists')
            return redirect('/contact')
        data = Contact.objects.create(name=name,email=email,subject=subject,message=message)
        data.save()
        messages.success(request,"Contact Share Succesfuly")
        return render(request,'app/contact.html',{'data':data})
    return render(request,'app/contact.html')

