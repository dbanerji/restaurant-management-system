from django.contrib import admin
from rms_app.models import Menu_Items,Reservation,Table,Guest

# Register your models here.
admin.site.register(Menu_Items)
admin.site.register(Reservation)
admin.site.register(Guest)
admin.site.register(Table)