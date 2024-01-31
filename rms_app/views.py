from django.shortcuts import render
from .models import Menu_Items
from .forms import ReservationForm
from .models import Reservations
from .models import Table
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"rms_app/home.html")

def about(request):
    return render(request,"rms_app/about.html")

def menu(request):
    menu_items = Menu_Items.objects.all()
    breakfast_items = []
    lunch_items = []
    dinner_items = []
    for item in menu_items:
        if item.section == "BreakFast":
            breakfast_items.append(item)
        elif item.section == "Lunch":
            lunch_items.append(item)
        else:
            dinner_items.append(item)
    return render(request,"rms_app/menu.html",{"breakfast_items":breakfast_items,"lunch_items":lunch_items,"dinner_items":dinner_items})

def reservations(request):
    if request.method == 'POST':
        model = Reservations
        form = ReservationForm(request.POST or None)
        
        if form.is_valid():
            reservation =form.save(commit=False)
            reservation.table = reserveTable(form.cleaned_data.get("numberOfPeople"))
            reservation.save()
            return redirect("rms_app:home")
    else:
        form = ReservationForm()
    
    return render(request,"rms_app/reservations.html",{"form":form})
    
def reserveTable(numberOfPeople):

    free_one_seaters = Table.objects.filter(status="Free",numberOfSeats=1)
    free_two_seaters = Table.objects.filter(status="Free",numberOfSeats=2)

    if numberOfPeople==1:
        for table in free_one_seaters:
            table.status = "Reserved"
            table.save()
            return table
    elif numberOfPeople==2:
        for table in free_two_seaters:
            table.status = "Reserved"
            table.save()
            return table
        


    
    
