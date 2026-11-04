from django.shortcuts import render

def home(request):
    return render(request, 'mainapp/home.html')

def about(request):
    return render(request, 'mainapp/about.html')

def contacts(request):
    return render(request, 'mainapp/contacts.html')

def how_to_find(request):
    return render(request, 'mainapp/how_to_find.html')

def catalog(request):
    return render(request, 'mainapp/catalog.html')

def resources(request):
    return render(request, 'mainapp/resources.html')
