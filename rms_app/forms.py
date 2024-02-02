from django import forms

from .models import Reservations

class ReservationForm(forms.ModelForm):

    class Meta:
        model = Reservations
        fields= ["datetime","customer_name","number_of_people"]
        exclude= ["table"]
   
