from django.contrib.auth import get_user_model

from rest_framework import (
    viewsets,
    generics,
    permissions,
)

from . import serializers
from .models import Booking, MenuItem


class UserViewSet(viewsets.ModelViewSet):

    queryset = get_user_model().objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class MenuItemView(generics.ListCreateAPIView):

    queryset = MenuItem.objects.all()
    serializer_class = serializers.MenuSerializer
    permission_classes = [permissions.IsAuthenticated]


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):

    queryset = MenuItem.objects.all()
    serializer_class = serializers.MenuSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookingViewSet(viewsets.ModelViewSet):

    queryset = Booking.objects.all()
    serializer_class = serializers.BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
