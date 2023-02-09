from rest_framework import (
    viewsets,
    generics,
    permissions,
)

from . import serializers
from .models import Booking, Menu


class MenuView(generics.ListCreateAPIView):

    queryset = Menu.objects.all()
    serializer_class = serializers.MenuSerializer
    permission_classes = [permissions.IsAuthenticated]


class SingleMenuView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Menu.objects.all()
    serializer_class = serializers.MenuSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookingViewSet(viewsets.ModelViewSet):

    queryset = Booking.objects.all()
    serializer_class = serializers.BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
