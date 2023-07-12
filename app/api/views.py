from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from app.models import Room, HotelReservation, Train, TrainSeat, TrainReservation
from .serializers import RoomSerializer, HotelReservationSerializer, TrainSeatSerializer, TrainReservationSerializer
from rest_framework import permissions


class RoomReservationAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        rooms = Room.objects.filter(is_reserved=False, is_available=True)
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)

    def post(self, request):
        room_id = request.data.get('room_id')
        check_in = request.data.get('check_in')
        check_out = request.data.get('check_out')

        room = get_object_or_404(Room, pk=room_id)
        if not room.is_available or room.is_reserved:
            return Response({'error': 'The room is not available.'}, status=400)

        reservation = HotelReservation(
            user=request.user,
            room=room,
            check_in=check_in,
            check_out=check_out
        )
        reservation.save()

        room.is_available = False
        room.is_reserved = True
        room.save()

        serializer = HotelReservationSerializer(reservation)

        return Response({'data': serializer.data, 'message': f'اتاق {room.number} با موفقیت رزرو شد'}, status=200)


class TrainReservationAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        train_seats = TrainSeat.objects.filter(is_reserved=False)
        serializer = TrainSeatSerializer(train_seats, many=True)
        return Response(serializer.data)

    def post(self, request):
        train_id = request.data.get('train_id')
        reserved_seat = request.data.get('reserved_seat')
        train = get_object_or_404(Train, id=train_id)
        seat = get_object_or_404(TrainSeat, train=train, number=reserved_seat)

        if seat.is_reserved:
            return Response({'error': 'The seat is not available.'}, status=400)

        reservation = TrainReservation(
            user=request.user,
            train=train,
            reserved_seat=seat
        )
        reservation.save()

        seat.is_reserved = True
        seat.save()

        serializer = TrainReservationSerializer(reservation)

        return Response({'data': serializer.data, 'message': f'بلیظ {seat.number} با موفقیت رزرو شد.'}, status=200)
