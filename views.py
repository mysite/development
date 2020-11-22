from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from dev.models import Room_Climate, Share, Share_Movement
from dev.serializers import Room_ClimateSerializer
#from dev.serializers import PersonVehicleSerializer

from smarthome.passwords import *

from alpha_vantage.timeseries import TimeSeries
import datetime
import pandas as pd
#from django.shortcuts import HttpResponse
import json

def index(request):
	return render(request, 'dev/index.html')

def smarthome(request):
	climate = Room_Climate.objects.order_by('-time')[:80]
	context = {'climate': climate}
	return render(request, 'dev/smarthome.html', context)

def temperature(request):
	climate = Room_Climate.objects.order_by('-time')[:80]
	context = {'climate': climate}
	return render(request, 'dev/temperature.html', context)

def humidity(request):
	climate = Room_Climate.objects.order_by('-time')[:80]
	context = {'climate': climate}
	return render(request, 'dev/humidity.html', context)

def share(request):
	shares = Share.objects.order_by('id')
	context = {'shares': shares}
	return render(request, 'dev/share.html', context)

def share_detail(request, share):
	shares = Share.objects.order_by('id')
	ts = TimeSeries(key = alpha_vantage_key, output_format='pandas')
	#share, metadata=ts.get_daily('WDI.DE', outputsize='compact')
	share_detail, metadata=ts.get_daily(share, outputsize='compact')
	share_detail.columns = ['open','high','low','close','volume']
	json_records = share_detail.reset_index().astype(str).to_json(orient = "records", date_format = "iso")
	data = []
	data = json.loads(json_records)
	context = {'share': data, 'shares': shares}
	return render(request, 'dev/share_detail.html', context)

def portfolio(request):
	shares = Share.objects.order_by('id')
	movements = Share_Movement.objects.order_by('id')
	ts = TimeSeries(key = 'TJ0VXVFQ9JBLWAUF', output_format='pandas')
	share_entries= []
	for movement in movements:
		share, metadata=ts.get_daily(movement.share_id, outputsize='compact')
		share_entrie = {}
		share_entrie['name'] = movement.share_id
		share_entrie['profit'] = round((share['4. close'].iloc[0]- movement.prize)*movement.quantity*movement.exchange_rate,2)
		share_entrie['earned'] = round((share['4. close'].iloc[0]- movement.prize)*movement.quantity*movement.exchange_rate-movement.cost-movement.expenses,2)
		share_entries.append(share_entrie)
	context = {'shares': shares, 'share':share_entries}
	return render(request, 'dev/portfolio.html', context)

@api_view(["POST"])
def Climate(request):
	ser = Room_ClimateSerializer(data=request.data)
	ser.is_valid(raise_exception=True)
	ser.save()
	return Response({"Worked just fine"})

#@api_view(["POST"])
#def PersonVehicle(request):
#	# Deserialize the information provided in the request
#	ser = PersonVehicleSerializer(data=request.data)
#	# Validate the information provided
#	ser.is_valid(raise_exception=True)
#	# Save the information in the datawarehouse
#	ser.save()
#	return Response({"All good, everything has been saved"})
