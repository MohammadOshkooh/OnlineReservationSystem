from django.utils import timezone

from django.contrib.auth import get_user_model
from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    description = models.TextField()
    image = models.ImageField(upload_to='hotels/', null=True, blank=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=15, decimal_places=0)
    is_available = models.BooleanField(default=True)
    is_reserved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.hotel} / {self.room_type}'


class HotelReservation(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField(default=timezone.now)
    check_out = models.DateField()

    def __str__(self):
        return self.user


class Train(models.Model):
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    number_seats = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.name}  ({self.origin} / {self.destination})'


class TrainSeat(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    is_reserved = models.BooleanField(default=False)

    def __str__(self):
        return self.number


class TrainReservation(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    reserved_seat = models.ForeignKey('TrainSeat', on_delete=models.CASCADE)

    def __str__(self):
        return self.train

