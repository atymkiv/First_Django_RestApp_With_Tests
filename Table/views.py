from .models import Student
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from .serializers import StudentSerializer



class RESTStudentList(generics.ListCreateAPIView):
	queryset = Student.objects.order_by('-rate')
	serializer_class = StudentSerializer

class RESTStudentDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer


