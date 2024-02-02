from django.shortcuts import render, redirect
from .models import Menu_Items, Reservations, Table, Booking
from .forms import ReservationForm


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
    is_full = False
    if request.method == 'POST':
        model = Reservations
        form = ReservationForm(request.POST or None)
        
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.table = reserveTable(form.cleaned_data.get("number_of_people"))
            if reservation.table is None:
                is_full =True
            else:
                reservation.save()
                return redirect("rms_app:home")
    else:
        form = ReservationForm()
    
    return render(request,"rms_app/reservations.html",{"form":form,"is_full":is_full})
    
def reserveTable(number_of_people):

    free_one_seaters = Table.objects.filter(table_status="Free",number_of_seats=1)
    free_two_seaters = Table.objects.filter(table_status="Free",number_of_seats=2)
    
    one_booked = Booking.one_seater_available
    two_booked = Booking.two_seater_available

    if not free_one_seaters.exists():
        one_booked.available = False

    if not free_two_seaters.exists():
        two_booked.available = False

    if number_of_people==1 and one_booked:
        for table in free_one_seaters:
            table.status = "Reserved"
            table.save()
            return table

    elif number_of_people==2 and two_booked:
        for table in free_two_seaters:
            table.status = "Reserved"
            table.save()
            return table
    else:
        return None
        


    
    
