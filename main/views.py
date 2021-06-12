from django.shortcuts import render
from .models import Contact


def home_page(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        contact = Contact(name=name, email=email, phone=phone)
        contact.save()
        return render(request, 'main/home.html')

    return render(request, 'main/home.html')
