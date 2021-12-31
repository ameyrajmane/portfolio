from django.shortcuts import render, HttpResponse
from home.models import Contact


# Create your views here.

def home(request):
    # return HttpResponse("This is home page (/) ")
    return render(request, 'home.html')


def about(request):
    # return HttpResponse("This is about page (/about) ")
    return render(request, 'about.html')


def projects(request):
    # return HttpResponse("This is projects.html page (/projects.html) ")
    return render(request, 'projects.html')


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        # print(name, email, phone, desc)
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        print("The data has been submitted")
    # return HttpResponse("This is contact page (/contact) ")
    return render(request, 'contact.html')
