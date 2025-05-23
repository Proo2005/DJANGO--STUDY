from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages




# Create your views here.
def index(request):
  
  return render(request,"index.html")

def about(request):
  return render(request,"about.html")



def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        
        phone = request.POST.get('phone')

        # Create an instance of the Contact model
        contact = Contact(name=name, phone=phone)
        contact.save()  # Now this will work

        messages.success(request, "Your message has been sent.")
        

    return render(request, 'contact.html')


def services(request):
  return render(request,"services.html")

