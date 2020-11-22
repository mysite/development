from rest_framework import serializers
from dev.models import Room_Climate
#from dev.models import Person, PersonVehicle, Vehicle

class Room_ClimateSerializer(serializers.Serializer):
	room = serializers.CharField(max_length=200)
	temperature = serializers.FloatField()
	humidity = serializers.FloatField()

	def create(self, validated_data):
		return Room_Climate.objects.create(**validated_data)

#class VehicleSerializer(serializers.Serializer):
#	registration_plate = serializers.CharField(max_length=100)

#class PersonVehicleSerializer(serializers.Serializer):
#	first_name = serializers.CharField(max_length=100)
#	last_name = serializers.CharField(max_length=100)
#	email = serializers.CharField(max_length=100)
#	vehicles = VehicleSerializer(many=True)

#	def save(self):
#		# First update or create the person
#		person_obj, created = Person.objects.update_or_create(
#			first_name=self.validated_data["first_name"],
#			last_name=self.validated_data["last_name"],
#			defaults={"email": self.validated_data["email"]},
#			)
#		# Then create each Vehicle and link it to the person created before
#		for vehicle in self.validated_data["vehicles"]:
#			vehicle_obj, created =  Vehicle.objects.get_or_create(registration_plate=vehicle["registration_plate"])
#			personvehicle_obj, created = PersonVehicle.objects.update_or_create(
#				vehicle=vehicle_obj, defaults={"person": person_obj}
#				)
