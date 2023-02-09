from rest_framework import (
    viewsets,
    generics,
    permissions,
)

from . import serializers
from .models import Booking, MenuItem


class MenuItemView(generics.ListCreateAPIView):

    queryset = MenuItem.objects.all()
    serializer_class = serializers.MenuItemSerializer
    permission_classes = [permissions.IsAuthenticated]


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):

    queryset = MenuItem.objects.all()
    serializer_class = serializers.MenuItemSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookingViewSet(viewsets.ModelViewSet):

    queryset = Booking.objects.all()
    serializer_class = serializers.BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
