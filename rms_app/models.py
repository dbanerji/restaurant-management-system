from django.db import models
from django.utils import timezone

# Create your models here.

class Table(models.Model):
    class Seat(models.IntegerChoices):
        ONE_SEATER = 1
        TWO_SEATER = 2

    class Table_Status(models.TextChoices):
        FREE = "Free"
        RESERVED = "Reserved"
    number_of_seats = models.IntegerField(Seat.choices)
    table_status = models.CharField(Table_Status.choices,max_length=20)  
    
class Menu_Items(models.Model):
    class Menu_Section(models.TextChoices):
        BREAKFAST = "BreakFast"
        LUNCH = "Lunch"
        DINNER = "Dinner"
    section = models.CharField(Menu_Section.choices,max_length=20)
    name = models.CharField(max_length=65)
    description = models.TextField()
    price = models.FloatField()

class Reservations(models.Model):
    table = models.ForeignKey(Table, null=True, on_delete=models.CASCADE, related_name='reservations')
    datetime = models.DateTimeField(default=timezone.now)
    customer_name = models.CharField(max_length=100)
    number_of_people = models.IntegerField()

class TimeSlots(models.Model):
    time_start = models.TimeField()
    time_end = models.TimeField()

class Booking(models.Model):
    one_seater_available = models.BooleanField()
    two_seater_available = models.BooleanField()



