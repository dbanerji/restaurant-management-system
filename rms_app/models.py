from django.db import models
from datetime import datetime
# Create your models here.
class Table(models.Model):
    class Seat(models.IntegerChoices):
        OneSeater = 1
        TwoSeater = 2
    class Table_Status(models.TextChoices):
        Free = "Free"
        Reserved = "Reserved"
    numberOfSeats = models.IntegerField(Seat.choices)
    status = models.CharField(Table_Status.choices,max_length=255)  
    
class Menu_Items(models.Model):
    class Menu_Section(models.TextChoices):
        Breakfast = "BreakFast"
        Lunch = "Lunch"
        Dinner = "Dinner"
    section = models.CharField(Menu_Section.choices,max_length=255)
    name = models.CharField(max_length=65)
    description = models.CharField(max_length=255)
    price = models.FloatField()

class Reservations(models.Model):
    table = models.ForeignKey(Table, null=True, on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=datetime.now())
    customerName = models.CharField(max_length=100)
    numberOfPeople = models.IntegerField()

class TimeSlots(models.Model):
    time_start = models.TimeField()
    time_end = models.TimeField()

class OneSeater_Booked(models.Model):
    available = models.BooleanField()

class TwoSeater_Booked(models.Model):
    available = models.BooleanField()

