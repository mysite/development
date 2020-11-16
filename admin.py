from django.contrib import admin
from .models import Room_Climate, Person, Vehicle, PersonVehicle

# Register your models here.
admin.site.register(Room_Climate)
admin.site.register(Person)
admin.site.register(Vehicle)
admin.site.register(PersonVehicle)
