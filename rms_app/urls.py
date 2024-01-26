from django.urls import path

from .import views

app_name='rms_app'
urlpatterns=[
    path('',views.home,name ="home"),
    path('menu/',views.menu,name ="menu"),
    path('about/',views.about,name ="about"),
    path('reservations/',views.reservations,name ="reservations")

    ]
