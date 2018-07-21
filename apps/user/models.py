from django.db import models
from django.utils import timezone


# Modelo Usuario

class User(models.Model):

	# Atributos

	name      = models.CharField(max_length=120)
	lastName  = models.CharField(max_length=120)
	email     = models.CharField(max_length=120)
	username  = models.CharField(max_length=120)
	password  = models.CharField(max_length=120)
	answer1   = models.CharField(max_length=120)
	answer2   = models.CharField(max_length=120)
	answer3   = models.CharField(max_length=120)
	birthdate = models.DateTimeField()


# Modelo Cliente

class Client(models.Model):

	# Atributos

	name                 = models.CharField(max_length=120)
	lastName             = models.CharField(max_length=120)
	identification_card  = models.CharField(max_length=11)
	email                = models.CharField(max_length=120)
	phone                = models.CharField(max_length=11)
	address              = models.CharField(max_length=120)

	#Claves Foráneas 
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)