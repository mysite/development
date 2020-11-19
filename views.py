from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from dev.models import Room_Climate, Test

from dev.serializers import Room_ClimateSerializer, PersonVehicleSerializer

# Create your views here.

def index(request):
	climate = Room_Climate.objects.order_by('-time')[:80]
	context = {'climate': climate}
	return render(request, 'dev/index.html', context)

@api_view(["POST"])
def PersonVehicle(request):
	# Deserialize the information provided in the request
	ser = PersonVehicleSerializer(data=request.data)
	# Validate the information provided
	ser.is_valid(raise_exception=True)
	# Save the information in the datawarehouse
	ser.save()
	return Response({"All good, everything has been saved"})

@api_view(["POST"])
def Climate(request):
	ser = Room_ClimateSerializer(data=request.data)
	ser.is_valid(raise_exception=True)
	ser.save()
	return Response({"Worked just fine"})
