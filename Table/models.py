from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Student(models.Model):
	firstName = models.CharField(max_length = 30)
	midName =models.CharField(max_length=30)
	lastName = models.CharField(max_length=30)
	rate = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(100.0)],)
	def get_lastName(self):
		return 'Прізвище студента '+self.firstName + ' - ' + self.lastName+'.'
	def get_rate(self):
		return 'Рейтинг студента '+ self.firstName+ ' - ' + str(self.rate)+'.'
# Create your models here.
