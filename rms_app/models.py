from django.db import models
from django.utils import timezone

# Create your models here.
MAX_SEATS = 10

class Menu_Items(models.Model):
    class Menu_Section(models.TextChoices):
        BREAKFAST = "BreakFast"
        LUNCH = "Lunch"
        DINNER = "Dinner"
    section = models.CharField(Menu_Section.choices,max_length=20)
    name = models.CharField(max_length=65)
    description = models.TextField()
    price = models.FloatField()

class Table(models.Model):
    capacity = models.IntegerField()
    
class Guest(models.Model):
    name = models.CharField(max_length=65)
    phone_number = models.CharField(max_length=10, unique=True)

class Reservation(models.Model):
    table = models.ForeignKey(Table, null=True, on_delete=models.CASCADE)
    guest = models.ForeignKey(Guest,null=True,on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=timezone.now())
    number_of_guests = models.IntegerField()


