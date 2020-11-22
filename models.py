from django.db import models
from datetime import datetime
from simple_history.models import HistoricalRecords

class Room_Climate(models.Model):
	room = models.CharField('room', max_length=200)
	temperature = models.FloatField('temperature',null=True,blank=True)
	humidity = models.FloatField('humidity',null=True,blank=True)
	time = models.DateTimeField('time', default=datetime.now)

	def __str__(self):
		return self.room

class Share(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	share_name = models.CharField(max_length=100)
	share_id = models.CharField(max_length=100)

	def __str__(self):
		return self.share_id

class Share_Movement(models.Model):
	currencies = (
    ('euro','Euro'),
    ('usd', 'USD'),
    )
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	share_id = models.ForeignKey(Share, on_delete=models.PROTECT)
	time_of_purchase = models.DateTimeField('time', default=datetime.now)
	prize = models.FloatField('prize',null=True,blank=True)
	currency = models.CharField(max_length=10, choices=currencies, default='no')
	exchange_rate = models.FloatField('exchange_rate',null=True,blank=True)
	quantity = models.FloatField('quantity',null=True,blank=True)
	cost = models.FloatField('cost',null=True,blank=True)
	expenses = models.FloatField('expenses',null=True,blank=True)
	
	#category_landscape = 1
    #category_people = 2
    #category_random = 3
    #category_wall = 4
    #category_project = 5
    #categories = (
    #    (category_landscape, 'Landscape'),
    #    (category_people, 'People'),
    #    (category_random, 'Random'),
    #    (category_wall, 'Wall'),
    #    (category_project, 'Project'),
    #)
    #category = models.SmallIntegerField('Category', choices=categories, default=category_wall)
    
#class Person(models.Model):
#	created_at = models.DateTimeField(auto_now_add=True)
#	updated_at = models.DateTimeField(auto_now=True)
#	first_name = models.CharField(max_length=100)
#	last_name = models.CharField(max_length=100)
#	email = models.CharField(max_length=100)
#	history = HistoricalRecords()

#	class Meta:
#		unique_together = (("first_name","last_name"),)

#	def __str__(self):
#		return "{} {}".format(self.first_name, self.last_name)

#class Vehicle(models.Model):
#	created_at = models.DateTimeField(auto_now_add=True)
#	updated_at = models.DateTimeField(auto_now=True)
#	registration_plate = models.CharField(max_length=100)

#	def __str__(self):
#		return self.registration_plate

#class PersonVehicle(models.Model):
#	created_at = models.DateTimeField(auto_now_add=True)
#	updated_at = models.DateTimeField(auto_now=True)
#	vehicle = models.ForeignKey(Vehicle, on_delete=models.PROTECT)
#	person = models.ForeignKey(Person, on_delete=models.PROTECT)
#	history = HistoricalRecords()

#	class Meta:
#		 unique_together = (("vehicle"),)

#	def __str__(self):
#		return "{} {}".format(self.vehicle, self.person)

