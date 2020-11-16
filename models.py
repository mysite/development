from django.db import models
from datetime import datetime
from simple_history.models import HistoricalRecords
# Create your models here.

class Test(models.Model):
	column1 = models.CharField(max_length=100)

class Room_Climate(models.Model):
	room = models.CharField('room', max_length=200)
	temperature = models.FloatField('temperature',null=True,blank=True)
	humidity = models.FloatField('humidity',null=True,blank=True)
	time = models.DateTimeField('time', default=datetime.now)

	def __str__(self):
		return self.room

class Person(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	history = HistoricalRecords()

	class Meta:
		unique_together = (("first_name","last_name"),)

	def __str__(self):
		return "{} {}".format(self.first_name, self.last_name)

class Vehicle(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	registration_plate = models.CharField(max_length=100)

	def __str__(self):
		return self.registration_plate

class PersonVehicle(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	vehicle = models.ForeignKey(Vehicle, on_delete=models.PROTECT)
	person = models.ForeignKey(Person, on_delete=models.PROTECT)
	history = HistoricalRecords()

	class Meta:
		 unique_together = (("vehicle"),)

	def __str__(self):
		return "{} {}".format(self.vehicle, self.person)
