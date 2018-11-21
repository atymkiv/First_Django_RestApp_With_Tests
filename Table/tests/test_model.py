from django.urls import reverse, resolve, path
from ..models import Student
import pytest
class TestsRate:
	@pytest.mark.django_db
	def test_rate(self):
		student = Student.objects.create(firstName='name', lastName='lastName', midName='midName', rate='100.0')
		assert student.firstName == "name"
		assert student.lastName == "lastName"
		assert student.midName == "midName"
		assert student.rate == '100.0'