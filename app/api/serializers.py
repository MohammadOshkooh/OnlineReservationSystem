from rest_framework import serializers
from app.models import Hotel, Room, HotelReservation, TrainSeat, TrainReservation, Train


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    hotel = HotelSerializer()

    class Meta:
        model = Room
        fields = '__all__'


class HotelReservationSerializer(serializers.ModelSerializer):
    room = RoomSerializer()

    class Meta:
        model = HotelReservation
        fields = '__all__'


class TrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Train
        fields = '__all__'


class TrainSeatSerializer(serializers.ModelSerializer):
    train = TrainSerializer()

    class Meta:
        model = TrainSeat
        fields = '__all__'


class TrainReservationSerializer(serializers.ModelSerializer):
    train = TrainSerializer()

    class Meta:
        model = TrainReservation
        fields = '__all__'
