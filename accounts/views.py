from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from .models import User


def loginPage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home-page')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')



def register(request):
    if request.method == 'POST' and request.FILES['picture']:
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        picture = request.FILES['picture']
        fs = FileSystemStorage()
        filename = fs.save(picture.name, picture)
        user = User.objects.create_superuser(email=email, first_name=first_name, last_name=last_name,
                                                address=address, password=password, phone=phone, profile_pic=picture)
        if user is not None:
            login(request, user)
            return redirect('login')
        else:
            messages.add_message(request, messages.error, 'Please Review Your Data Failed To Register')
    context = {}
    return render(request, 'accounts/register.html', context)




