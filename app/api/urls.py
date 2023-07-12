from django.urls import path, include
from app.api.views import RoomReservationAPIView, TrainReservationAPIView

urlpatterns = [
    path('reservations/room/', RoomReservationAPIView.as_view(), name='hotel_reservation_api'),
    path('reservations/train/', TrainReservationAPIView.as_view(), name='train_reservation_api'),
]
