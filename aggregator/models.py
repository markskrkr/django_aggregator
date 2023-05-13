from django.db import models

# Create your models here.
from django.db import models

class Flight(models.Model):
    plane_number = models.CharField(max_length=100)
    departure_airport = models.CharField(max_length=100)
    destin_airport = models.CharField(max_length=100)
    departure_datetime = models.DateTimeField()
    arrival_datetime = models.DateTimeField()
    seatbusi_occupied = models.IntegerField()
    max_seatbusi = models.IntegerField()
    seatbusi_price = models.FloatField()
    seatcoom_occupied = models.IntegerField()
    max_seatcoom = models.IntegerField()
    seatcoom_price = models.FloatField()
    seatfirst_occupied = models.IntegerField()
    max_seatfirst = models.IntegerField()
    seatfirst_price = models.FloatField()

    def __str__(self):
        return f"{self.departure_airport} - {self.destin_airport} ({self.departure_datetime})"


class Refund(models.Model):
    booking = models.ForeignKey('Booking', on_delete=models.CASCADE)
    customer_id = models.CharField(max_length=20)
    refund_time = models.DateTimeField()

    def __str__(self):
        return f"Refund {self.id} for Booking {self.booking_id}"


class Booking(models.Model):
    payment_id = models.IntegerField()
    stamp = models.CharField(max_length=100)
    flight = models.ForeignKey('Flight', on_delete=models.CASCADE)

    def __str__(self):
        return f"Booking {self.id} for Flight {self.flight_id}"


class Customer(models.Model):
    booking = models.ForeignKey('Booking', on_delete=models.CASCADE)
    customer_id = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    seat_type = models.CharField(max_length=20)
    status = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} (Booking {self.booking_id})"