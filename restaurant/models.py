from django.db import models
from django.core.validators import MaxValueValidator


class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.PositiveSmallIntegerField(
                        validators=[MaxValueValidator(6)]
                    )
    bookingdate = models.DateTimeField()

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.PositiveIntegerField()

    def __str__(self):
        return self.title
