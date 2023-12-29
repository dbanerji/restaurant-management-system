from django.db import models

# Create your models here.
class Table(models.Model):
    class Seat(models.IntegerChoices):
        OneSeater = 1
        TwoSeater = 2
        ThreeSeater = 3
        FourSeater = 4
        FiveSeater = 5
        SixSeater = 6
    class Table_Status(models.TextChoices):
        Free = "Free"
        Reserved = "Reserved"
        Occupied = "Occupied"
    numberOfSeats = models.IntegerField(
        max_length=10,
        choices=Seat,
        default=1)
    status = models.CharField(
        max_length = 10, 
        choices=Table_Status,
        default=Table_Status.Free)  
    
class Menu_Items(models.Model):
    class Menu_Section(models.TextChoices):
        Breakfast = "BreakFast"
        Lunch = "Lunch"
        Dinner = "Dinner"
    section = models.CharField(
        max_length=30,
        choices = Menu_Section)
    name = models.CharField(max_length=65)
    price = models.FloatField

class Reservations(models.Model):
    class Reservation_Status(models.TextChoices):
        Reserved = "Reserved"
        Canceled = "Canceled"
    status = models.CharField(max_length=30,choices=Reservation_Status)
    date = models.DateField()
    customerName = models.CharField(max_length=100)
    numberOfPeople = models.IntegerField(max_length=10)




