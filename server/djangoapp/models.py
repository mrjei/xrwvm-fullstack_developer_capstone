# Uncommented imports
from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
# Car Make model
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=100, default='')
    description = models.TextField()
   
    def __str__(self):
        return self.name  # Return the name as the string representation

# Car Model model
class CarModel(models.Model):
    # Many-To-One relationship to Car Make model (One Car Make has many Car Models)
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
   
    name = models.CharField(null=False, max_length=100, default='')
   
    # Type choices for the car
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('COUPE', 'Coupe'),
        ('CONVERTIBLE', 'Convertible'),
        ('HATCHBACK', 'Hatchback'),
        ('TRUCK', 'Truck'),
    ]
   
    type = models.CharField(null=False, max_length=15, choices=CAR_TYPES, default='SEDAN')
   
    # Year field with min value 2015 and max value 2023
    year = models.IntegerField(default=2023,
                              validators=[
                                  MinValueValidator(2015),
                                  MaxValueValidator(2023)
                              ])
   
    def __str__(self):
        return f"{self.car_make.name} {self.name}"  # Return car make and model name