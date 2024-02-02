from django.contrib import admin
from rms_app.models import Menu_Items
from rms_app.models import Reservations
from rms_app.models import Table
# Register your models here.
admin.site.register(Menu_Items)
admin.site.register(Reservations)
admin.site.register(Table)