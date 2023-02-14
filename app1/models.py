from django.db import models

class BookingTable(models.Model):
    name = models.CharField(max_length=100)
    no_of_guest = models.IntegerField()
    bookingdate = models.DateField()

class MenuTable(models.Model):
    title = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    inventory = models.IntegerField()
    
