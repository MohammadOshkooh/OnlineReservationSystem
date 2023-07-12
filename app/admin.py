from django.contrib import admin

from .models import Hotel, Room, HotelReservation, TrainReservation, Train, TrainSeat

admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(HotelReservation)

admin.site.register(Train)
admin.site.register(TrainSeat)
admin.site.register(TrainReservation)
