from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Student(models.Model):
	firstName = models.CharField(max_length = 30)
	midName =models.CharField(max_length=30)
	lastName = models.CharField(max_length=30)
	rate = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(100.0)],)
	def __str__(self):
		return self.lastName
# Create your models here.
