from django.db import models
# Create your models here.

class BookTrip(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    phone = models.CharField(max_length=20, blank=False, null=False)
    destination = models.CharField(max_length=100 , blank=False, null=False)
    date = models.DateField(blank=False, null=False)
    
    def __str__(self):
        return self.name
    
class Facilities(models.Model):
    Dining_Options = models.CharField(max_length=100, blank=False, null=False)
    Entertainment_Activities = models.CharField(max_length=100, blank=False, null=False)
    Accommodation_Details = models.CharField(max_length=100, blank=False, null=False)
    
    def __str__(self):
        return self.Dining_Options