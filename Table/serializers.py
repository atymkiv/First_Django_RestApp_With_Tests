from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
 	class Meta:
 		model = Student
 		fields = ["id", "firstName","lastName","midName","rate"]

"""def create(self, validated_data):
	student_data = validated_data.pop('student')
 	student, created = Student.objects.get_or_create(lastName=student_data['second_name'], **validated_data)
	return student

def update(self, instance, validated_data):
	student_data = validated_data.pop('student')
	category, created = Student.objects.get_or_create(lastName=student_data['second_name'], **validated_data)
 for fname, fvalue in validated_data.items():
 setattr(instance, fname, fvalue)
 instance.category = category
 instance.save()
 return instance"""