from django.db import models

class Student(models.Model):
	firstName = models.CharField(max_length = 30)
	midName =models.CharField(max_length=30)
	lastName = models.CharField(max_length=30)
	rate = models.FloatField()
	def __str__(self):
		return self.lastName
# Create your models here.
