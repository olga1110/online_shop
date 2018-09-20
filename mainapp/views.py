from django.shortcuts import render


def mainapp_catalog(request):
    return render(request,'mainapp/catalog.html', {})

def mainapp_Contacts(request):
    return render(request,'mainapp/Contacts.html', {})

def mainapp_index(request):
    return render(request,'mainapp/index.html', {})

def mainapp_registration(request):
    return render(request,'mainapp/registration.html', {})


# Create your views here.
