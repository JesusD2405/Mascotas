from django.db import models
from django.utils import timezone


# Modelo Iventario

class Inventory(models.Model):

	# Atributos

	typeInventory = models.CharField(max_length=120)
	quantity      = models.IntegerField()
	total         = models.DecimalField(max_digits=12, decimal_places=2)


# Modelo Producto

class Product(models.Model):

	# Atributos

	code = models.CharField(max_length=120)
	name = models.CharField(max_length=120)
	brand = models.CharField(max_length=120)
	description = models.CharField(max_length=120)
	quantity  = models.IntegerField()
	price  = models.DecimalField(max_digits=12, decimal_places=2)
	due_date = models.DateTimeField()

	#Claves Foráneas 
	inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, blank=True)




