from django import forms
from django.utils import timezone
from .models import MAX_SEATS

from datetime import datetime

class ReservationForm(forms.Form):
    guest_name = forms.CharField()
    guest_phone = forms.CharField()
    num_guests = forms.ChoiceField(choices = [(x, x) for x in range(1, MAX_SEATS)])
    reservation_datetime = forms.DateTimeField(widget=forms.DateTimeInput(format=('%Y-%m-%dT%H:%M')))


class ShowReservationsOnDateForm(forms.Form):
    reservation_date = forms.DateField()

class AddTableForm(forms.Form):
    table_capacity = forms.ChoiceField(choices = [(x, x) for x in range(1, MAX_SEATS)])