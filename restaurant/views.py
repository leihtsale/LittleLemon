from django.shortcuts import render
from rest_framework.throttling import UserRateThrottle
from rest_framework import (
    viewsets,
    generics,
    permissions,
)

from . import serializers
from .models import Booking, MenuItem


def index(request):
    return render(request, 'restaurant/index.html')


def about(request):
    return render(request, 'restaurant/about.html')


class MenuItemView(generics.ListCreateAPIView):

    queryset = MenuItem.objects.all()
    serializer_class = serializers.MenuItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    ordering_fields = ['price', 'inventory']
    search_fields = ['title']
    throttle_classes = [UserRateThrottle]


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):

    queryset = MenuItem.objects.all()
    serializer_class = serializers.MenuItemSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookingViewSet(viewsets.ModelViewSet):

    queryset = Booking.objects.all()
    serializer_class = serializers.BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
    ordering_fields = ['no_of_guests', 'booking_date']
    search_fields = ['name']
    throttle_classes = [UserRateThrottle]
