from django.contrib import admin
from .models import Room_Climate, Share, Share_Movement
#from .models import Person, Vehicle, PersonVehicle

class ClimateView(admin.ModelAdmin):
    list_display = ('id'
    		,'room'
    		,'temperature'
    		,'humidity'
            ,'time'
            )

admin.site.register(Room_Climate, ClimateView)

class ShareView(admin.ModelAdmin):
    list_display = ('id'
    		,'share_name'
    		,'share_id'
    		)

admin.site.register(Share, ShareView)

class ShareMovement(admin.ModelAdmin):
    list_display = ('created_at' 
			,'updated_at' 
			,'share_id' 
			,'time_of_purchase'
			,'prize'
            ,'currency'
            ,'exchange_rate'
			,'quantity'
			,'cost'
			,'expenses'
    		)

admin.site.register(Share_Movement, ShareMovement)

#admin.site.register(Person)
#admin.site.register(Vehicle)
#admin.site.register(PersonVehicle)