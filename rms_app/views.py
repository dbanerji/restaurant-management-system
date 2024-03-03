from django.shortcuts import render, redirect
from .models import Menu_Items, Guest, Table, Reservation
from .forms import ReservationForm
from django.utils import timezone
from django.db import transaction

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
        form = ReservationForm(request.POST or None)
        
        if form.is_valid():
            if form.cleaned_data.get("reservation_datetime") < timezone.now():
                return redirect("rms_app:home")
            reservation = create_reservation(form)
            if reservation:
                return redirect("rms_app:home")
            else:
                print(reservation)
                return redirect("rms_app:reservations")
    else:
        form = ReservationForm()
    
    return render(request,"rms_app/reservations.html",{"form":form})
    

def create_reservation(form):
    with transaction.atomic():
        guest = Guest(name=form.cleaned_data.get("guest_name"), phone_number=form.cleaned_data.get("guest_phone"))
        guest.save()

        capacity = form.cleaned_data.get("num_guests")
        tables = Table.objects.filter(capacity__gte=int(capacity)).order_by('-capacity')
        table_ids = [t.id for t in tables]

        if not table_ids:
            print("No tables")
            return False

        reservations = Reservation.objects.filter(table__id__in=table_ids, datetime=form.cleaned_data.get("reservation_datetime"))

        if len(table_ids) == len(reservations):
            print("All tables booked")
            return False
        else:
            reserved_table_ids = [r.table.id for r in reservations]
            available_table_ids = set(table_ids) - set(reserved_table_ids)
            table_id = available_table_ids.pop()

        print(Table.objects.get(id=table_id))
        print(guest)

        # Explicitly set all fields for the Reservation model
        reservation = Reservation()
        reservation.table = Table.objects.get(id=table_id)
        reservation.guest = guest
        reservation.datetime = form.cleaned_data.get("reservation_datetime")
        reservation.number_of_guests = capacity

        reservation.save()

    return reservation

