from django.contrib import admin
from .models import CarMake, CarModel

# Register CarMake model
admin.site.register(CarMake)

# Register CarModel model  
admin.site.register(CarModel)