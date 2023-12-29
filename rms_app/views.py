from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"rms_app/home.html")

def about(request):
    return render(request,"rms_app/about.html")

def menu(request):
    return render(request,"rms_app/menu.html")

def reservations(request):
    return render(request,"rms_app/reservations.html")
    