from django.test import TestCase
from ..models import Student

# Create your tests here.
class Students(TestCase):
    """ Test module for Student model """

    def setUp(self):
        Student.objects.create(
            firstName='Петро', lastName='Петренко', midName='Петрович', rate='100')
        Student.objects.create(
            firstName='Віталій', lastName='Горішний', midName='Батькович', rate='95.5')

    def test_student_lastName(self):
        student_vyetal = Student.objects.get(firstName='Віталій')
        student_petro = Student.objects.get(firstName='Петро')
        self.assertEqual(
            student_vyetal.get_lastName(), "Прізвище студента Віталій - Горішний.")
        self.assertEqual(
            student_petro.get_lastName(), "Прізвище студента Петро - Петренко.")
        
    def test_student_rate(self):
    	student_vyetal = Student.objects.get(firstName='Віталій')
    	student_petro = Student.objects.get(firstName='Петро')
    	self.assertEqual(
    		student_vyetal.get_rate(), "Рейтинг студента Віталій - 95.5.")
    	self.assertEqual(
    		student_petro.get_rate(), "Рейтинг студента Петро - 100.0.")

